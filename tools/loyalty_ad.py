src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pvary.py').read()
exec(src[:src.index('P=[]')])
import math
O=S+'out/loyal/'; os.makedirs(O,exist_ok=True)
GOLD=(216,190,128); CREAM=(244,238,226)
def R(d,x,y,t,f,fill=WHITE,anchor='rs'): d.text((x,y),t,font=f,fill=fill,direction='rtl',anchor=anchor)
def cup(d,cx,cy,r,filled):
    col=CREAM if filled else (120,170,162)
    if filled: d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(40,128,118,255),outline=(120,190,180),width=2)
    w=r*1.0; h=r*0.75
    d.rounded_rectangle([cx-w/2,cy-h/2+4,cx+w/2-6,cy+h/2+4],radius=8,fill=col if filled else None,outline=col,width=4)
    d.arc([cx+w/2-18,cy-h/4+2,cx+w/2+8,cy+h/4+8],-90,90,fill=col,width=4)
    d.line([(cx-w/2-6,cy+h/2+12),(cx+w/2,cy+h/2+12)],fill=col,width=4)
def card(W0=900,stamps=7,total=10):
    H0=int(W0*0.63); s=4; c=Image.new('RGBA',(W0,H0),(0,0,0,0)); d=ImageDraw.Draw(c)
    m=Image.new('L',(W0,H0),0); ImageDraw.Draw(m).rounded_rectangle([0,0,W0-1,H0-1],radius=40,fill=255)
    g=Image.new('RGBA',(W0,H0)); gd=ImageDraw.Draw(g)
    for y in range(H0):
        t=y/H0; gd.line([(0,y),(W0,y)],fill=(int(47-20*t),int(112-40*t),int(104-38*t),255))
    gl=Image.new('RGBA',(W0,H0),(0,0,0,0)); ImageDraw.Draw(gl).ellipse([-W0*.3,-H0*.9,W0*.9,H0*.45],fill=(255,255,255,26))
    g.alpha_composite(gl); c.paste(g,(0,0),m); d=ImageDraw.Draw(c)
    d.rounded_rectangle([12,12,W0-13,H0-13],radius=32,outline=GOLD+(150,),width=2)
    lg=Image.open(S+'logo_white.png').convert('RGBA'); lg=lg.resize((120,round(lg.height*120/lg.width)),Image.LANCZOS); c.alpha_composite(lg,(W0-160,34))
    R(d,W0-180,90,'بطاقة الولاء',SB(40),CREAM); R(d,W0-180,134,'NUSS CLUB',SB(24),GOLD)
    cols=5; gap=(W0-140)/cols
    for k in range(total):
        r_,cc=divmod(k,cols); cx=W0-90-cc*gap; cy=250+r_*120
        if k==total-1:
            d.ellipse([cx-44,cy-44,cx+44,cy+44],outline=GOLD,width=4); d.polygon([(cx+26*math.cos(math.pi/2+k2*math.pi/5)*(1 if k2%2==0 else .42),cy-26*math.sin(math.pi/2+k2*math.pi/5)*(1 if k2%2==0 else .42)) for k2 in range(10)],fill=GOLD)
        else: cup(d,cx,cy,44,k<stamps)
    R(d,W0-50,H0-56,'معالي الزبون',SR(24),(190,215,210)); R(d,W0-50,H0-22,'ضيفنا العزيز',SB(32),CREAM)
    d.text((50,H0-26),'NUSS-2026-0007',font=SB(26),fill=(190,215,210),anchor='ls')
    return c
def place_card(base,cx,cy,w,rot):
    c=card(w); c=c.rotate(rot,expand=True,resample=Image.BICUBIC)
    sh=Image.new('RGBA',base.size,(0,0,0,0)); a=c.getchannel('A').point(lambda v:int(v*.65)); blk=Image.new('RGBA',c.size,(0,0,0,255)); blk.putalpha(a)
    sh.alpha_composite(blk,(int(cx-c.width/2+18),int(cy-c.height/2+34))); base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    base.alpha_composite(c,(int(cx-c.width/2),int(cy-c.height/2)))
# --- post 4:5
im=prep(71,640,200)
place_card(im,560,900,800,-7); CUR[0]=im.copy()
head(im,'جديد: بطاقة الولاء','كل طلب بختـــم...','والقهوة علينـــا')
mlabel(im,1010,600,'بطاقتك','على محفظة جوالك',[(880,640),(840,680),(800,720)])
footer_c(im); im.convert('RGB').save(O+'loyalty_post.jpg',quality=95)
# --- story 9:16
VW,VH=1080,1920
base=Image.open(S+'real/r71.png').convert('RGB'); s=max(VW/base.width,VH/base.height); base=base.resize((round(base.width*s),round(base.height*s)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,90,2))
x=(base.width-VW)//2; st=base.crop((x,0,x+VW,VH)).convert('RGBA')
ov=Image.new('RGBA',(VW,VH),(0,0,0,0)); d=ImageDraw.Draw(ov)
for y in range(VH):
    t=abs(y-VH*0.55)/(VH*0.55); d.line([(0,y),(VW,y)],fill=(8,12,11,int(120+100*min(1,t))))
st.alpha_composite(ov); d=ImageDraw.Draw(st)
pt='جديد: بطاقة الولاء'; fp=SB(34); w=tw(d,pt,fp); d.rounded_rectangle([1010-w-48,150,1010,214],radius=32,fill=TEAL); R(d,986,195,pt,fp)
R(d,1010,360,'كل طلب بختـــم...',DB(84))
f2=DB(104); hl(st,d,1010,500,'والقهوة علينـــا',f2,pad=(18,5),skew=9); d=ImageDraw.Draw(st); R(d,1010,500,'والقهوة علينـــا',f2)
place_card(st,540,880,880,-6); d=ImageDraw.Draw(st)
steps=[('1','صوّر QR الطاولة أو افتح المنيو'),('2','حط رقم جوالك وطلّع البطاقة ببلاش'),('3','ضيفها لـ Apple أو Google Wallet'),('4','كل طلب بختم… وكمّل الأختام والمكافأة إلك')]
y=1280
for n,t in steps:
    d.ellipse([952,y-46,1010,y+12],fill=TEAL); d.text((981,y-2),n,font=SB(36),fill=WHITE,anchor='ms'); R(d,930,y,t,SB(38),CREAM); y+=92
R(d,VW/2,1700,'ما بدها تطبيق • بتنحفظ بمحفظة جوالك',SR(32),(190,205,202),'ms')
lg=Image.open(S+'logo_white.png').convert('RGBA'); lg=lg.resize((120,round(lg.height*120/lg.width)),Image.LANCZOS); st.alpha_composite(lg,(VW//2-60,1745))
st.convert('RGB').save(O+'loyalty_story.jpg',quality=95)
sh=Image.new('RGB',(540+30+304,675),(30,30,30)); sh.paste(_open(O+'loyalty_post.jpg').resize((540,675)),(0,0)); sh.paste(_open(O+'loyalty_story.jpg').resize((380,675)).crop((0,0,304,675)) if False else _open(O+'loyalty_story.jpg').resize((304,540)),(570,60)); sh.save(O+'preview.jpg'); print('ok')
