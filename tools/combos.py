src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/p20.py').read()
exec(src[:src.index('\nP=[\n')])
import os
O=S+'out/combo/'; os.makedirs(O,exist_ok=True)
BB={}
def bbox(n): return BB[n]
def topdark(im,h=470,a=170):
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(h): d.line([(0,y),(W,y)],fill=(8,12,11,int(a*(1-y/h)**1.2)))
    o=im.convert('RGBA'); o.alpha_composite(ov); return o
def head(img,pill,l1,l2):
    d=ImageDraw.Draw(img); f=SB(28); w=tw(d,pill,f); XR=1010
    d.rounded_rectangle([XR-w-44,60,XR,110],radius=25,fill=TEAL); d.text((XR-22,97),pill,font=f,fill=WHITE,direction='rtl',anchor='rs')
    T(d,XR,205,l1,DB(66),WHITE); f2=DB(84)
    while tw(d,l2,f2)>720: f2=DB(f2.size-4)
    hlw(img,XR,315,l2,f2,WHITE)
def mlabel(img,lx,ly,bold,sub,pts):
    d=ImageDraw.Draw(img); fb=SB(40); fs=SR(30)
    hl(img,d,lx,ly,bold,fb,pad=(8,2),skew=3); d=ImageDraw.Draw(img)
    d.text((lx,ly),bold,font=fb,fill=WHITE,direction='rtl',anchor='rs'); d.text((lx,ly+42),sub,font=fs,fill=WHITE,direction='rtl',anchor='rs')
    arrow_c(img,pts,WHITE)

YEL=(255,206,38); ORG=(240,120,30); RED=(214,48,40); INK2=(20,24,22)
DBk=lambda s_:F('thmanyahserifdisplay-Black',s_); SBk=lambda s_:F('thmanyahsans-Black',s_)
def starburst(d,cx,cy,r1,r2,n,fill):
    pts=[]
    for k in range(2*n):
        a=math.pi*k/n; r=r1 if k%2==0 else r2; pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    d.polygon(pts,fill=fill)
def price_banner(img,cx,cy,old,new,tag='عرض!',rot=6):
    tmp=ImageDraw.Draw(Image.new('RGBA',(10,10)))
    fN=SBk(150); nw=tmp.textbbox((0,0),new,font=fN)[2]
    fo=SB(40); fs=SB(46); so='بدل '+old; ow=tw(tmp,so,fo); sw=tw(tmp,'شيكل بس',fs)
    stack=max(ow,sw); bw=40+nw+30+stack+40; bh=200
    Wl,Hl=int(bw+160),int(bh+230); lay=Image.new('RGBA',(Wl,Hl),(0,0,0,0)); d=ImageDraw.Draw(lay)
    bx0,by0=80,130; bx1,by1=bx0+bw,by0+bh
    d.polygon([(bx0,by0+10),(bx1,by0-6),(bx1-16,by1),(bx0+14,by1+8)],fill=YEL)
    d.text((bx0+40,by1-34),new,font=fN,fill=INK2,anchor='ls')
    xr=bx1-36
    d.text((xr,by0+78),so,font=fo,fill=INK2,direction='rtl',anchor='rs')
    d.line([(xr-ow-6,by0+66),(xr+6,by0+42)],fill=RED,width=7)
    d.text((xr,by1-40),'شيكل',font=fs,fill=INK2,direction='rtl',anchor='rs')
    w1=tw(d,'شيكل ',fs); d.text((xr-w1,by1-40),'بس',font=fs,fill=RED,direction='rtl',anchor='rs')
    starburst(d,bx0+10,by0-18,100,74,14,RED); d.text((bx0+10,by0-2),tag,font=SBk(38),fill=WHITE,direction='rtl',anchor='ms')
    for (x0,y0,x1,y1) in [(bx1+18,by0+10,bx1+50,by0-14),(bx1+24,by0+90,bx1+58,by0+88),(bx1+14,by1-10,bx1+44,by1+14),(bx0+30,by1+30,bx0+10,by1+56),(bx0+110,by1+34,bx0+104,by1+64)]:
        d.line([(x0,y0),(x1,y1)],fill=YEL,width=7)
    lay=lay.rotate(rot,expand=True,resample=Image.BICUBIC)
    x=int(cx-lay.width/2); y=int(cy-lay.height/2)
    x=max(-5,min(W-lay.width+5,x))
    img.alpha_composite(lay,(x,y))

def price(img,cx,cy,num,sub=None):
    d=ImageDraw.Draw(img); r=105
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(241,234,221)); d.ellipse([cx-r+10,cy-r+10,cx+r-10,cy+r-10],outline=TEAL,width=3)
    d.text((cx,cy+22),num,font=SB(92),fill=TEAL,anchor='ms')
    d.text((cx,cy+62),'شيكل',font=SB(30),fill=(18,28,26),direction='rtl',anchor='ms')
    if sub:
        f=SR(28); d.text((cx,cy-r-14),sub,font=f,fill=WHITE,direction='rtl',anchor='ms')
        w=tw(d,sub,f); d.line([(cx-w/2-4,cy-r-24),(cx+w/2+4,cy-r-24)],fill=(222,96,80),width=4)
C=[
 ('camp/c02.png','c1','كومبو الطالب','إندومي وكاسة شـــاي...','بتكفّي لآخر الدرس',
  [(420,690,'إندومي','سادة مع بهارات',[(300,735),(270,770),(300,815)]),(1000,830,'شاي','سخن ومنعنع',[(880,880),(850,900),(800,940)])],
  ('15','12',790,560),'إندومي وشاي بـ12 شيكل بدل 15 🍜☕'),
 ('camp/c05.png','c2','4 إندومي و4 شاي','جيب الشلّـــة...','كومبو الشلّـــة',
  [(400,930,'4 إندومي','سادة مع بهارات',[(290,880),(270,850),(290,815)]),(1010,540,'4 شاي','على الطاولة',[(890,500),(870,480),(850,460)])],
  ('48','40',330,1075),'جيب الشلّة… 4 إندومي و4 شاي بـ40 شيكل بدل 48 🍜🍜🍜🍜'),
 ('gen5/n5.png','c3','كومبو الرواق','قهوة على مهلـــك...','وتشيز يكمّل الحكايـــة',
  [(1,'تشيز كيك','بستاشيو'),(2,'آيس لاتيه','بارد وناعم')],
  ('25','20',300,1060),'قهوة على مهلك… وتشيز يكمّل الحكاية، بـ20 شيكل بدل 25 🤎'),
 ('gen5/n1.png','c4','عرض التيكاوي','مستعجـــل؟','قهوتك عالطريـــق',
  [(1010,560,'قهوة تيكاوي','معك وين ما رحت',[(860,600),(810,612),(760,600)])],
  ('10','7',270,560),'مستعجل؟ قهوتك عالطريق بـ7 شيكل بدل 10 ☕🚗'),
 ('gen5/n2.png','c5','عرض الآيس لاتيه','رشفة وحـــدة...','وبتنسى الدنيـــا',
  [(300,600,'آيس لاتيه','بارد وناعم',[(200,640),(250,700),(340,720)])],
  ('14','10',860,760),'رشفة وحدة… وبتنسى الدنيا. آيس لاتيه بـ10 شيكل بدل 14 🤎'),
 ('gen5/n4.png','c6','كومبو الصحوة','إسبريسو وشوكـــولا...','صحوة على أصولهـــا',
  [(420,660,'إسبريسو','شوت مركّز',[(330,685),(345,715),(380,745)]),(330,1080,'شوكولا','قطعة مرّة',[(230,1040),(222,1010),(226,975)])],
  ('10','8',820,580),'إسبريسو وقطعة شوكولا… صحوة على أصولها، بـ8 شيكل بدل 10 ⚡'),
]
BBX={'c3':{1:(440,690,680,930),2:(650,540,780,710)}}
caps=[]
for src_,name,pill,l1,l2,labs,pr,cap in C:
    base=cover(Image.open(S+src_).convert('RGB')); im=topdark(base); CUR[0]=im.copy()
    BB.clear(); BB.update(BBX.get(name,{}))
    head(im,pill,l1,l2)
    for lab in labs:
        if len(lab)==3: auto_label(im,*lab)
        else: mlabel(im,*lab)
    price_banner(im,pr[2],pr[3],pr[0],pr[1])
    footer_c(im); im.convert('RGB').save(O+name+'.jpg',quality=95); caps.append((name,cap))
sh=Image.new('RGB',(3*400+20,1010),(30,30,30))
for i,(n,_) in enumerate(caps): sh.paste(Image.open(O+n+'.jpg').resize((400,500)),((i%3)*410,(i//3)*510))
sh.save(O+'preview.jpg')
import json; json.dump(caps,open(O+'caps.json','w'),ensure_ascii=False); print('ok')
