src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pplace.py').read()
exec(src[:src.index("b=place('win/c04.png'")])
R=S+'reel2/'; VW,VH=1080,1920
def fit(im,w,h):
    s=max(w/im.width,h/im.height); im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=(im.width-w)//2; y=(im.height-h)//2; return im.crop((x,y,x+w,y+h))
def load(p):
    im=_open(S+p).convert('RGB')
    if im.width<900: im=im.resize((1080,round(im.height*1080/im.width)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,90,2))
    return im
scenes=[]
scenes.append((load('real/r71.png'),'الشتا وصـــل...',None))
scenes.append((load('who2/g02.png'),'المطر بـــرّا...','واللاتيه جـــوّا'))
scenes.append((load('who2/g01.png'),'البردان الدايـــم؟','هوت شوكليـــت'))
scenes.append((place('win/c04.png','cuts/rnut.png',490,1095,740),'نوتيلا مثلّجـــة...','جامدة متل قلب حـــدا'))
scenes.append((place('win/c01_full.png','cuts/rcrepe.png',520,1075,760),'الجو بـــارد...','والكريب سخـــن'))
scenes.append((load('real/r68.png'),'بـــرد؟','الكنباية محجوزة إلك'))
for k,(im,l1,l2) in enumerate(scenes):
    bg=fit(im,int(VW*1.12),int(VH*1.12)); bg.save(R+f'bg{k}.png')
    ov=Image.new('RGBA',(VW,VH),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(760): d.line([(0,y),(VW,y)],fill=(8,12,11,int(200*(1-y/760)**1.3)))
    d=ImageDraw.Draw(ov); XR=1010
    if l2:
        d.text((XR,330),l1,font=DB(78),fill=WHITE,direction='rtl',anchor='rs')
        f2=DB(104)
        while tw(d,l2,f2)>940: f2=DB(f2.size-4)
        hl(ov,d,XR,470,l2,f2,pad=(18,5),skew=9); d=ImageDraw.Draw(ov); d.text((XR,470),l2,font=f2,fill=WHITE,direction='rtl',anchor='rs')
    else:
        f=DB(120); hl(ov,d,XR,420,l1,f,pad=(18,5),skew=9); d=ImageDraw.Draw(ov); d.text((XR,420),l1,font=f,fill=WHITE,direction='rtl',anchor='rs')
    lg=_open(S+'logo_white.png'); lg=lg.resize((130,round(lg.height*130/lg.width)),Image.LANCZOS); ov.alpha_composite(lg,(VW-60-130,VH-260))
    ov.save(R+f'tx{k}.png')
# endcard
ec=Image.new('RGBA',(VW,VH),(12,20,19,255)); d=ImageDraw.Draw(ec)
lg=_open(S+'logo_white.png'); lg=lg.resize((420,round(lg.height*420/lg.width)),Image.LANCZOS); ec.alpha_composite(lg,((VW-420)//2,420))
d.text((VW/2,1060),'نُصّك المفقـــود',font=DB(96),fill=WHITE,direction='rtl',anchor='ms')
hl(ec,d,VW/2+tw(d,'دافي هالشتا',DB(80))/2,1200,'دافي هالشتا',DB(80),pad=(18,5),skew=9); d=ImageDraw.Draw(ec)
d.text((VW/2,1200),'دافي هالشتا',font=DB(80),fill=WHITE,direction='rtl',anchor='ms')
d.text((VW/2,1360),'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',font=SR(36),fill=(200,214,210),direction='rtl',anchor='ms')
d.text((VW/2,1430),'السبت – الخميس 10 – 10  ·  الجمعة 3 – 10',font=SB(36),fill=(200,214,210),direction='rtl',anchor='ms')
ec.convert('RGB').save(R+'end.png'); print(len(scenes))
