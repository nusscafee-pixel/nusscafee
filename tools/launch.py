import sys,json
src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pcombo.py').read()
exec(src[:src.index('C=[\n')])
O=S+'out/launch/'; os.makedirs(O,exist_ok=True)
spec=json.loads(sys.argv[1])
base=cover(Image.open(S+'launch/'+spec['src']).convert('RGB')); im=topdark(base,520,175); CUR[0]=im.copy()
head(im,spec['pill'],spec['l1'],spec['l2'])
for lab in spec.get('labs',[]): mlabel(im,*lab)
if spec.get('sub'):
    d=ImageDraw.Draw(im); T(d,1010,420,spec['sub'],SR(34),WHITE)
footer_c(im); im.convert('RGB').save(O+spec['name']+'.jpg',quality=95); print('ok')
