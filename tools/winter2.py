src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pcombo.py').read()
exec(src[:src.index('C=[\n')])
O=S+'out/winter2/'; os.makedirs(O,exist_ok=True)
_open=Image.open
def myopen(p,*a,**k):
    if isinstance(p,str) and p.endswith('scratchpad/logo.png'): p=S+'logo_white.png'
    return _open(p,*a,**k)
Image.open=myopen
BB={}
def bbox(n): return BB[n]
P=[
 ('who2/g01.png',(372,784,759,1051),'الشتا عنّا','البردان الدايـــم...','هوت شوكليت بيحميـــك',('هوت شوكليت','14 شيكل · بطانية بكاسة'),
  'البردان الدايم؟ هوت شوكليت 14 شيكل… بطانية بس بكاسة 🧣🍫','#هوت_شوكليت'),
 ('who2/g02.png',(306,622,590,1136),'الشتا عنّا','المطر بـــرّا...','واللاتيه جـــوّا',('لاتيه سخن','14 شيكل · بيهدّي الدراما'),
  'المطر برّا… واللاتيه جوّا. لاتيه 14 شيكل بيقنعك إنه اليوم بيمرق بلا دراما ☔☕','#لاتيه'),
 ('who2/g05.png',(417,707,691,1213),'جلد ذات شتوي','"أنا مش بـــردان"','قالها وهو بيرجـــف',('آيس أمريكانو','20 شيكل · حتى بعز الشتا'),
  'في ناس بتشرب آيس أمريكانو بعز الشتا… وبتقول "عادي" 😂🧊 20 شيكل','#آيس_أمريكانو'),
 ('win/c03.png',(400,661,760,958),'الشتا عنّا','ستّك قالت: البـــس منيح','وإحنا بنقول: شـــاي',('شاي','8 شيكل · فاهم اللعبة'),
  'ستّك قالت البس منيح… وإحنا بنقول اشرب شاي 🍵 8 شيكل بس','#شاي'),
 ('win/c04.png',(324,796,700,1053),'جلد ذات شتوي','الريجيـــم؟','خلّيه لبعد الشتـــا',('براوني','25 شيكل · 3 نكهات'),
  'الريجيم مأجّل لبعد الشتا… رسمي 😏 براوني 25 شيكل','#براوني'),
 ('launch/t2.png',None,'الشتا عنّا','برّا بـــرد...','وجوّا دفا ونُـــص',None,
  'برّا برد… وجوّا دفا ونُص. الباب مفتوح من 10 الصبح لـ10 المسا 🧥☕','#شتوية_النص'),
]
caps=[]
for k,(src_,bb,pill,l1,l2,lab,cap,tag) in enumerate(P):
    im0=Image.open(S+src_).convert('RGB')
    base=cover(im0); im=topdark(base,520,180); CUR[0]=im.copy()
    head(im,pill,l1,l2)
    if lab:
        if src_.startswith('who2'):
            x0,y0,x1,y1=bb; BB[k]=bb
        else: BB[k]=bb
        M={0:(430,650,[(380,690),(410,750),(470,800)]),2:(390,640,[(340,680),(370,730),(430,770)]),
           3:(430,1160,[(380,1120),(400,1060),(440,1010)]),4:(1010,830,[(870,800),(800,820),(720,880)])}
        if k in M: mlabel(im,M[k][0],M[k][1],lab[0],lab[1],M[k][2])
        else: auto_label(im,k,*lab)
    footer_c(im); n=f'W{k+1}'; im.convert('RGB').save(O+n+'.jpg',quality=95); caps.append((n,cap,tag))
sh=Image.new('RGB',(3*400+20,2*510),(30,30,30))
for k,(n,_,_) in enumerate(caps): sh.paste(_open(O+n+'.jpg').resize((400,500)),((k%3)*410,(k//3)*510))
sh.save(O+'preview.jpg')
import json; json.dump(caps,open(O+'caps.json','w'),ensure_ascii=False); print('ok')
