src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pcombo.py').read()
exec(src[:src.index('C=[\n')])
_open=Image.open
def myopen(p,*a,**k):
    if isinstance(p,str) and p.endswith('scratchpad/logo.png'): p=S+'logo_white.png'
    return _open(p,*a,**k)
Image.open=myopen
O=S+'out/vary/'; os.makedirs(O,exist_ok=True)
def prep(i,dark=520,alpha=180):
    im0=Image.open(S+f'real/r{i}.png').convert('RGB')
    im0=im0.resize((W,round(im0.height*W/im0.width)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,90,2))
    im=topdark(cover(im0),dark,alpha); CUR[0]=im.copy(); return im
P=[]
im=prep(71,640,190); L_D(im,'الشتا|بدّه ضو ودفـــا','نُص كافيه'); footer_c(im); P.append(('V1',im,'الشتا بدّه ضو دافي… وكاسة أدفى 🕯️☕','#شتوية_النص'))
im=prep(47,560,190); L_C(im,'قعدة المســـا...','بين الأضـــواء'); footer_c(im); P.append(('V2',im,'قعدة المسا بين الأضواء… فاتحين لحد الساعة 10 ✨','#نص_كافيه_بالليل'))
im=prep(68,620,200); L_B(im,'بـــرد؟','الكنبايـــة','محجوزة إلك'); footer_c(im); P.append(('V3',im,'برد؟ الكنباية محجوزة… بس إلك 🛋️ وهوت شوكليت 14 شيكل جنبك','#شتوية_النص'))
im=prep(52,640,235); L_A(im,7,'دلـــع','الشتا بدّه شوكولا سخنة'); footer_c(im); P.append(('V4',im,'الشتا بدّه شوكولا سخنة… ونُص ما بيقصّر 🍫','#حلويات_النص'))
im=prep(65,600,190); L_E(im,'كريب','الجو بارد...','والكريب سخـــن'); mlabel(im,420,760,'كريب','22 شيكل · دبي 29',[(380,800),(420,860),(500,900)]); footer_c(im); P.append(('V5',im,'الجو بارد… والكريب سخن. كريب 22، مكس 24، ودبي 29 🔥','#كريب'))
for n,im,_,_ in P: im.convert('RGB').save(O+n+'.jpg',quality=95)
sh=Image.new('RGB',(5*360+40,450),(30,30,30))
for k,(n,_,_,_) in enumerate(P): sh.paste(_open(O+n+'.jpg').resize((360,450)),(k*370,0))
sh.save(O+'preview.jpg')
import json; json.dump([(n,c,t) for n,_,c,t in P],open(O+'caps.json','w'),ensure_ascii=False); print('ok')
