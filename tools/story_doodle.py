src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pstory_who2.py').read()
exec(src[:src.index('g1=Image.open')])
O=S+'out/doodle/'; os.makedirs(O,exist_ok=True)
INK=CREAM; LW=7
def wob(pts,amp=2.5):
    return [(x+random.uniform(-amp,amp),y+random.uniform(-amp,amp)) for x,y in pts]
def line(img,pts,col=INK,w=LW,smooth=True):
    d=ImageDraw.Draw(img); c=curve(pts) if smooth else pts; d.line(c,fill=col,width=w,joint='curve')
def arrowto(img,pts,col=INK,w=LW): arrow(img,pts,col,w)
def battery(img,x,y,w,h,level,fillc):
    d=ImageDraw.Draw(img); d.rounded_rectangle([x,y,x+w,y+h],radius=14,outline=INK,width=LW)
    d.rounded_rectangle([x+w,y+h*.3,x+w+16,y+h*.7],radius=5,fill=INK)
    n=4; gap=8; bw=(w-2*16-gap*(n-1))/n
    for k in range(level): bx=x+16+k*(bw+gap); d.rounded_rectangle([bx,y+16,bx+bw,y+h-16],radius=5,fill=fillc)
def bolt(img,x,y,s,col=INK,rot=0):
    P=[(0,-1),(.45,-1),(.15,-.1),(.55,-.1),(-.2,1.1),(.05,.15),(-.35,.15)]
    ca,sa=math.cos(rot),math.sin(rot)
    ImageDraw.Draw(img).polygon([(x+s*(px*ca-py*sa),y+s*(px*sa+py*ca)) for px,py in P],fill=col)
def heart(img,x,y,s,col,rot=0):
    pts=[]
    for k in range(60):
        t=2*math.pi*k/60; hx=16*math.sin(t)**3; hy=-(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))
        px,py=hx*s/16,hy*s/16; ca,sa=math.cos(rot),math.sin(rot); pts.append((x+px*ca-py*sa,y+px*sa+py*ca))
    ImageDraw.Draw(img).polygon(pts,fill=col)
def bubble(img,x,y,t,f,tail='left'):
    d=ImageDraw.Draw(img); w=W(d,t,f); h=f.size*1.45; x0,y0,x1,y1=x-w/2-34,y-h/2,x+w/2+34,y+h/2
    d.rounded_rectangle([x0,y0,x1,y1],radius=h/2,fill=INK)
    tx=x0+40 if tail=='left' else x1-40; d.polygon([(tx-12,y1-4),(tx+22,y1-4),(tx-20,y1+34)] if tail=='left' else [(tx+12,y1-4),(tx-22,y1-4),(tx+20,y1+34)],fill=INK)
    d.text((x,y+f.size*.33),t,font=f,fill=BG,direction='rtl',anchor='ms')
def label(img,x,y,t,f=None,anchor='rs'):
    f=f or SB(40); ImageDraw.Draw(img).text((x,y),t,font=f,fill=INK,direction='rtl',anchor=anchor)
def zz(img,x,y):
    d=ImageDraw.Draw(img)
    for k,s in enumerate([34,46,60]): d.text((x+k*42,y-k*52),'z',font=SB(s),fill=INK)
def head(img,i,pill,l1,l2,f1=120,f2=135):
    progress(img,i,3); pillC(img,120,pill); d=ImageDraw.Draw(img); C(d,320,l1,DB(f1)); HLC(img,490,l2,DB(f2))
def bottom(img,t,cta):
    d=ImageDraw.Draw(img); C(d,1640,t,SB(44)); pillC(img,1680,cta,SB(32),fill=(255,255,255),fg=TEAL); footer(img,1815)
def base2(p,cy=.5,dy=0):
    im=Image.new('RGBA',(SW,SH),BG+(255,)); im.paste(fit(Image.open(S+p).convert('RGB'),SW,SH,cy),(0,dy))
    grad(im,0,720,240,0); grad(im,1420,SH,0,248); return im
# 1 ENERGY
im=base2('g20/g20.png'); head(im,0,'مزاجك اليوم؟','الدوام طويـــل؟','اشحن حالـــك')
battery(im,70,760,190,95,1,(222,96,80)); label(im,262,900,'قبل',SB(36),'ms')
zz(im,90,720)
line(im,wob([(280,810),(420,770),(560,820),(700,900)]))
arrowto(im,[(700,900),(780,960),(800,1020)])
battery(im,790,1040,190,95,4,TL); label(im,885,1185,'بعد',SB(36),'ms')
bolt(im,385,990,52,INK,-.25); bolt(im,710,1250,44,INK,.3); bolt(im,690,1500,34,TL,.15)
bottom(im,'من بطارية فاضية... لفُل بشفطة','جرّب اشحن حالك عنّا')
im.convert('RGB').save(O+'d1.jpg',quality=95)
# 2 DESSERT
im=base2('g20/g14.png'); head(im,1,'مزاجك اليوم؟','قطعة وحـــدة؟','ما بتكفّـــي')
for (x,y,s,c,r) in [(330,960,40,(222,96,80),-.3),(450,880,28,INK,.2),(820,980,34,(222,96,80),.35),(900,860,22,INK,-.2)]: heart(im,x,y,s,c,r)
bubble(im,800,760,'يمّ!',DB(64),tail='left')
label(im,250,1110,'الكرزة إلي',SB(40),'ms')
arrowto(im,[(250,1130),(330,1200),(470,1210),(560,1195)])
for k in range(3):
    line(im,wob([(920+k*28,1250+k*18),(990+k*28,1235+k*18)],1.5),w=6,smooth=False)
bottom(im,'تاغ اللي ما بيقاسمك حلوه','مين بيقاسمك؟')
im.convert('RGB').save(O+'d2.jpg',quality=95)
# 3 LATTE
im=base2('g20/g11.png',dy=-170); head(im,2,'مزاجك اليوم؟','شو بصيـــر','جوّا كاستـــك؟')
label(im,300,1060,'إسبريسو',SB(42),'rs'); arrowto(im,[(310,1045),(400,1030),(470,1000),(520,960)])
label(im,300,1250,'ثلج',SB(42),'rs'); arrowto(im,[(310,1235),(380,1225),(440,1200)])
label(im,300,1430,'حليب بارد',SB(42),'rs'); arrowto(im,[(310,1415),(370,1412),(425,1395)])
for k,(a,b) in enumerate([(-.9,-.2),(-.75,-.05)]):
    r=80+k*36; cx,cy=560,730; pts=[(cx+r*math.cos(a+(b-a)*t/10),cy+r*math.sin(a+(b-a)*t/10)) for t in range(11)]
    line(im,pts,w=6)
bracket_x=780
line(im,wob([(bracket_x,930),(bracket_x+30,940),(bracket_x+30,1210),(bracket_x+55,1230),(bracket_x+30,1250),(bracket_x+30,1520),(bracket_x,1530)],1.2),w=6,smooth=False)
label(im,1040,1240,'بالترتيب',SB(38),'rs'); label(im,1040,1290,'الصح',SB(38),'rs')
bottom(im,'آيس لاتيه... كل طبقة إلها دور','جرّبه اليوم')
im.convert('RGB').save(O+'d3.jpg',quality=95)
sh=Image.new('RGB',(3*360+20,640),(30,30,30))
for i in range(3): sh.paste(Image.open(O+f'd{i+1}.jpg').resize((360,640)),(i*370,0))
sh.save(O+'preview.jpg'); print('ok')
