src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pcombo.py').read()
exec(src[:src.index('C=[\n')])
_open=Image.open
def myopen(p,*a,**k):
    if isinstance(p,str) and p.endswith('scratchpad/logo.png'): p=S+'logo_white.png'
    return _open(p,*a,**k)
Image.open=myopen
def mlabel(img,lx,ly,bold,sub,pts):
    d=ImageDraw.Draw(img); fb=SB(40); fs=SR(30)
    hl(img,d,lx,ly,bold,fb,pad=(8,2),skew=3); d=ImageDraw.Draw(img)
    d.text((lx,ly),bold,font=fb,fill=WHITE,direction='rtl',anchor='rs'); T(d,lx,ly+42,sub,fs,WHITE)
    b=(min(p[0] for p in pts),min(p[1] for p in pts),max(p[0] for p in pts),max(p[1] for p in pts))
    arrow_c(img,pts,DARK if lum(img,b)>150 else WHITE)
O=S+'out/vary/'; os.makedirs(O,exist_ok=True)
def prep(i,dark=520,alpha=180):
    im0=Image.open(S+f'real/r{i}.png').convert('RGB')
    if im0.width<900: im0=im0.resize((W,round(im0.height*W/im0.width)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,90,2))
    im=topdark(cover(im0),dark,alpha); CUR[0]=im.copy(); return im
P=[]
im=prep(71,640,190); L_D(im,'الشتا|بدّه ضو ودفـــا','نُص كافيه'); footer_c(im); P.append(('V1',im,'الشتا بدّه ضو دافي… وكاسة أدفى 🕯️☕','#شتوية_النص'))
im=prep(47,560,190); L_C(im,'قعدة المســـا...','بين الأضـــواء'); footer_c(im); P.append(('V2',im,'قعدة المسا بين الأضواء… فاتحين لحد الساعة 10 ✨','#نص_كافيه_بالليل'))
im=prep(68,620,200); L_B(im,'بـــرد؟','الكنبايـــة','محجوزة إلك'); footer_c(im); P.append(('V3',im,'برد؟ الكنباية محجوزة… بس إلك 🛋️ وهوت شوكليت 14 شيكل جنبك','#شتوية_النص'))
im=prep('nut',560,200); L_A(im,7,'نوتيـــلا','جامدة متل قلب اللي عمل سين وما ردّ'); mlabel(im,1010,880,'كيك نوتيلا','22 شيكل · مثلّجة',[(870,920),(760,960),(640,1000)]); footer_c(im); P.append(('V4',im,'كيك نوتيلا مثلّجة… جامدة متل قلب اللي عمل سين زرقا وما ردّ 💔 22 شيكل','#كيك_نوتيلا'))
im=prep('crepe',560,200); L_E(im,'كريب','الجو بارد...','والكريب سخـــن'); mlabel(im,430,420,'كريب','22 شيكل · دبي 29',[(390,470),(430,540),(520,600)]); footer_c(im); P.append(('V5',im,'الجو بارد… والكريب سخن. كريب 22، مكس 24، ودبي 29 🔥','#كريب'))
for n,im,_,_ in P: im.convert('RGB').save(O+n+'.jpg',quality=95)
sh=Image.new('RGB',(5*360+40,450),(30,30,30))
for k,(n,_,_,_) in enumerate(P): sh.paste(_open(O+n+'.jpg').resize((360,450)),(k*370,0))
sh.save(O+'preview.jpg')
import json; json.dump([(n,c,t) for n,_,c,t in P],open(O+'caps.json','w'),ensure_ascii=False); print('ok')
