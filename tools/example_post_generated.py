import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'post.py')).read())
src=Image.open(S+'gen/scene.png'  # Magnific output).convert('RGB')
img=cover(src,.5,.5,1.0)
# mood: slight darken + vignette + top/bottom fade
img=ImageEnhance.Brightness(img).enhance(.9)
g=Image.new('L',(1,H))
for y in range(H):
    t=max(0,1-y/(H*.30))**1.5*.55 + max(0,(y-H*.84)/(H*.16))**1.3*.75
    g.putpixel((0,y),int(255*min(1,t)))
img=Image.composite(Image.new('RGB',(W,H),(8,10,10)),img,g.resize((W,H)))
# translucent teal blocks like the reference
lay=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(lay)
for b in [(350,330,600,520),(790,640,1000,860),(0,820,170,990),(470,590,560,760)]:
    ld.rectangle(b,fill=(38,96,92,95))
img=img.convert('RGBA'); img.alpha_composite(lay)
d=ImageDraw.Draw(img); XR=1010; f=DB(80)
text(d,XR,135,'نـاعــم من بـرّا...',f)
wa=tw(d,'وقلبه ',f)
hl(img,d,XR-wa,238,'إسبريســـو',f,pad=(16,4),skew=8); d=ImageDraw.Draw(img)
text(d,XR,238,'وقلبه ',f); text(d,XR-wa,238,'إسبريســـو',f)
# label
lx=900; ly=1085
hl(img,d,lx,ly,'آيـــس',SB(40),pad=(8,2),skew=3); d=ImageDraw.Draw(img)
text(d,lx,ly,'آيـــس',SB(40)); text(d,lx,ly+42,'سبانش لاتيه',SR(30))
arrow(img,[(lx-120,ly-40),(lx-150,ly-70),(lx-200,ly-80),(lx-250,ly-60)])
footer(img,ImageDraw.Draw(img))
img.convert('RGB').save(S+'out/post3_spanish_latte_magnific.jpg',quality=95)
