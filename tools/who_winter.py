src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/p20.py').read()
exec(src[:src.index('\nP=[\n')])
import os,sys
TAG='مين إنت بالشتا؟'
def k(x0,y0,x1,y1): return (int(x0*1.406),int(y0*1.406-45),int(x1*1.406),int(y1*1.406-45))
BB={1:k(265,590,540,780),2:k(218,475,420,840),5:k(297,535,492,895)}
def bbox(n): return BB[n]
P=[
 (1,'البردان الدايـــم...','إنت هوت شوكليـــت',('هوت شوكليت','بيدفّي القلب قبل الإيدين'),'البردان الدايم؟','هوت شوكليـــت'),
 (2,'إذا بتحب المطـــر...','إنت لاتيه سخـــن',('لاتيه سخن','طبقات ودفا'),'بتحب المطر؟','لاتيه سخـــن'),
 (3,'طالب بموسم الامتحانـــات؟','إنت إسبريســـو',('إسبريسو','شوت بيصحّيك'),'عندك امتحان؟','إسبريســـو'),
 (4,'ملك البطانيـــة...','إنت شاي أعشـــاب',('شاي أعشاب','دافي وهادي'),'ملك البطانية؟','شاي أعشـــاب'),
 (5,'"أنا مش بردان"...','إنت آيس أمريكانـــو',('آيس أمريكانو','حتى بعز الشتا'),'مش بردان؟','آيس أمريكانـــو'),
 (6,'الحلو أول إشـــي...','إنت قنبلة النُّـــص',('قنبلة النُّص','بستاشيو ونوتيلا'),'الحلو أول؟','قنبلة النُّـــص'),
]
def topdark(im):
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(440): d.line([(0,y),(W,y)],fill=(8,12,11,int(150*(1-y/440)**1.3)))
    o=im.convert('RGBA'); o.alpha_composite(ov); return o
def layout(img,l1,l2):
    d=ImageDraw.Draw(img); f=SB(28); w=tw(d,TAG,f); XR=1010
    d.rounded_rectangle([XR-w-44,60,XR,110],radius=25,fill=TEAL); d.text((XR-22,97),TAG,font=f,fill=WHITE,direction='rtl',anchor='rs')
    T(d,XR,205,l1,DB(66),WHITE)
    f2=DB(84)
    while tw(d,l2,f2)>900: f2=DB(f2.size-4)
    hlw(img,XR,315,l2,f2,WHITE)
os.makedirs(S+'out/who2',exist_ok=True); done=[]
for n,l1,l2,lab,s1,s2 in P:
    p=S+f'who2/g{n:02d}.png'
    if not os.path.exists(p): continue
    base=cover(Image.open(p).convert('RGB'))
    clean=base.convert('RGBA'); im=topdark(base); CUR[0]=im.copy()
    layout(im,l1,l2); auto_label(im,n,*lab); footer_c(im)
    im.convert('RGB').save(S+f'out/who2/who_post{n:02d}.jpg',quality=95); done.append(n)
    st=Image.new('RGBA',(1080,1920),(12,20,19,255)); st.paste(clean,(0,120))
    d=ImageDraw.Draw(st); d.line([(0,120),(1080,120)],fill=TEAL,width=3); d.line([(0,1470),(1080,1470)],fill=TEAL,width=3)
    CUR[0]=st.copy()
    d.text((1010,1565),s1,font=DB(70),fill=WHITE,direction='rtl',anchor='rs')
    hl(st,d,1010,1660,s2,DB(84),pad=(14,4),skew=7); d=ImageDraw.Draw(st); d.text((1010,1660),s2,font=DB(84),fill=WHITE,direction='rtl',anchor='rs')
    lg=Image.open(S+'logo.png'); lg=lg.resize((120,round(lg.height*120/lg.width)),Image.LANCZOS); st.alpha_composite(lg,(70,1500))
    d.text((1010,1745),'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',font=SR(24),fill=(190,205,202),direction='rtl',anchor='rs')
    ft=SB(28); w=tw(d,TAG,ft); d.rounded_rectangle([1010-w-44,150,1010,200],radius=25,fill=TEAL); d.text((1010-22,187),TAG,font=ft,fill=WHITE,direction='rtl',anchor='rs')
    st.convert('RGB').save(S+f'out/who2/who_story{n:02d}.jpg',quality=95)
sh=Image.new('RGB',(400*len(done)+270*len(done),500))
for i,n in enumerate(done):
    sh.paste(Image.open(S+f'out/who2/who_post{n:02d}.jpg').resize((400,500)),(i*400,0))
    sh.paste(Image.open(S+f'out/who2/who_story{n:02d}.jpg').resize((270,480)),(400*len(done)+i*270,10))
sh.save(S+'out/who2/preview.jpg'); print(done)
