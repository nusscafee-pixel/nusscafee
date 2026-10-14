import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'post.py')).read())
W,H=1080,1920
R=S+'reel/'
def layer(): return Image.new('RGBA',(W,H),(0,0,0,0))
def scrim_top(im,y0,y1,a=150):
    m=Image.new('L',(W//4,H//4),0); d=ImageDraw.Draw(m); d.rounded_rectangle([60//4,y0//4,1060//4,y1//4],radius=10,fill=a)
    m=m.filter(ImageFilter.GaussianBlur(24)).resize((W,H)); im.alpha_composite(Image.merge('RGBA',(*Image.new('RGB',(W,H),(6,9,9)).split(),m)))
# clip1: two layers (line1, line2)
a=layer(); scrim_top(a,180,560); shadow_text(a,[(1010,380,'قنبلـــة',DB(150))]); text(ImageDraw.Draw(a),1010,380,'قنبلـــة',DB(150)); a.save(R+'o1a.png')
b=layer(); d=ImageDraw.Draw(b); hl(b,d,1010,540,'النُّص',DB(150),pad=(20,6),skew=10); d=ImageDraw.Draw(b); text(d,1010,540,'النُّص',DB(150)); b.save(R+'o1b.png')
# clip2
a=layer(); scrim_top(a,180,520); shadow_text(a,[(1010,370,'شو جوّاتهـــا؟',DB(120))]); text(ImageDraw.Draw(a),1010,370,'شو جوّاتهـــا؟',DB(120)); a.save(R+'o2a.png')
b=layer(); d=ImageDraw.Draw(b); f=DB(84)
w1=tw(d,'كريمـــة و',f)
hl(b,d,1010,490,'كريمـــة',f,pad=(12,3),skew=6); hl(b,d,1010-w1,490,'نوتيـــلا',f,pad=(12,3),skew=6)
d=ImageDraw.Draw(b); text(d,1010,490,'كريمـــة و',f); text(d,1010-w1,490,'نوتيـــلا',f); b.save(R+'o2b.png')
# clip3
a=layer(); scrim_top(a,180,560); shadow_text(a,[(1010,380,'تعال',DB(130))]); text(ImageDraw.Draw(a),1010,380,'تعال',DB(130)); a.save(R+'o3a.png')
b=layer(); d=ImageDraw.Draw(b); hl(b,d,1010,530,'فجّرهـــا عنّا',DB(130),pad=(18,5),skew=9); d=ImageDraw.Draw(b); text(d,1010,530,'فجّرهـــا عنّا',DB(130)); b.save(R+'o3b.png')
# end card overlay (over darkened last frame)
e=layer(); lg=Image.open(S+'logo.png'); lg=lg.resize((420,round(lg.height*420/lg.width)),Image.LANCZOS)
e.alpha_composite(lg,((W-420)//2,560))
d=ImageDraw.Draw(e); f=DB(70); t='قنبلـــة النُّص'; w=tw(d,t,f); text(d,(W+w)/2,1150,t,f)
f=SR(40); t='وصلت... وناطرتك'; w=tw(d,t,f); text(d,(W+w)/2,1230,t,f,fill=(215,225,222))
H=1700; footer(e,ImageDraw.Draw(e),logo=False); H=1920
e.save(R+'oend.png'); print('ok')

# Assemble: see the ffmpeg xfade/overlay command in the session notes (3 Kling 5s clips + end card, 16.7s, 1080x1920@30).
