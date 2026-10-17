src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/p20.py').read()
exec(src[:src.index('\nP=[\n')])
import sys,os
LABELS=len(sys.argv)>1
TAG='مين إنت بالشتا؟'
FILES={1:'Gf915ahAJjUvdXfW8nCXIRQBEBLlr3Hi6yYrUuGs.jpg',2:'kL0t64P8riXpZaJCoRr4tKmbGqT8VvuS04x8qfa9 (1).jpg',3:'txl6ZuwYP1f3l1GKDh8yabRaJaNa8HfDWNtfmiLi.jpg',
       4:'F3nVlXf3tbFBaHv6aBpVYSYo0Y6gjEXaylLGk49K.jpg',5:'NmZKk6JU3tCcH5jRbfrh46bhbLJdOcWbNoZ1UMyE.jpg',6:'jcQxJ018gXG6mxLDlrOfRbTKhGqQrPlsWq1JQOvY.jpg'}
FOC={1:(.5,.62,.30),2:(.5,.6,.34),3:(.42,.66,.28),4:(.45,.66,.30),5:(.45,.62,.32),6:(.5,.66,.36)}
CROP={1:(.5,.5,1.0),2:(.5,.5,1.0),3:(.5,.5,1.0),4:(.5,.5,1.0),5:(.5,.5,1.0),6:(.5,.5,1.0)}
BB={1:(365,662,797,959),2:(400,445,724,1053),3:(346,648,797,1004),4:(351,662,797,972),5:(373,419,707,1134),6:(284,540,797,972)}
def bbox(n): return BB.get(n,(400,700,680,1100))
P=[
 (1,'البردان الدايـــم...','إنت هوت شوكليـــت',('هوت شوكليت','بيدفّي القلب قبل الإيدين'),'البردان الدايم؟','هوت شوكليـــت'),
 (2,'إذا بتحب المطـــر...','إنت لاتيه سخـــن',('لاتيه سخن','طبقات ودفا'),'بتحب المطر؟','لاتيه سخـــن'),
 (3,'طالب بموسم الامتحانـــات؟','إنت إسبريســـو',('إسبريسو','شوت بيصحّيك'),'عندك امتحان؟','إسبريســـو'),
 (4,'ملك البطانيـــة...','إنت شاي أعشـــاب',('شاي أعشاب','دافي وهادي'),'ملك البطانية؟','شاي أعشـــاب'),
 (5,'"أنا مش بردان"...','إنت آيس أمريكانـــو',('آيس أمريكانو','حتى بعز الشتا'),'مش بردان؟','آيس أمريكانـــو'),
 (6,'الحلو أول إشـــي...','إنت قنبلة النُّـــص',('قنبلة النُّص','بستاشيو ونوتيلا'),'الحلو أول؟','قنبلة النُّـــص'),
]
def layout(img,l1,l2):
    d=ImageDraw.Draw(img); f=SB(28); w=tw(d,TAG,f); XR=1010
    d.rounded_rectangle([XR-w-44,60,XR,110],radius=25,fill=TEAL); d.text((XR-22,97),TAG,font=f,fill=WHITE,direction='rtl',anchor='rs')
    T(d,XR,205,l1,DB(66),WHITE)
    f2=DB(84)
    while tw(d,l2,f2)>900: f2=DB(f2.size-4)
    hlw(img,XR,315,l2,f2,WHITE)
os.makedirs(S+'out/who',exist_ok=True); posts=[]
for n,l1,l2,lab,s1,s2 in P:
    src_=Image.open(S+'products/'+FILES[n]).convert('RGB')
    cx,cy,z=CROP[n]; fx,fy,fr=FOC[n]
    base=grade(cover(src_,cx,cy,z),focus=(fx,fy),fr=fr)
    im=base.convert('RGBA'); CUR[0]=im.copy(); clean=im.copy()
    layout(im,l1,l2)
    if LABELS: auto_label(im,n,*lab)
    footer_c(im)
    im.convert('RGB').save(S+f'out/who/who_post{n:02d}.jpg',quality=95); posts.append(im)
    st=Image.new('RGBA',(1080,1920),(12,20,19,255)); st.paste(clean,(0,120))
    d=ImageDraw.Draw(st); d.line([(0,120),(1080,120)],fill=TEAL,width=3); d.line([(0,1470),(1080,1470)],fill=TEAL,width=3)
    CUR[0]=st.copy()
    d.text((1010,1565),s1,font=DB(70),fill=WHITE,direction='rtl',anchor='rs')
    hl(st,d,1010,1660,s2,DB(84),pad=(14,4),skew=7); d=ImageDraw.Draw(st); d.text((1010,1660),s2,font=DB(84),fill=WHITE,direction='rtl',anchor='rs')
    lg=Image.open(S+'logo.png'); lg=lg.resize((120,round(lg.height*120/lg.width)),Image.LANCZOS); st.alpha_composite(lg,(70,1500))
    d.text((1010,1745),'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',font=SR(24),fill=(190,205,202),direction='rtl',anchor='rs')
    ft=SB(28); w=tw(d,TAG,ft); d.rounded_rectangle([1010-w-44,150,1010,200],radius=25,fill=TEAL); d.text((1010-22,187),TAG,font=ft,fill=WHITE,direction='rtl',anchor='rs')
    st.convert('RGB').save(S+f'out/who/who_story{n:02d}.jpg',quality=95)
sh=Image.new('RGB',(400*3,500*2))
for i,im in enumerate(posts): sh.paste(im.convert('RGB').resize((400,500)),((i%3)*400,(i//3)*500))
sh.save(S+'out/who/posts.jpg')
sh=Image.new('RGB',(270*6,480))
for i in range(6): sh.paste(Image.open(S+f'out/who/who_story{i+1:02d}.jpg').resize((270,480)),(i*270,0))
sh.save(S+'out/who/stories.jpg'); print('ok')
