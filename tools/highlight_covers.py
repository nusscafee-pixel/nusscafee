import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'post.py')).read())
import math
CW,CH=1080,1920; CX,CY=540,960
LW=20; WH=(245,243,238)
def base():
    im=Image.new('RGB',(CW,CH),(14,18,17))
    g=Image.new('L',(CW//4,CH//4),0); d=ImageDraw.Draw(g); d.ellipse([CX/4-150,CY/4-150,CX/4+150,CY/4+150],fill=255)
    g=g.filter(ImageFilter.GaussianBlur(60)).resize((CW,CH))
    im=Image.composite(Image.new('RGB',(CW,CH),(35,92,86)),im,g)
    n=Image.effect_noise((CW,CH),14).convert('RGB'); im=Image.blend(im,ImageChops.overlay(im,n),.12)
    d=ImageDraw.Draw(im)
    d.ellipse([CX-430,CY-430,CX+430,CY+430],outline=(90,150,142),width=4)
    return im
def arc(d,box,a0,a1,w=LW): d.arc(box,a0,a1,fill=WH,width=w)
def L(d,pts,w=LW): d.line(pts,fill=WH,width=w,joint='curve'); [d.ellipse([x-w/2,y-w/2,x+w/2,y+w/2],fill=WH) for x,y in (pts[0],pts[-1])]
def steam(d,x,y,h=110):
    pts=[(x+18*math.sin(t/12),y-t) for t in range(0,h,4)]; L(d,pts,14)
def ic_coffee(d):
    oy=40
    L(d,[(CX-170,CY-110+oy),(CX-140,CY+90+oy),(CX+110,CY+90+oy),(CX+140,CY-110+oy),(CX-170,CY-110+oy)])
    arc(d,[CX+90,CY-80+oy,CX+230,CY+40+oy],-90,90)
    L(d,[(CX-230,CY+140+oy),(CX+230,CY+140+oy)])
    for x in (CX-80,CX,CX+80): steam(d,x,CY-150+oy)
def ic_iced(d):
    L(d,[(CX-140,CY-230),(CX-105,CY+230),(CX+105,CY+230),(CX+140,CY-230)])
    L(d,[(CX-135,CY-120),(CX+135,CY-120)],10)
    for (x,y,a) in [(-60,-60,15),(40,-20,-10),(-30,70,5),(60,110,20)]:
        s=42; pts=[(CX+x+s*math.cos(math.radians(a+k*90+45)),CY+y+s*math.sin(math.radians(a+k*90+45))) for k in range(5)]
        L(d,pts,12)
    L(d,[(CX+40,CY-120),(CX+90,CY-300),(CX+170,CY-330)],16)
def ic_cake(d):
    p=[(CX-230,CY+150),(CX+230,CY+150),(CX+230,CY-40),(CX-230,CY+150)]
    L(d,[(CX-230,CY+150),(CX+230,CY+150),(CX+230,CY-60),(CX-230,CY+150)])
    L(d,[(CX-110,CY+100),(CX+230,CY+100)],12); L(d,[(CX+10,CY+50),(CX+230,CY+50)],12)
    L(d,[(CX-230,CY+150),(CX-230,CY+60),(CX+230,CY-140),(CX+230,CY-60)])
    d.ellipse([CX+120,CY-250,CX+200,CY-170],outline=WH,width=LW); L(d,[(CX+160,CY-250),(CX+190,CY-300)],12)
def ic_orange(d):
    r=200; d.ellipse([CX-r,CY-r+30,CX+r,CY+r+30],outline=WH,width=LW)
    r2=150
    for k in range(8):
        a=math.radians(k*45); L(d,[(CX,CY+30),(CX+r2*math.cos(a),CY+30+r2*math.sin(a))],10)
    d.ellipse([CX-r2,CY-r2+30,CX+r2,CY+r2+30],outline=WH,width=10)
    L(d,[(CX,CY-170),(CX+20,CY-230)],14); d.ellipse([CX+20,CY-280,CX+120,CY-220],outline=WH,width=12)
def ic_pin(d):
    r=150; cy=CY-60
    arc(d,[CX-r,cy-r,CX+r,cy+r],150,390)
    L(d,[(CX-r*math.cos(math.radians(30)),cy+r*math.sin(math.radians(30))),(CX,CY+250),(CX+r*math.cos(math.radians(30)),cy+r*math.sin(math.radians(30)))])
    d.ellipse([CX-55,cy-55,CX+55,cy+55],outline=WH,width=LW)
    d.ellipse([CX-170,CY+235,CX+170,CY+300],outline=WH,width=10)
def ic_star(d):
    R,r=230,95; pts=[]
    for k in range(11):
        rr=R if k%2==0 else r; a=math.radians(-90+k*36); pts.append((CX+rr*math.cos(a),CY+20+rr*math.sin(a)))
    L(d,pts)
C=[('qahwa','قهـــوة',ic_coffee),('bared','بـــارد',ic_iced),('helo','حلـــو',ic_cake),('fresh','فريـــش',ic_orange),('location','موقعنـــا',ic_pin),('reviews','آراءكـــم',ic_star)]
outs=[]
for key,name,fn in C:
    im=base(); d=ImageDraw.Draw(im); fn(d)
    f=DB(84); d.text((CX+tw(d,name,f)/2,CY+400),name,font=f,fill=WH,direction='rtl',anchor='rs') if False else None
    im.save(S+f'hl/highlight_{key}.jpg',quality=95); outs.append((name,im))
# preview: profile row of circles
pv=Image.new('RGB',(6*200+40,300),(250,250,250)); d=ImageDraw.Draw(pv)
for i,(name,im) in enumerate(outs):
    c=im.crop((CX-540,CY-540,CX+540,CY+540)).resize((160,160),Image.LANCZOS)
    m=Image.new('L',(160,160),0); ImageDraw.Draw(m).ellipse([0,0,159,159],fill=255)
    x=20+i*200+20; d.ellipse([x-6,24,x+166,196],outline=(200,200,200),width=2); pv.paste(c,(x,30),m)
    f=SR(28); n=name.replace('ـ',''); d.text((x+80+tw(d,n,f)/2,250),n,font=f,fill=(30,30,30),direction='rtl',anchor='rs')
pv.save(S+'hl/preview_profile.jpg',quality=95)
sh=Image.new('RGB',(6*270,480))
for i,(n,im) in enumerate(outs): sh.paste(im.resize((270,480)),(i*270,0))
sh.save(S+'hl/sheet.jpg'); print('ok')
