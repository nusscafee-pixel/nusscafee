src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pdoodle.py').read()
exec(src[:src.index('# 1 ENERGY')])
SW,SH=1080,1350; O=S+'out/mood_posts/'; os.makedirs(O,exist_ok=True); random.seed(3)
def pbase(p,dy=0):
    im=Image.new('RGBA',(SW,SH),BG+(255,)); im.paste(fit(Image.open(S+p).convert('RGB'),SW,SH),(0,dy))
    grad(im,0,560,235,0); grad(im,1120,SH,0,240); return im
def phead(img,l1,l2,pill='مزاجك اليوم؟'):
    pillC(img,50,pill,SB(30)); d=ImageDraw.Draw(img); C(d,205,l1,DB(92)); HLC(img,335,l2,DB(104))
def pfoot(img): footer(img,1295)
def dashed(img,pts,col=INK,w=6,dash=16,gap=14):
    c=curve(pts,40); d=ImageDraw.Draw(img); acc=0; on=True; seg=[c[0]]
    for a,b in zip(c,c[1:]):
        L=math.dist(a,b); acc+=L; seg.append(b)
        if acc>=(dash if on else gap):
            if on: d.line(seg,fill=col,width=w)
            on=not on; acc=0; seg=[b]
    (ax,ay),(bx,by)=c[-4],c[-1]; a=math.atan2(by-ay,bx-ax)
    for s in (.55,-.55): d.line([(bx,by),(bx-26*math.cos(a+s),by-26*math.sin(a+s))],fill=col,width=w)
def bulb(img,x,y,r=46):
    d=ImageDraw.Draw(img); d.ellipse([x-r,y-r,x+r,y+r],outline=INK,width=LW)
    d.rectangle([x-r*.42,y+r*.85,x+r*.42,y+r*1.35],outline=INK,width=LW); d.line([(x-r*.42,y+r*1.1),(x+r*.42,y+r*1.1)],fill=INK,width=5)
    d.line([(x-14,y+18),(x-6,y-10),(x+6,y+8),(x+14,y-14)],fill=(250,210,110),width=6)
    for k in range(7):
        a=-math.pi+k*math.pi/6; d.line([(x+(r+16)*math.cos(a),y+(r+16)*math.sin(a)),(x+(r+40)*math.cos(a),y+(r+40)*math.sin(a))],fill=INK,width=6)
def corners(img,box,L=60,w=8):
    d=ImageDraw.Draw(img); x0,y0,x1,y1=box
    for (x,y,sx,sy) in [(x0,y0,1,1),(x1,y0,-1,1),(x0,y1,1,-1),(x1,y1,-1,-1)]:
        d.line([(x,y+sy*L),(x,y),(x+sx*L,y)],fill=INK,width=w,joint='curve')
def burst(img,x,y,r0=40,r1=90,n=10,col=INK):
    d=ImageDraw.Draw(img)
    for k in range(n):
        a=2*math.pi*k/n+.15; rr=r1 if k%2==0 else r1*.75
        d.line([(x+r0*math.cos(a),y+r0*math.sin(a)),(x+rr*math.cos(a),y+rr*math.sin(a))],fill=col,width=6)
def sunface(img,x,y,r=58):
    d=ImageDraw.Draw(img); d.ellipse([x-r,y-r,x+r,y+r],outline=(250,210,110),width=LW)
    for k in range(10):
        a=2*math.pi*k/10; d.line([(x+(r+14)*math.cos(a),y+(r+14)*math.sin(a)),(x+(r+38)*math.cos(a),y+(r+38)*math.sin(a))],fill=(250,210,110),width=6)
    d.ellipse([x-22,y-16,x-10,y-4],fill=INK); d.ellipse([x+10,y-16,x+22,y-4],fill=INK)
    d.arc([x-26,y-14,x+26,y+28],20,160,fill=INK,width=6)
def plane(img,x,y,s=1.0,rot=-.5):
    P=[(0,-38),(8,-10),(48,8),(48,18),(8,8),(6,34),(18,44),(18,50),(0,44),(-18,50),(-18,44),(-6,34),(-8,8),(-48,18),(-48,8),(-8,-10)]
    ca,sa=math.cos(rot),math.sin(rot); ImageDraw.Draw(img).polygon([(x+s*(px*ca-py*sa),y+s*(px*sa+py*ca)) for px,py in P],fill=INK)
def pin(img,x,y,r=30,col=TEAL):
    d=ImageDraw.Draw(img); d.ellipse([x-r,y-r*2.2,x+r,y-r*.2],fill=col); d.polygon([(x-r*.9,y-r*.9),(x+r*.9,y-r*.9),(x,y+6)],fill=col); d.ellipse([x-r*.38,y-r*1.58,x+r*.38,y-r*.82],fill=INK)
def crown(img,x,y,w=120,col=(250,210,110)):
    h=w*.6; P=[(x-w/2,y),(x-w/2,y-h*.7),(x-w/4,y-h*.35),(x,y-h),(x+w/4,y-h*.35),(x+w/2,y-h*.7),(x+w/2,y)]
    d=ImageDraw.Draw(img); d.line(P+[P[0]],fill=col,width=LW,joint='curve')
    for px,py in [(x-w/2,y-h*.7),(x,y-h),(x+w/2,y-h*.7)]: d.ellipse([px-8,py-8,px+8,py+8],fill=col)
def emph(img,x,y,ang,n=3):
    d=ImageDraw.Draw(img)
    for k in range(n):
        a=ang+(k-1)*.45; d.line([(x+20*math.cos(a),y+20*math.sin(a)),(x+60*math.cos(a),y+60*math.sin(a))],fill=INK,width=6)
P=[]
# 1 pistachio study
im=pbase('g20/g06.png'); phead(im,'دراسة طويلـــة؟','بستاشيو بيفتح المخ')
bulb(im,250,560); arrow(im,[(300,640),(350,700),(400,720)])
d=ImageDraw.Draw(im); d.ellipse([110,1080,250,1200],outline=INK,width=6); d.text((180,1160),'A+',font=SB(56),fill=INK,anchor='ms')
emph(im,690,560,-1.2)
pfoot(im); im.convert('RGB').save(O+'m1.jpg',quality=95); P.append(('m1','دراسة طويلة؟ البستاشيو بيفتح المخ 💡📚','#بستاشيو'))
# 2 camera
im=pbase('g20/g07.png'); phead(im,'صوّرهـــا...','قبل ما تخلـــص')
corners(im,(445,640,740,1150)); burst(im,340,860,70,120)
bubble(im,200,640,'كليك!',DB(54),tail='right')
pfoot(im); im.convert('RGB').save(O+'m2.jpg',quality=95); P.append(('m2','صوّرها قبل ما تخلص 📸','#لوتس'))
# 3 banana
im=pbase('g20/g08.png'); phead(im,'صباحك أحلـــى','بالموز والحليـــب')
sunface(im,900,640)
arrow(im,[(330,820),(380,900),(430,920)])
label(im,330,1000,'من الشجرة',SB(38),'ms'); label(im,330,1045,'لكاستك',SB(38),'ms')
pfoot(im); im.convert('RGB').save(O+'m3.jpg',quality=95); P.append(('m3','صباحك أحلى بالموز والحليب 🍌☀️','#سموذي_موز'))
# 4 spain
im=pbase('gen10/d04.png'); phead(im,'مش لازم تسافـــر','إسبانيا عنّـــا')
dashed(im,[(900,520),(820,600),(760,620),(640,680),(560,760)])
plane(im,930,500,1.15,-.9)
pin(im,520,770); label(im,250,1110,'سان سيباستيان',SB(40),'ms')
arrow(im,[(250,1080),(300,1020),(380,960)])
pfoot(im); im.convert('RGB').save(O+'m4.jpg',quality=95); P.append(('m4','وفّر حق التذكرة… سان سيباستيان عنّا ✈️','#سان_سيباستيان'))
# 5 chess
im=pbase('gen10/d05.png'); phead(im,'كش ملـــك...','وما في هـــروب')
dashed(im,[(800,600),(700,560),(580,620),(500,760)])
crown(im,440,800,130)
emph(im,560,1000,1.6)
pfoot(im); im.convert('RGB').save(O+'m5.jpg',quality=95); P.append(('m5','نقلة وحدة… وخلصت اللعبة ♟️','#براوني'))
# 6 honest americano
im=pbase('gen10/d01.png'); phead(im,'مش مُـــرّ...','هو بس صريـــح')
bubble(im,880,560,'بصراحة؟',DB(50),tail='left')
emph(im,350,560,-2.2)
pfoot(im); im.convert('RGB').save(O+'m6.jpg',quality=95); P.append(('m6','مش مُرّ… هو بس صريح ☕🖤','#آيس_أمريكانو'))
sh=Image.new('RGB',(3*400+20,2*500+10),(30,30,30))
for i,(n,_,_) in enumerate(P): sh.paste(Image.open(O+n+'.jpg').resize((400,500)),((i%3)*410,(i//3)*510))
sh.save(O+'preview.jpg')
import json; json.dump(P,open(O+'captions.json','w'),ensure_ascii=False); print('ok')
