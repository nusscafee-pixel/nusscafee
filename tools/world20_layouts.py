import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'post.py')).read())
import numpy as np
TEAL=(47,112,104); TL=(120,190,180); DARK=(22,34,32)
def lum(im,box):
    a=np.asarray(im.convert('L').crop(box),dtype=float); return a.mean()
def col(im,box): return (DARK,TEAL,(70,80,78)) if lum(im,box)>135 else (WHITE,TL,(205,215,212))
CUR=[None]
def T(d,x,y,t,f,fill,anchor='rs'):
    if fill in (WHITE,DARK,(205,215,212),(70,80,78)) and CUR[0] is not None:
        b=d.textbbox((x,y),t,font=f,direction='rtl',anchor=anchor)
        fill=DARK if lum(CUR[0],(max(0,b[0]),max(0,b[1]),min(W,b[2]),min(H,b[3])))>140 else (WHITE if fill in (WHITE,DARK) else (205,215,212))
    d.text((x,y),t,font=f,fill=fill,direction='rtl',anchor=anchor)
def hlw(img,XR,y,t,f,fg):  # teal block word, text white always
    d=ImageDraw.Draw(img); hl(img,d,XR,y,t,f,pad=(16,4),skew=8); d=ImageDraw.Draw(img); d.text((XR,y),t,font=f,fill=WHITE,direction='rtl',anchor='rs')
def bbox(n):
    m=np.asarray(Image.open(S+f'g20/m{n:02d}.png').convert('L'))>128
    ys,xs=np.where(m[400:1250]); ys=ys+400
    if len(xs)==0: return (400,600,680,1100)
    x0,x1=np.percentile(xs,[5,95]); y0,y1=np.percentile(ys,[5,95]); return (int(x0),int(y0),int(x1),int(y1))
def auto_label(img,n,bold,sub):
    x0,y0,x1,y1=bbox(n)
    if n==5: x0,y0,x1,y1=(700,620,1000,900)
    cy=int(y0+(y1-y0)*0.30)
    d=ImageDraw.Draw(img); fb=SB(40); fs=SR(30); wb=max(tw(d,bold,fb),tw(d,sub,fs))
    ly=max(600,cy-30)
    if W-x1>=x0:
        lx=min(W-55,x1+150+wb); sx=lx-wb-14; ex=x1+12
        pts=[(sx,ly-20),(sx-35,ly-70),(ex+60,ly-80),(ex,ly-25)]
    else:
        lx=max(55+wb,x0-150); sx=lx+14; ex=x0-12
        pts=[(sx,ly-20),(sx+35,ly-70),(ex-60,ly-80),(ex,ly-25)]
    hl(img,d,lx,ly,bold,fb,pad=(8,2),skew=3); d=ImageDraw.Draw(img)
    d.text((lx,ly),bold,font=fb,fill=WHITE,direction='rtl',anchor='rs'); T(d,lx,ly+42,sub,fs,WHITE)
    b=(min(p[0] for p in pts),min(p[1] for p in pts),max(p[0] for p in pts),max(p[1] for p in pts))
    arrow_c(img,pts,DARK if lum(img,b)>150 else WHITE)
def arrow_c(base,pts,color):
    d=ImageDraw.Draw(base); P=[pts[0]]+pts+[pts[-1]]; out=[]
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        for k in range(20):
            t=k/20; t2,t3=t*t,t*t*t
            out.append(tuple(.5*((2*p1[j])+(-p0[j]+p2[j])*t+(2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2+(-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3) for j in (0,1)))
    out.append(pts[-1]); d.line(out,fill=color,width=3,joint='curve')
    (ax,ay),(bx,by)=out[-4],out[-1]; a=math.atan2(by-ay,bx-ax)
    for s in (2.5,-2.5): d.line([(bx,by),(bx-18*math.cos(a+s*.2),by-18*math.sin(a+s*.2))],fill=color,width=3)
def footer_c(img):
    fg,acc,_=col(img,(40,1230,520,1320)); d=ImageDraw.Draw(img); xr=505
    hl(img,d,xr-28,H-92,'عنواننا',SB(34),pad=(8,2),skew=3); d=ImageDraw.Draw(img); T(d,xr-28,H-92,'عنواننا',SB(34),WHITE)
    T(d,xr-28,H-48,'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',SR(22),fg)
    d.ellipse([xr-9,H-118,xr+3,H-106],fill=acc); d.line([xr-3,H-106,xr-3,H-58],fill=fg,width=2)
    lg=Image.open(S+'logo.png').convert('RGBA'); lg=lg.resize((118,round(lg.height*118/lg.width)),Image.LANCZOS)
    if fg==DARK:
        a=lg.getchannel('A'); lg=Image.merge('RGBA',(*Image.new('RGB',lg.size,DARK).split(),a))
    img.alpha_composite(lg,(W-60-118,H-48-lg.height))
# ---- layouts
def L_A(img,num,giant,sub):  # editorial giant word
    fg,acc,mut=col(img,(60,60,1020,420)); d=ImageDraw.Draw(img)
    d.line([(70,118),(1010,118)],fill=acc,width=2)
    T(d,1010,100,'نُص كافيه',SB(26),fg); d.text((70,100),f'No.{num:02d}',font=SB(26),fill=acc,anchor='ls')
    f=DB(165); T(d,1010,290,giant,f,fg)
    w=tw(d,giant,f); d.rectangle([1010-w*0.55,308,1010,320],fill=TEAL)
    T(d,1010,378,sub,SB(40),mut if fg==WHITE else DARK)
def L_B(img,l1,l2,l3):  # stacked column with rule
    fg,acc,mut=col(img,(380,80,1060,480)); d=ImageDraw.Draw(img)
    d.line([(1032,110),(1032,450)],fill=acc,width=4)
    T(d,1005,175,l1,DB(70),fg)
    hlw(img,1005,300,l2,DB(104),fg); d=ImageDraw.Draw(img)
    T(d,1005,410,l3,DB(70),fg)
def L_C(img,l1,b):  # centered minimal
    fg,acc,mut=col(img,(160,60,920,420)); d=ImageDraw.Draw(img)
    t='جديد عنّا'; f=SB(30); w=tw(d,'نُص كافيه',f)
    d.text((W/2,120),'— نُص كافيه —',font=f,fill=acc,anchor='ms',direction='rtl')
    f1=DB(80); w1=tw(d,l1,f1); T(d,W/2+w1/2,240,l1,f1,fg)
    f2=DB(100); w2=tw(d,b,f2); hlw(img,W/2+w2/2,370,b,f2,fg)
def L_D(img,quote,attr):  # quote
    fg,acc,mut=col(img,(120,60,1060,460)); d=ImageDraw.Draw(img)
    d.text((1020,260),'”',font=DB(300),fill=TEAL,anchor='rs')
    lines=quote.split('|'); y=250
    for ln in lines:
        T(d,880,y,ln,DB(76),fg); y+=96
    T(d,880,y+10,'— '+attr,SB(34),acc)
def L_E(img,outline,l1,b):  # outlined giant word + headline
    fg,acc,mut=col(img,(60,60,1060,480)); d=ImageDraw.Draw(img)
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(lay)
    f=DB(230); ld.text((1030,300),outline,font=f,fill=(0,0,0,0),stroke_width=3,stroke_fill=fg+(170,),direction='rtl',anchor='rs')
    img.alpha_composite(lay); d=ImageDraw.Draw(img)
    T(d,1010,400,l1,DB(70),fg); hlw(img,1010,505,b,DB(86),fg)
P=[
 (1,'A',(1,'شـــاي','الساعة خمسة... وكاسة شاي'),('شاي','بالنعنع')),
 (2,'B',('حرّ؟','ليمـــون ونعنع','وبيروق الجو'),('ليمون','ونعنع فريش')),
 (3,'C',('أخضر وبارد...','موهيتـــو تفاح'),('موهيتو','تفاح أخضر')),
 (4,'D',('التوت|مش بس للصيف','فرابيه بلوبيري'),('فرابيه','بلوبيري')),
 (5,'E',('بلوبيري','قطعة على نغمة...','تشيز كيـــك'),('تشيز كيك','بلوبيري')),
 (6,'A',(6,'بستاشيـــو','ميلك شيك... للي بيفهم'),('ميلك شيك','بستاشيو')),
 (7,'B',('صوّر','لوتـــس','قبل ما يخلص'),('ميلك شيك','لوتس')),
 (8,'C',('صباح الموز...','ميلك شيـــك'),('ميلك شيك','موز')),
 (9,'D',('كلاسيكي...|متل أغنية قديمة','ميلك شيك فانيلا'),('ميلك شيك','فانيلا')),
 (10,'E',('موكا','الدنيا بتشتّي...','وإحنا آيس موكـــا'),('آيس','موكا')),
 (11,'A',(11,'كرامـــيل','آيس ماكياتو... طبقة فوق طبقة'),('آيس','كراميل ماكياتو')),
 (12,'B',('اكتب','قصتـــك','واللاتيه جنبك'),('لاتيه','ماكياتو')),
 (13,'C',('الشتا بلّش...','أمريكانـــو'),('أمريكانو','سخن')),
 (14,'D',('ما بنعرف نقاوم...|وإنت؟','براوني لوتس'),('براوني','لوتس')),
 (15,'E',('بستاشيو','قعدة ملوكية...','كيكـــة بستاشيو'),('كيكة','بستاشيو')),
 (16,'A',(16,'رول','بستاشيو وفواكه... بكل لقمة'),('رول','بستاشيو')),
 (17,'B',('زيد','الكرامـــيل','ما حدا شايف'),('فرابيه','كراميل')),
 (18,'C',('وردي...','ومنعـــش'),('موهيتو','توت')),
 (19,'D',('صيف|بكاسة','عصير استوائي'),('عصير','استوائي')),
 (20,'E',('BLU','الدوام طويل؟','اشحن حالك'),('BLU','مشروب طاقة')),
]
LAY={'A':L_A,'B':L_B,'C':L_C,'D':L_D,'E':L_E}
outs=[]
for n,L,args,lab in P:
    im=cover(Image.open(S+f'g20/g{n:02d}.png').convert('RGB')).convert('RGBA'); CUR[0]=im.copy()
    LAY[L](im,*args); auto_label(im,n,*lab); footer_c(im)
    im.convert('RGB').save(S+f'out/w{n:02d}.jpg',quality=95); outs.append(im)
sh=Image.new('RGB',(270*10,338*2))
for i,im in enumerate(outs): sh.paste(im.convert('RGB').resize((270,338)),((i%10)*270,(i//10)*338))
sh.save(S+'out/w_sheet.jpg'); print('ok')
