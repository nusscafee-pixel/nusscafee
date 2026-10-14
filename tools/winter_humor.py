src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/p20.py').read()
exec(src[:src.index('\nP=[\n')])
import numpy as np
BB={1:(418,891,689,1107),2:(351,661,810,972),3:(400,661,760,958),4:(324,796,700,1053),5:(405,931,715,1174),6:(391,445,742,1066)}
def bbox(n): return BB[n]
TAG='الشتا قرّب'
def soften_band(im):
    a=np.asarray(im.convert('L'),dtype=float); sd=a.std(axis=1); b=0
    while b<H*0.4 and sd[b]<6: b+=1
    if b<40: return im
    col_=tuple(int(v) for v in np.asarray(im)[5:b-5].reshape(-1,3).mean(0))
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(b-10,min(H,b+170)):
        t=(y-(b-10))/180; d.line([(0,y),(W,y)],fill=col_+(int(255*(1-t)**1.6),))
    o=im.convert('RGBA'); o.alpha_composite(ov); return o.convert('RGB')
def layout(img,l1,l2):
    d=ImageDraw.Draw(img); f=SB(28); w=tw(d,TAG,f); XR=1010
    d.rounded_rectangle([XR-w-44,60,XR,110],radius=25,fill=TEAL); d.text((XR-22,97),TAG,font=f,fill=WHITE,direction='rtl',anchor='rs')
    f1=DB(66); T(d,XR,205,l1,f1,WHITE)
    f2=DB(84); 
    while tw(d,l2,f2)>900: f2=DB(f2.size-4)
    hlw(img,XR,315,l2,f2,WHITE)
P=[
 (1,'طلّع الجاكيـــت...','ونزّل الهوت شوكليـــت',('هوت شوكليت','سخن ودسم'),'طلّع الجاكيت','والهوت شوكليـــت'),
 (2,'صرت تحكي ويطلع بخـــار؟','يعني وقت الكابتشيـــنو',('كابتشينو','رغوة وبخار'),'صرت تحكي','ويطلع بخـــار؟'),
 (3,'ستّك بتقول: البس منيـــح','وإحنا بنقول: اشرب شـــاي',('شاي بالنعنع','متل شاي ستّك'),'البس منيح...','واشرب شـــاي'),
 (4,'الريجيـــم؟','خلّيه لبعد الشتـــا',('براوني','كراميل وكريمة'),'الريجيم؟','بعد الشتـــا'),
 (5,'الفرشة دافية... والصبح بـــارد','الحل؟ إسبريســـو',('إسبريسو','شوت بيصحّيك'),'الصبح بارد؟','إسبريســـو'),
 (6,'المطر جاي؟','خلّيه ييجـــي',('لاتيه سخن','طبقات ودفا'),'المطر جاي؟','خلّيه ييجـــي'),
]
import os; os.makedirs(S+'out/win',exist_ok=True); posts=[]
for n,l1,l2,lab,s1,s2 in P:
    base=soften_band(cover(Image.open(S+f'win/c{n:02d}.png').convert('RGB')))
    im=base.convert('RGBA'); CUR[0]=im.copy(); clean=im.copy()
    layout(im,l1,l2); auto_label(im,n,*lab); footer_c(im)
    im.convert('RGB').save(S+f'out/win/win_post{n:02d}.jpg',quality=95); posts.append(im)
    st=Image.new('RGBA',(1080,1920),(12,20,19,255)); st.paste(clean,(0,120))
    d=ImageDraw.Draw(st); d.line([(0,120),(1080,120)],fill=TEAL,width=3); d.line([(0,1470),(1080,1470)],fill=TEAL,width=3)
    CUR[0]=st.copy()
    d.text((1010,1565),s1,font=DB(70),fill=WHITE,direction='rtl',anchor='rs')
    hl(st,d,1010,1660,s2,DB(84),pad=(14,4),skew=7); d=ImageDraw.Draw(st); d.text((1010,1660),s2,font=DB(84),fill=WHITE,direction='rtl',anchor='rs')
    lg=Image.open(S+'logo.png'); lg=lg.resize((120,round(lg.height*120/lg.width)),Image.LANCZOS); st.alpha_composite(lg,(70,1500))
    d.text((1010,1745),'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',font=SR(24),fill=(190,205,202),direction='rtl',anchor='rs')
    ft=SB(28); w=tw(d,TAG,ft); d.rounded_rectangle([1010-w-44,150,1010,200],radius=25,fill=TEAL); d.text((1010-22,187),TAG,font=ft,fill=WHITE,direction='rtl',anchor='rs')
    st.convert('RGB').save(S+f'out/win/win_story{n:02d}.jpg',quality=95)
sh=Image.new('RGB',(400*3,500*2))
for i,im in enumerate(posts): sh.paste(im.convert('RGB').resize((400,500)),((i%3)*400,(i//3)*500))
sh.save(S+'out/win/posts.jpg')
sh=Image.new('RGB',(270*6,480))
for i in range(6): sh.paste(Image.open(S+f'out/win/win_story{i+1:02d}.jpg').resize((270,480)),(i*270,0))
sh.save(S+'out/win/stories.jpg'); print('ok')
