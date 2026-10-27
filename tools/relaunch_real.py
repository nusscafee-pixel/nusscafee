import sys,json
src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pcombo.py').read()
exec(src[:src.index('C=[\n')])
O=S+'out/real/'; os.makedirs(O,exist_ok=True)
import builtins
_open=Image.open
def myopen(p,*a,**k):
    if isinstance(p,str) and p.endswith('scratchpad/logo.png'): p=S+'logo_white.png'
    return _open(p,*a,**k)
Image.open=myopen
for spec in json.load(open(S+'real/specs.json')):
    im0=Image.open(S+f"real/r{spec['id']}.png").convert('RGB')
    im0=im0.resize((W,round(im0.height*W/im0.width)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,90,2))
    base=cover(im0); im=topdark(base,spec.get('dark',520),spec.get('alpha',175)); CUR[0]=im.copy()
    head(im,spec['pill'],spec['l1'],spec['l2'])
    for lab in spec.get('labs',[]): mlabel(im,*lab)
    footer_c(im); im.convert('RGB').save(O+spec['name']+'.jpg',quality=95)
names=[s['name'] for s in json.load(open(S+'real/specs.json'))]
sh=Image.new('RGB',(3*400+20,((len(names)+2)//3)*510),(30,30,30))
for k,n in enumerate(names): sh.paste(_open(O+n+'.jpg').resize((400,500)),((k%3)*410,(k//3)*510))
sh.save(O+'preview.jpg'); print('ok')
