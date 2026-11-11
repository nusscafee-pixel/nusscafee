# Winter coffee posts: generated scene (ElevenLabs gemini-3.1-flash-image + Adobe generative expand) + brand overlay
import math
from PIL import Image,ImageDraw,ImageFont
S='/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/'; RP='/home/user/nusscafee/'
W,H=1080,1350; TEAL=(35,92,86); TEAL2=(47,112,104); WHITE=(246,243,236)
RQ=ImageFont.Layout.RAQM
def F(w,s): return ImageFont.truetype(S+f'fonts/thmanyahsans-{w}.otf',s,layout_engine=RQ)
def tw(d,t,f): b=d.textbbox((0,0),t,font=f,direction='rtl',anchor='rs'); return b[2]-b[0]
def R(d,x,y,t,f,fill=WHITE): d.text((x,y),t,font=f,fill=fill,direction='rtl',anchor='rs')
def grad(im,y0,y1,a0,a1,top=True):
    ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(y0,y1):
        t=(y-y0)/max(1,y1-y0); d.line([(0,y),(W,y)],fill=(6,10,10,int(a0+(a1-a0)*t)))
    im.alpha_composite(ov)
def block(im,xr,y,t,f,skew=8,pad=20):
    d=ImageDraw.Draw(im); b=d.textbbox((xr,y),t,font=f,direction='rtl',anchor='rs'); h=b[3]-b[1]
    x0,x1=b[0]-pad,b[2]+pad; y0=b[1]-h*.12; y1=b[3]+h*.2
    lay=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(lay).polygon([(x0,y0+skew),(x1,y0-skew/2),(x1,y1),(x0,y1+skew/2)],fill=TEAL2+(245,)); im.alpha_composite(lay)
    R(ImageDraw.Draw(im),xr,y,t,f)
def head(im,pill,l1,l2,XR=1010):
    d=ImageDraw.Draw(im); fp=F('Bold',30); w=tw(d,pill,fp)
    d.rounded_rectangle([XR-w-48,64,XR,112],radius=24,outline=WHITE,width=2); R(d,XR-24,99,pill,fp)
    f1=F('Bold',74); R(d,XR,214,l1,f1)
    f2=F('Black',86)
    while tw(d,l2,f2)>960: f2=F('Black',f2.size-4)
    block(im,XR-18,326,l2,f2)
def bez(p,n=40):
    (x0,y0),(x1,y1),(x2,y2),(x3,y3)=p; o=[]
    for i in range(n+1):
        t=i/n; u=1-t; o.append((u**3*x0+3*u*u*t*x1+3*u*t*t*x2+t**3*x3,u**3*y0+3*u*u*t*y1+3*u*t*t*y2+t**3*y3))
    return o
def arrow(im,p):
    d=ImageDraw.Draw(im); pts=bez(p); d.line(pts,fill=WHITE,width=5,joint='curve')
    (xa,ya),(xb,yb)=pts[-4],pts[-1]; a=math.atan2(yb-ya,xb-xa)
    for s in (2.5,-2.5):
        d.line([(xb,yb),(xb-30*math.cos(a+s/6*math.pi/2.2),yb-30*math.sin(a+s/6*math.pi/2.2))],fill=WHITE,width=5)
def label(im,xr,y,name,sub,p):
    block(im,xr,y,name,F('Black',48),skew=6,pad=16)
    R(ImageDraw.Draw(im),xr,y+52,sub,F('Medium',32)); arrow(im,p)
def footer(im):
    d=ImageDraw.Draw(im); x=70
    d.ellipse([x-9,1170-9,x+9,1170+9],fill=TEAL2); d.line([(x,1185),(x,1290)],fill=TEAL2,width=4)
    fa=F('Bold',32); w=tw(d,'عنواننا',fa); d.rectangle([x+22,1180,x+22+w+28,1228],fill=TEAL2); R(d,x+36+w,1216,'عنواننا',fa)
    fs=F('Medium',27); t='تقاطع شارع ملعب فلسطين، مع شارع التايلاندي'; R(d,x+22+tw(d,t,fs),1272,t,fs)
    lg=Image.open(RP+'brand/logo_official_white.png').convert('RGBA'); s=150/lg.width; lg=lg.resize((150,int(lg.height*s)),Image.LANCZOS)
    im.alpha_composite(lg,(W-60-150,H-50-lg.height))
def base(p):
    im=Image.open(p).convert('RGB').resize((W,H),Image.LANCZOS).convert('RGBA')
    grad(im,0,430,150,0); grad(im,1060,H,0,190); return im
O=RP+'posts/winter_coffee/'
# 1) cappuccino
im=base(S+'cw/capx.png'); head(im,'الشتا عنّا','إيديك بردانـــة؟','حطّهم على كابتشينـــو')
label(im,1010,640,'كابتشينو','بيدفّي الإيدين والقلب',[(830,700),(640,720),(470,780),(410,880)])
footer(im); im.convert('RGB').save(O+'C1_cappuccino.jpg',quality=95)
# 2) turkish coffee
im=base(S+'cw/turkx.png'); head(im,'الشتا عنّا','مطر، وكتـــاب...','وفنجان قهـــوة تركي')
label(im,1030,720,'قهوة تركي','على رواق… متل قعدة ستّك',[(870,790),(760,800),(640,850),(590,945)])
footer(im); im.convert('RGB').save(O+'C2_turkish.jpg',quality=95)
a=Image.open(O+'C1_cappuccino.jpg').resize((540,675)); b=Image.open(O+'C2_turkish.jpg').resize((540,675))
s=Image.new('RGB',(1090,675),(20,20,20)); s.paste(a,(0,0)); s.paste(b,(550,0)); s.save(O+'preview.jpg',quality=90); print('ok')
