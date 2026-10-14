import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'post.py')).read())
import math
K=2  # supersample
CW,CH=1080*K,1920*K; CX,CY=CW//2,CH//2
T=(35,92,86); T2=(47,112,104); TL=(214,232,229); TLL=(236,244,242); DK=(24,38,36); WT=(255,255,255)
def P(x,y): return (CX+x*K, CY+y*K)
def poly(d,pts,fill): d.polygon([P(*p) for p in pts],fill=fill)
def rr(d,x0,y0,x1,y1,r,fill,outline=None,w=0): d.rounded_rectangle([*P(x0,y0),*P(x1,y1)],radius=r*K,fill=fill,outline=outline,width=w*K)
def el(d,x0,y0,x1,y1,fill=None,outline=None,w=0): d.ellipse([*P(x0,y0),*P(x1,y1)],fill=fill,outline=outline,width=w*K)
def ln(d,pts,col,w):
    pp=[P(*p) for p in pts]; d.line(pp,fill=col,width=w*K,joint='curve')
    for x,y in (pp[0],pp[-1]): d.ellipse([x-w*K/2,y-w*K/2,x+w*K/2,y+w*K/2],fill=col)
def blob(d,seed):
    import random; rnd=random.Random(seed); pts=[]
    for k in range(120):
        a=2*math.pi*k/120; r=330+22*math.sin(3*a+seed)+16*math.cos(5*a+seed*2)
        pts.append((r*math.cos(a),r*math.sin(a)))
    poly(d,pts,TLL)
def sparkle(d,x,y,s):
    poly(d,[(x,y-s),(x+s*.22,y-s*.22),(x+s,y),(x+s*.22,y+s*.22),(x,y+s),(x-s*.22,y+s*.22),(x-s,y),(x-s*.22,y-s*.22)],T2)
def ic_coffee(d):
    rr(d,-230,150,230,185,18,TL)
    poly(d,[(-175,-90),(150,-90),(120,140),(-145,140)],T)
    el(d,95,-60,225,70,outline=T,w=34)
    poly(d,[(-175,-90),(150,-90),(146,-60),(-171,-60)],T2)
    rr(d,-120,-50,-80,90,20,(70,135,127))
    for x in (-90,0,90): ln(d,[(x+18*math.sin(t/14),-130-t) for t in range(0,120,6)],DK,16)
    sparkle(d,200,-230,34)
def ic_iced(d):
    poly(d,[(-150,-230),(150,-230),(115,240),(-115,240)],TL)
    poly(d,[(-138,-60),(138,-60),(115,240),(-115,240)],T)
    for (x,y,a) in [(-55,-10,15),(45,30,-12),(-25,120,8)]:
        s=46; pts=[(x+s*math.cos(math.radians(a+k*90+45)),y+s*math.sin(math.radians(a+k*90+45))) for k in range(4)]; poly(d,pts,(120,170,163))
    ln(d,[(-150,-230),(-115,240),(115,240),(150,-230)],DK,14)
    ln(d,[(40,-60),(85,-300),(165,-330)],DK,18)
    sparkle(d,-215,-160,30)
def ic_cake(d):
    poly(d,[(-240,170),(240,170),(240,-70)],T)
    poly(d,[(-240,170),(-240,90),(240,-150),(240,-70)],TL)
    poly(d,[(-160,170),(240,170),(240,110),(-40,110)],T2)
    poly(d,[(-240,90),(240,-150),(240,-120),(-240,120)],WT)
    el(d,140,-260,220,-180,fill=(150,30,40)); ln(d,[(180,-255),(210,-305)],DK,12)
    sparkle(d,-200,-130,32)
def ic_orange(d):
    el(d,-210,-170,210,250,fill=T)
    el(d,-160,-120,160,200,fill=TL)
    for k in range(8):
        a=math.radians(k*45+22.5); ln(d,[(0,40),(150*math.cos(a),40+150*math.sin(a))],T,12)
    el(d,-24,16,24,64,fill=T)
    ln(d,[(0,-170),(15,-230)],DK,14); poly(d,[(15,-225),(120,-280),(150,-240),(60,-210)],T2)
    sparkle(d,215,-170,32)
def ic_pin(d):
    el(d,-180,250,180,310,fill=TL)
    r=165; cy=-60
    el(d,-r,cy-r,r,cy+r,fill=T); poly(d,[(-r*0.86,cy+r*0.5),(0,265),(r*0.86,cy+r*0.5)],T)
    el(d,-62,cy-62,62,cy+62,fill=WT)
    sparkle(d,205,-220,32)
def ic_star(d):
    R,r=245,105; pts=[]
    for k in range(10):
        rr_=R if k%2==0 else r; a=math.radians(-90+k*36); pts.append((rr_*math.cos(a),25+rr_*math.sin(a)))
    poly(d,pts,T)
    pts2=[(x*0.55-40,y*0.55-25) for x,y in pts]; poly(d,pts2,T2)
    sparkle(d,215,-200,34); sparkle(d,-230,180,22)
C=[('qahwa','قهوة',ic_coffee,1),('bared','بارد',ic_iced,2),('helo','حلو',ic_cake,3),('fresh','فريش',ic_orange,4),('location','موقعنا',ic_pin,5),('reviews','آراءكم',ic_star,6)]
outs=[]
for key,name,fn,sd in C:
    im=Image.new('RGB',(CW,CH),WT); d=ImageDraw.Draw(im); blob(d,sd); fn(d)
    im=im.resize((1080,1920),Image.LANCZOS)
    im.save(S+f'hl2/highlight_{key}.jpg',quality=95); outs.append((name,im))
pv=Image.new('RGB',(6*200+40,300),(255,255,255)); d=ImageDraw.Draw(pv)
for i,(name,im) in enumerate(outs):
    c=im.crop((0,420,1080,1500)).resize((160,160),Image.LANCZOS)
    m=Image.new('L',(160,160),0); ImageDraw.Draw(m).ellipse([0,0,159,159],fill=255)
    x=40+i*200; d.ellipse([x-6,24,x+166,196],outline=(219,219,219),width=2); pv.paste(c,(x,30),m)
    f=SR(28); d.text((x+80+tw(d,name,f)/2,250),name,font=f,fill=(30,30,30),direction='rtl',anchor='rs')
pv.save(S+'hl2/preview_profile.jpg',quality=95); print('ok')
