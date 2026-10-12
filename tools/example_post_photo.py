import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'post.py')).read())
src=Image.open(S+'products/jGIkNbrVUmvSNkr5VlWIiWA3U2iG2TpH9KvQChBG.jpg').convert('RGB')
img=place(src,.74,.47,-95)
img=grade(img,focus=(.45,.62),fr=.30).convert('RGBA')
d=ImageDraw.Draw(img)
XR=1000; f=DB(86)
l1='مش مُـــــــرّ...'; l2_a='هو بس '; l2_b='صريـــــح'
text(d,XR,205,l1,f)
wa=tw(d,l2_a,f)
hl(img,d,XR-wa,318,l2_b,f,pad=(16,4),skew=8); d=ImageDraw.Draw(img)
text(d,XR,318,l2_a,f); text(d,XR-wa,318,l2_b,f)
# product label (left), arrow from label toward glass
lx=255; ly=690
hl(img,d,lx,ly,'آيـــس',SB(42),pad=(8,2),skew=3); d=ImageDraw.Draw(img)
text(d,lx,ly,'آيـــس',SB(42)); text(d,lx,ly+44,'أمريكانو',SR(30))
arrow(img,[(lx-30,ly-60),(lx+20,ly-105),(lx+90,ly-112),(lx+150,ly-70)])
footer(img,ImageDraw.Draw(img))
img.convert('RGB').save(S+'out/post1_ice_americano.jpg',quality=95)
