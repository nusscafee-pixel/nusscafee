import os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'world20_layouts.py')).read()
exec(src[:src.index('\nP=[\n')])
import numpy as np
def bbox(n):
    if n==2: return (135,700,580,1030)
    if n==7: return (330,960,800,1250)
    m=np.asarray(Image.open(S+f'camp/m{n:02d}.png').convert('L'))>128
    ys,xs=np.where(m[420:1250]); ys=ys+420
    if len(xs)==0: return (400,600,680,1100)
    x0,x1=np.percentile(xs,[5,95]); y0,y1=np.percentile(ys,[5,95]); return (int(x0),int(y0),int(x1),int(y1))
TAG='شتوية النُّص'
def tag(img,x=70,y=58):
    d=ImageDraw.Draw(img); f=SB(28); w=tw(d,TAG,f)
    d.rounded_rectangle([x,y,x+w+44,y+50],radius=25,fill=TEAL); d.text((x+22+w,y+37),TAG,font=f,fill=WHITE,direction='rtl',anchor='rs')
# campaign variants of layouts
def CA(img,giant,sub):
    fg,acc,mut=col(img,(60,60,1020,420)); d=ImageDraw.Draw(img)
    d.line([(70,118),(1010,118)],fill=acc,width=2); T(d,1010,100,TAG,SB(26),fg); d.text((70,100),'INDOMIE',font=SB(26),fill=acc,anchor='ls')
    f=DB(150); T(d,1010,280,giant,f,fg); w=tw(d,giant,f); d.rectangle([1010-w*0.55,298,1010,310],fill=TEAL)
    T(d,1010,372,sub,SB(40),fg)
def CB(img,a,b,c): L_B(img,a,b,c); tag(img)
def CC(img,a,b):
    fg,acc,mut=col(img,(160,60,920,420)); d=ImageDraw.Draw(img)
    d.text((W/2,120),'— '+TAG+' —',font=SB(30),fill=acc,anchor='ms',direction='rtl')
    f1=DB(80); w1=tw(d,a,f1); T(d,W/2+w1/2,240,a,f1,fg); f2=DB(100); w2=tw(d,b,f2); hlw(img,W/2+w2/2,370,b,f2,fg)
def CD(img,q,attr): L_D(img,q,attr); tag(img)
def CE(img,o,a,b): L_E(img,o,a,b); tag(img)
P=[
 (1,CA,('جوعـــة','الساعة ١٢ بالليل... وبدك إندومي'),('إندومي','سادة مع بهارات')),
 (2,CB,('إندومي','وكاسة شاي','أحلى ثنائي'),('إندومي','وشاي بالنعنع')),
 (3,CC,('الدراسة بدها...','إندومـــي'),('إندومي','سادة مع بهارات')),
 (4,CD,('السرّ|بالبهارات','إندومي النُّص'),('بهارات','النُّص')),
 (5,CE,('الشلّة','إندومي للشلّة...','كلنا جوعانين'),('إندومي','للكل')),
 (6,CA,('تيكاوي','خذ إندوميك معك... ودفّي طريقك'),('تيكاوي','بكاسة النُّص')),
 (7,CB,('دفّي','إيديـــك','وقلبك كمان'),('إندومي','سخنة')),
 (8,CC,('آخر الأسبوع...','فيلم وإندومـــي'),('إندومي','سادة مع بهارات')),
 (9,CD,('مرقة سخنة|من النار لإيدك','إندومي النُّص'),('إندومي','من النار')),
 (10,CE,('شتوية','الشباك مغبّش...','والإندومي سخنة'),('إندومي','سادة مع بهارات')),
]
STORY=[('جوعة آخر الليل؟','إندومـــي'),('إندومي','وكاسة شاي'),('الدراسة بدها','إندومـــي'),('السرّ','بالبهارات'),('جيب الشلّة','وتعـــال'),('خذها','تيكاوي'),('دفّي','إيديـــك'),('آخر الأسبوع','إندومـــي'),('من النار','لإيـــدك'),('الشتا','بدها إندومـــي')]
posts=[]; 
for i,(n,fn,args,lab) in enumerate(P):
    im=cover(Image.open(S+f'camp/c{n:02d}.png').convert('RGB')).convert('RGBA'); CUR[0]=im.copy()
    clean=im.copy()
    fn(im,*args); auto_label(im,n,*lab); footer_c(im)
    im.convert('RGB').save(S+f'out/camp_post{n:02d}.jpg',quality=95); posts.append(im)
    # story
    st=Image.new('RGBA',(1080,1920),(12,20,19,255))
    n_=Image.effect_noise((1080,1920),10).convert('L').point(lambda v:v//10)
    st.paste(clean,(0,120)); 
    d=ImageDraw.Draw(st); d.line([(0,120),(1080,120)],fill=TEAL,width=3); d.line([(0,1470),(1080,1470)],fill=TEAL,width=3)
    CUR[0]=st.copy()
    l1,b=STORY[i]; f=DB(70)
    d.text((1010,1565),l1,font=f,fill=WHITE,direction='rtl',anchor='rs')
    hl(st,d,1010,1660,b,DB(84),pad=(14,4),skew=7); d=ImageDraw.Draw(st); d.text((1010,1660),b,font=DB(84),fill=WHITE,direction='rtl',anchor='rs')
    lg=Image.open(S+'logo.png'); lg=lg.resize((120,round(lg.height*120/lg.width)),Image.LANCZOS); st.alpha_composite(lg,(70,1500))
    f2=SR(24); d.text((70+60,1700),'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',font=f2,fill=(190,205,202),anchor='ms',direction='rtl') if False else d.text((1010,1745),'📍 تقاطع شارع ملعب فلسطين، مع شارع التايلاندي'.replace('📍 ',''),font=f2,fill=(190,205,202),direction='rtl',anchor='rs')
    # tag on image top-right inside story
    dd=ImageDraw.Draw(st); ft=SB(28); w=tw(dd,TAG,ft); dd.rounded_rectangle([1010-w-44,150,1010,200],radius=25,fill=TEAL); dd.text((1010-22,187),TAG,font=ft,fill=WHITE,direction='rtl',anchor='rs')
    st.convert('RGB').save(S+f'out/camp_story{n:02d}.jpg',quality=95)
sh=Image.new('RGB',(400*5,500*2))
for i,im in enumerate(posts): sh.paste(im.convert('RGB').resize((400,500)),((i%5)*400,(i//5)*500))
sh.save(S+'out/camp_posts.jpg')
sh=Image.new('RGB',(270*10,480))
for i in range(10): sh.paste(Image.open(S+f'out/camp_story{i+1:02d}.jpg').resize((270,480)),(i*270,0))
sh.save(S+'out/camp_stories.jpg'); print('ok')
