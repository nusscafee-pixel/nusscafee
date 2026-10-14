import sys,math
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageEnhance,ImageChops
import os
S=os.environ.get('NUSS_WORK','/tmp/nuss/')  # folder with fonts/ products/ gen/ logo.png out/
W,H=1080,1350
TEAL=(47,112,104); TEAL_D=(35,92,86); WHITE=(245,243,238)
R=ImageFont.Layout.RAQM
def F(n,s): return ImageFont.truetype(S+'fonts/'+n+'.otf',s,layout_engine=R)
DB=lambda s:F('thmanyahserifdisplay-Bold',s); DM=lambda s:F('thmanyahserifdisplay-Medium',s)
SB=lambda s:F('thmanyahsans-Bold',s); SR=lambda s:F('thmanyahsans-Regular',s)

def cover(im,cx=.5,cy=.5,zoom=1.0):
    s=max(W/im.width,H/im.height)*zoom; im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=int((im.width-W)*cx); y=int((im.height-H)*cy); return im.crop((x,y,x+W,y+H))

def grade(im,focus=(.5,.62),fr=.42):
    im=ImageEnhance.Color(im).enhance(.78)
    dark=ImageEnhance.Brightness(im).enhance(.30)
    # teal tint in shadows
    tint=Image.new('RGB',im.size,(10,34,32)); dark=ImageChops.screen(dark,tint)
    lit=ImageEnhance.Brightness(im).enhance(.92)
    m=Image.new('L',(W//4,H//4),0); d=ImageDraw.Draw(m)
    fx,fy=focus[0]*W/4,focus[1]*H/4; r=fr*W/4
    d.ellipse([fx-r,fy-r*1.25,fx+r,fy+r*1.25],fill=255)
    m=m.filter(ImageFilter.GaussianBlur(r*.55)).resize((W,H),Image.LANCZOS)
    out=Image.composite(lit,dark,m)
    # top & bottom fade for text
    g=Image.new('L',(1,H)); 
    for y in range(H):
        t=max(0,1-y/(H*.36))**1.6*.75 + max(0,(y-H*.80)/(H*.20))**1.4*.8
        g.putpixel((0,y),int(255*min(1,t)))
    g=g.resize((W,H)); out=Image.composite(Image.new('RGB',(W,H),(8,12,11)),out,g)
    # grain
    n=Image.effect_noise((W,H),18).convert('RGB'); out=Image.blend(out,ImageChops.overlay(out,n),.18)
    return out

def tw(d,t,f): b=d.textbbox((0,0),t,font=f,direction='rtl',anchor='rs'); return b[2]-b[0]

def hl(base,d,x_right,y_base,text,f,pad=(14,6),skew=6,color=TEAL,below=.20):
    """teal parallelogram behind a word; x_right = right edge of word, baseline y"""
    b=d.textbbox((x_right,y_base),text,font=f,direction='rtl',anchor='rs')
    h=b[3]-b[1]; x0,x1=b[0]-pad[0],b[2]+pad[0]; y0=b[1]+h*.18; y1=b[3]+h*below
    lay=Image.new('RGBA',base.size,(0,0,0,0)); ld=ImageDraw.Draw(lay)
    ld.polygon([(x0,y0+skew),(x1,y0-skew/2),(x1,y1),(x0,y1+skew/2)],fill=color+(235,))
    base.alpha_composite(lay)

def text(d,x,y,t,f,fill=WHITE): d.text((x,y),t,font=f,fill=fill,direction='rtl',anchor='rs')

def arrow(base,pts,width=3,head=True):
    d=ImageDraw.Draw(base)
    # catmull-rom through pts
    P=[pts[0]]+pts+[pts[-1]]; out=[]
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        for k in range(20):
            t=k/20; t2,t3=t*t,t*t*t
            out.append(tuple(.5*((2*p1[j])+(-p0[j]+p2[j])*t+(2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2+(-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3) for j in (0,1)))
    out.append(pts[-1]); d.line(out,fill=WHITE,width=width,joint='curve')
    if head:
        (ax,ay),(bx,by)=out[-4],out[-1]; a=math.atan2(by-ay,bx-ax)
        for s in (2.5,-2.5):
            d.line([(bx,by),(bx-18*math.cos(a+s*.2),by-18*math.sin(a+s*.2))],fill=WHITE,width=width)

def footer(base,d,logo=True):
    xr=505; 
    hl(base,d,xr-28,H-92,'عنواننا',SB(34),pad=(8,2),skew=3)
    text(d,xr-28,H-92,'عنواننا',SB(34))
    text(d,xr-28,H-48,'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',SR(22))
    d.ellipse([xr-9,H-118,xr+3,H-106],fill=(70,150,140)); d.line([xr-3,H-106,xr-3,H-58],fill=(200,200,195),width=2)
    if not logo: return
    lg=Image.open(S+'logo.png'); s=118/lg.width; lg=lg.resize((118,round(lg.height*s)),Image.LANCZOS)
    base.alpha_composite(lg,(W-60-118,H-48-lg.height))

def place(im,scale=.82,cx=.5,bottom=0):
    """shrink photo onto canvas, fill background with blurred, darkened version"""
    bg=cover(im,.5,.5,1.25).filter(ImageFilter.GaussianBlur(40))
    s=max(W/im.width,H/im.height)*scale; fg=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=int(W*cx-fg.width/2); y=H-fg.height+bottom
    m=Image.new('L',fg.size,0); md=ImageDraw.Draw(m); e=90
    md.rectangle([e,e,fg.width-e,fg.height-e],fill=255); m=m.filter(ImageFilter.GaussianBlur(50))
    bg.paste(fg,(x,y),m); return bg

def shadow_text(base,items,blur=10,alpha=170):
    """items: list of (x,y,text,font); soft dark shadow behind for readability"""
    lay=Image.new('L',base.size,0); d=ImageDraw.Draw(lay)
    for x,y,t,f in items: d.text((x,y+3),t,font=f,fill=255,direction='rtl',anchor='rs',stroke_width=6,stroke_fill=255)
    lay=lay.filter(ImageFilter.GaussianBlur(blur)).point(lambda v:v*alpha//255)
    base.alpha_composite(Image.merge('RGBA',(*Image.new('RGB',base.size,(0,0,0)).split(),lay)))

def headline(img,XR,y1,l1,l2a,l2b,f,gap=104):
    """two-line headline; l2b gets the teal block. returns draw"""
    d=ImageDraw.Draw(img); wa=tw(d,l2a,f) if l2a else 0
    shadow_text(img,[(XR,y1,l1,f),(XR,y1+gap,l2a+l2b,f)])
    d=ImageDraw.Draw(img)
    hl(img,d,XR-wa,y1+gap,l2b,f,pad=(16,4),skew=8); d=ImageDraw.Draw(img)
    text(d,XR,y1,l1,f)
    if l2a: text(d,XR,y1+gap,l2a,f)
    text(d,XR-wa,y1+gap,l2b,f); return d

def label(img,lx,ly,bold,sub,arrow_pts):
    d=ImageDraw.Draw(img)
    shadow_text(img,[(lx,ly,bold,SB(40)),(lx,ly+42,sub,SR(30))],blur=8,alpha=150) if sub else shadow_text(img,[(lx,ly,bold,SB(40))],blur=8,alpha=150)
    d=ImageDraw.Draw(img)
    hl(img,d,lx,ly,bold,SB(40),pad=(8,2),skew=3); d=ImageDraw.Draw(img)
    text(d,lx,ly,bold,SB(40))
    if sub: text(d,lx,ly+42,sub,SR(30))
    arrow(img,arrow_pts)

def logo_br(img,size=118):
    lg=Image.open(S+'logo.png'); lg=lg.resize((size,round(lg.height*size/lg.width)),Image.LANCZOS)
    img.alpha_composite(lg,(W-60-size,H-48-lg.height))
