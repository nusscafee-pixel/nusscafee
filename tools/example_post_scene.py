import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'scene.py')).read())
TY=1030
img=scene(arch_x=90,table_y=TY,light_c=(620,640),light=(150,138,120),wall=(34,37,36))
cut=Image.open(S+'cut61c.png')
img=put(img,cut,610,TY+120,640,TY)
# vignette + grain
v=radial((W,H),(560,640),820,(255,255,255),(70,70,70)); img=ImageChops.multiply(img.convert('RGB'),v)
n=Image.effect_noise((W,H),16).convert('RGB'); img=Image.blend(img,ImageChops.overlay(img,n),.15).convert('RGBA')
# logo inside arch
lg=Image.open(S+'logo.png'); lg=lg.resize((150,round(lg.height*150/lg.width)),Image.LANCZOS); img.alpha_composite(lg,(90+150-75,TY-640+170))
d=ImageDraw.Draw(img); XR=1000; f=DB(78)
text(d,XR,170,'نـاعــم من بـرّا...',f)
wa=tw(d,'وقلبه ',f)
hl(img,d,XR-wa,275,'إسبريســـو',f,pad=(16,4),skew=8); d=ImageDraw.Draw(img)
text(d,XR,275,'وقلبه ',f); text(d,XR-wa,275,'إسبريســـو',f)
lx=1000; ly=600
hl(img,d,lx,ly,'آيـــس',SB(42),pad=(8,2),skew=3); d=ImageDraw.Draw(img)
text(d,lx,ly,'آيـــس',SB(42)); text(d,lx,ly+42,'سبانش لاتيه',SR(30))
arrow(img,[(lx-60,ly+80),(lx-90,ly+140),(lx-170,ly+170),(lx-230,ly+160)])
footer(img,ImageDraw.Draw(img),logo=False)
img.convert('RGB').save(S+'out/post2_spanish_latte.jpg',quality=95)
