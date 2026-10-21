exec(open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/post.py').read())
import os,math,random
random.seed(7)
SW,SH=1080,1920; CX=SW//2; BG=(12,20,19); MUT=(195,208,205); TL=(120,190,180); CREAM=(240,232,218)
O=S+'out/story_who2/'; os.makedirs(O,exist_ok=True)
def fit(im,w,h,cy=.5,zoom=1.0):
    s=max(w/im.width,h/im.height)*zoom; im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=(im.width-w)//2; y=int((im.height-h)*cy); return im.crop((x,y,x+w,y+h))
def grad(img,y0,y1,a0,a1):
    ov=Image.new('RGBA',(SW,SH),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(y0,y1):
        t=(y-y0)/max(1,y1-y0); d.line([(0,y),(SW,y)],fill=BG+(int(a0+(a1-a0)*t),))
    img.alpha_composite(ov)
def C(d,y,t,f,fill=WHITE): d.text((CX,y),t,font=f,fill=fill,direction='rtl',anchor='ms')
def W(d,t,f): return tw(d,t,f)
def HLC(img,y,t,f,skew=9):
    d=ImageDraw.Draw(img); w=W(d,t,f); xr=CX+w/2
    hl(img,d,xr,y,t,f,pad=(22,6),skew=skew); d=ImageDraw.Draw(img); d.text((xr,y),t,font=f,fill=WHITE,direction='rtl',anchor='rs')
def progress(img,i,n=4):
    d=ImageDraw.Draw(img); gap=10; w=(SW-120-gap*(n-1))/n
    for k in range(n):
        x=60+k*(w+gap); d.rounded_rectangle([x,40,x+w,48],radius=4,fill=(255,255,255,235) if k<=i else (255,255,255,80))
def pillC(img,y,t,f=None,fill=TEAL,fg=WHITE):
    d=ImageDraw.Draw(img); f=f or SB(32); w=W(d,t,f)
    d.rounded_rectangle([CX-w/2-30,y,CX+w/2+30,y+60],radius=30,fill=fill); d.text((CX,y+43),t,font=f,fill=fg,direction='rtl',anchor='ms')
def sparkle(img,x,y,r,col=CREAM,rot=0):
    d=ImageDraw.Draw(img); pts=[]
    for k in range(8):
        a=rot+k*math.pi/4; rr=r if k%2==0 else r*.28
        pts.append((x+rr*math.cos(a),y+rr*math.sin(a)))
    d.polygon(pts,fill=col)
def curve(pts,n=24):
    P=[pts[0]]+pts+[pts[-1]]; out=[]
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        for k in range(n):
            t=k/n; t2,t3=t*t,t*t*t
            out.append(tuple(.5*((2*p1[j])+(-p0[j]+p2[j])*t+(2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2+(-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3) for j in (0,1)))
    out.append(pts[-1]); return out
def arrow(img,pts,col=CREAM,w=6):
    d=ImageDraw.Draw(img); c=curve(pts); d.line(c,fill=col,width=w,joint='curve')
    (ax,ay),(bx,by)=c[-5],c[-1]; a=math.atan2(by-ay,bx-ax)
    for s in (.55,-.55): d.line([(bx,by),(bx-30*math.cos(a+s),by-30*math.sin(a+s))],fill=col,width=w)
def scribble(img,box,col=CREAM,w=6,loops=1.15):
    d=ImageDraw.Draw(img); x0,y0,x1,y1=box; cx,cy=(x0+x1)/2,(y0+y1)/2; rx,ry=(x1-x0)/2,(y1-y0)/2; pts=[]
    N=90
    for k in range(int(N*loops)+1):
        a=-math.pi/2+2*math.pi*k/N; j=1+0.04*math.sin(k*.7)+0.03*(k/N)
        pts.append((cx+rx*j*math.cos(a),cy+ry*j*math.sin(a)))
    d.line(pts,fill=col,width=w,joint='curve')
def sticker(img,cx,cy,t,f,rot=-8,fill=CREAM,fg=BG):
    tmp=Image.new('RGBA',(10,10)); dd=ImageDraw.Draw(tmp); w=W(dd,t,f); h=f.size*1.5
    lay=Image.new('RGBA',(int(w+70),int(h+30)),(0,0,0,0)); d=ImageDraw.Draw(lay)
    d.rounded_rectangle([6,6,lay.width-6,lay.height-6],radius=22,fill=fill)
    d.text((lay.width/2,lay.height/2+f.size*.32),t,font=f,fill=fg,direction='rtl',anchor='ms')
    lay=lay.rotate(rot,expand=True,resample=Image.BICUBIC); img.alpha_composite(lay,(int(cx-lay.width/2),int(cy-lay.height/2)))
def footer(img,y=1790):
    d=ImageDraw.Draw(img); lg=Image.open(S+'logo.png').convert('RGBA'); lw=96; lg=lg.resize((lw,round(lg.height*lw/lg.width)),Image.LANCZOS)
    t='تقاطع شارع ملعب فلسطين، مع شارع التايلاندي'; f=SR(26); w=W(d,t,f); tot=lw+22+w; x=CX-tot/2
    img.alpha_composite(lg,(int(x),int(y-lg.height/2))); d.text((x+lw+22+w,y+9),t,font=f,fill=MUT,direction='rtl',anchor='rs')
g1=Image.open(S+'who2/g01.png').convert('RGB'); g2=Image.open(S+'who2/g02.png').convert('RGB'); g5=Image.open(S+'who2/g05.png').convert('RGB')
def base(src,cy=.5,zoom=1.0):
    im=Image.new('RGBA',(SW,SH),BG+(255,)); im.paste(fit(src,SW,SH,cy,zoom),(0,0))
    grad(im,0,760,235,0); grad(im,1350,SH,0,245); return im
# ---- 1 HOOK
im=base(g1,.5,1.05); progress(im,0)
pillC(im,120,'كويز الشتا')
d=ImageDraw.Draw(im); C(d,345,'مين إنـــت',DB(150))
HLC(im,525,'بالشتـــا؟',DB(165))
sparkle(im,170,250,34); sparkle(im,930,420,22,TL,.4); sparkle(im,120,560,16,CREAM,.2)
scribble(im,(330,1120,720,1440))
arrow(im,[(860,700),(900,860),(830,1020),(720,1140)])
d=ImageDraw.Draw(im); C(d,1620,'اختار مشروبك... ومنقلّك مين إنت',SB(46)); 
pillC(im,1665,'اسحب  ‹',SB(30),fill=(255,255,255),fg=BG)
footer(im); im.convert('RGB').save(O+'s1.jpg',quality=95)
# ---- 2 POLL
im=Image.new('RGBA',(SW,SH),BG+(255,))
L=fit(g1,SW//2,SH,.6,1.0); Rr=fit(g2,SW//2,SH,.62,1.0); im.paste(L,(SW//2,0)); im.paste(Rr,(0,0))
grad(im,0,700,240,0); grad(im,1200,SH,0,250)
d=ImageDraw.Draw(im); d.line([(CX,690),(CX,1270)],fill=CREAM,width=4)
progress(im,1); pillC(im,120,'مين إنت بالشتا؟')
d=ImageDraw.Draw(im); C(d,330,'هوت شوكليـــت',DB(96)); 
d.ellipse([CX-58,372,CX+58,488],fill=CREAM); d.text((CX,452),'ولا',font=DB(48),fill=BG,direction='rtl',anchor='ms')
HLC(im,610,'لاتيه سخـــن؟',DB(104))
sparkle(im,140,420,26); sparkle(im,950,250,20,TL,.5)
# poll card
cx0,cy0,cx1,cy1=110,1290,970,1700
d=ImageDraw.Draw(im); d.rounded_rectangle([cx0,cy0,cx1,cy1],radius=40,fill=(250,247,240))
d.text((CX,cy0+80),'إنت مين فيهم؟',font=DB(54),fill=BG,direction='rtl',anchor='ms')
for k,(lab,sub) in enumerate([('البردان الدايم','هوت شوكليت'),('بيحب المطر','لاتيه سخن')]):
    y=cy0+130+k*125
    d.rounded_rectangle([cx0+40,y,cx1-40,y+100],radius=50,fill=(232,238,236))
    d.ellipse([cx1-130,y+12,cx1-54,y+88],fill=TEAL); d.text((cx1-92,y+66),str(k+1),font=SB(44),fill=WHITE,anchor='ms')
    d.text((cx1-160,y+66),lab,font=SB(44),fill=BG,direction='rtl',anchor='rs')
    d.text((cx0+80,y+64),sub,font=SR(32),fill=(90,110,106),direction='rtl',anchor='ls')
footer(im); im.convert('RGB').save(O+'s2.jpg',quality=95)
# ---- 3 NOT COLD
im=base(g5,.55,1.08); progress(im,2); pillC(im,120,'مين إنت بالشتا؟')
d=ImageDraw.Draw(im); C(d,330,'"أنا مش بـــردان"',DB(110))
HLC(im,500,'وهو بيرجـــف',DB(130))
sticker(im,850,690,'رسمي!',DB(54),rot=10)
sparkle(im,150,260,28); sparkle(im,960,420,18,TL,.3)
scribble(im,(330,980,760,1440),w=6)
arrow(im,[(210,760),(170,900),(240,1040),(360,1120)])
d=ImageDraw.Draw(im); C(d,1610,'إنت آيس أمريكانو... وإنت عارف حالك',SB(42))
pillC(im,1650,'@صاحبك_اللي_بيرجف',SB(32),fill=(255,255,255),fg=TEAL)
footer(im); im.convert('RGB').save(O+'s3.jpg',quality=95)
# ---- 4 CTA
im=base(g2,.5,1.0); ov=Image.new('RGBA',(SW,SH),BG+(90,)); im.alpha_composite(ov); progress(im,3)
pillC(im,120,'شو ما كنت')
d=ImageDraw.Draw(im); C(d,340,'مشروبـــك',DB(150)); HLC(im,520,'مستنّيـــك',DB(160))
sparkle(im,160,300,30); sparkle(im,930,560,22,TL,.4)
# info card
cx0,cy0,cx1,cy1=120,1260,960,1700
card=Image.new('RGBA',(SW,SH),(0,0,0,0)); dc=ImageDraw.Draw(card); dc.rounded_rectangle([cx0,cy0,cx1,cy1],radius=40,fill=BG+(225,),outline=TL+(255,),width=3); im.alpha_composite(card)
d=ImageDraw.Draw(im)
rows=[('السبت – الخميس','10 الصبح – 10 المسا'),('الجمعة','3 العصر – 10 المسا')]
for k,(a,b) in enumerate(rows):
    y=cy0+100+k*95
    # clock icon
    d.ellipse([cx1-110,y-42,cx1-60,y+8],outline=TL,width=5); d.line([(cx1-85,y-17),(cx1-85,y-32)],fill=TL,width=4); d.line([(cx1-85,y-17),(cx1-72,y-12)],fill=TL,width=4)
    d.text((cx1-130,y),a,font=SB(40),fill=WHITE,direction='rtl',anchor='rs'); d.text((cx0+50,y),b,font=SR(36),fill=MUT,direction='rtl',anchor='ls')
d.line([(cx0+50,cy0+250),(cx1-50,cy0+250)],fill=(60,90,86),width=2)
y=cy0+340
# pin icon
d.ellipse([cx1-108,y-60,cx1-62,y-14],fill=TEAL); d.polygon([(cx1-104,y-30),(cx1-66,y-30),(cx1-85,y+4)],fill=TEAL); d.ellipse([cx1-92,y-45,cx1-78,y-31],fill=BG)
d.text((cx1-130,y-12),'تقاطع شارع ملعب فلسطين',font=SB(38),fill=WHITE,direction='rtl',anchor='rs')
d.text((cx1-130,y+42),'مع شارع التايلاندي',font=SR(32),fill=MUT,direction='rtl',anchor='rs')
lg=Image.open(S+'logo.png').convert('RGBA'); lw=150; lg=lg.resize((lw,round(lg.height*lw/lg.width)),Image.LANCZOS); im.alpha_composite(lg,(CX-lw//2,1740))
im.convert('RGB').save(O+'s4.jpg',quality=95)
sh=Image.new('RGB',(4*360+30,640),(30,30,30))
for i in range(4): sh.paste(Image.open(O+f's{i+1}.jpg').resize((360,640)),(i*370,0))
sh.save(O+'preview.jpg'); print('ok')
