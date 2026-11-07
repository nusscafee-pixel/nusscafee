src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pvary.py').read()
exec(src[:src.index("O=S+'out/vary/'")])
from PIL import ImageEnhance
O=S+'out/place/'; os.makedirs(O,exist_ok=True)
def place(bgp,cutp,cx,bottom,w,bright=.82,warm=1.06):
    bg=cover(Image.open(S+bgp).convert('RGB')).convert('RGBA')
    c=Image.open(S+cutp).convert('RGBA'); c=c.resize((w,round(c.height*w/c.width)),Image.LANCZOS)
    rgb=ImageEnhance.Brightness(c.convert('RGB')).enhance(bright)
    r,g,b=rgb.split(); r=r.point(lambda v:min(255,int(v*warm))); b=b.point(lambda v:int(v*0.95)); rgb=Image.merge('RGB',(r,g,b))
    c2=rgb.convert('RGBA'); c2.putalpha(c.getchannel('A'))
    x=int(cx-w/2); y=int(bottom-c.height)
    sh=Image.new('RGBA',bg.size,(0,0,0,0)); ImageDraw.Draw(sh).ellipse([x+w*.06,bottom-c.height*.28,x+w*.96,bottom+c.height*.06],fill=(0,0,0,170))
    bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(26))); bg.alpha_composite(c2,(x,y))
    return bg.convert('RGB')
def finish(base,pill,l1,l2,lab,name):
    im=topdark(base,520,180); CUR[0]=im.copy(); head(im,pill,l1,l2)
    mlabel(im,*lab); footer_c(im); im.convert('RGB').save(O+name+'.jpg',quality=95)
b=place('win/c04.png','cuts/rnut.png',490,1095,740)
finish(b,'جلد ذات شتوي','نوتيلا مثلّجـــة...','جامدة متل قلب حـــدا',(1010,800,'كيك نوتيلا','22 شيكل · مثلّجة',[(870,830),(760,830),(640,850)]),'P1_nutella')
b=place('win/c01.png','cuts/rcrepe.png',520,1150,700)
finish(b,'الشتا عنّا','الجو بـــارد...','والكريب سخـــن',(1010,760,'كريب','22 شيكل · دبي 29',[(870,800),(790,840),(700,880)]),'P2_crepe')
from PIL import Image as I2
a=_open(O+'P1_nutella.jpg').resize((540,675)); bb=_open(O+'P2_crepe.jpg').resize((540,675)); s=I2.new('RGB',(1080,675)); s.paste(a,(0,0)); s.paste(bb,(540,0)); s.save(O+'preview.jpg'); print('ok')
