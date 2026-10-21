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
  {1:(140,800,580,1080),2:(580,920,850,1110)},[(420,690,'إندومي','سادة مع بهارات',[(300,735),(270,770),(300,815)]),(1000,830,'شاي','سخن ومنعنع',[(880,880),(850,900),(800,940)])],'12',None,
  'إندومي وشاي بـ12 شيكل بس 🍜☕'),
 ('camp/c05.png','c2','4 إندومي و4 شاي','جيب الشلّـــة...','كومبو الشلّـــة',
  {1:(680,540,950,820),2:(200,330,340,480)},[(400,930,'4 إندومي','سادة مع بهارات',[(290,880),(270,850),(290,815)]),(1010,540,'4 شاي','على الطاولة',[(890,500),(870,480),(850,460)])],'40','بدل 48',
  'جيب الشلّة… 4 إندومي و4 شاي بـ40 شيكل 🍜🍜🍜🍜'),
 ('gen5/n5.png','c3','كومبو الرواق','قهوة على مهلـــك...','وتشيز يكمّل الحكايـــة',
  {1:(440,690,680,930),2:(650,540,780,710)},[(1,'تشيز كيك','بستاشيو'),(2,'آيس لاتيه','بارد وناعم')],'20',None,
  'قهوة على مهلك… وتشيز يكمّل الحكاية، بـ20 شيكل 🤎'),
]
caps=[]
for src_,name,pill,l1,l2,bbs,labs,num,sub,cap in C:
    base=cover(Image.open(S+src_).convert('RGB')); im=topdark(base); CUR[0]=im.copy()
    BB.clear(); BB.update(bbs)
    head(im,pill,l1,l2)
    for lab in labs:
        if len(lab)==3: auto_label(im,*lab)
        else: mlabel(im,*lab)
    price(im,175,255,num,sub)
    footer_c(im); im.convert('RGB').save(O+name+'.jpg',quality=95); caps.append((name,cap))
sh=Image.new('RGB',(3*400+20,500),(30,30,30))
for i,(n,_) in enumerate(caps): sh.paste(Image.open(O+n+'.jpg').resize((400,500)),(i*410,0))
sh.save(O+'preview.jpg')
import json; json.dump(caps,open(O+'caps.json','w'),ensure_ascii=False); print('ok')
