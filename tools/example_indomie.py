import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'post.py')).read())
def compose(n,dy=0,zoom=1.0,bright=.33):
    im=cover(Image.open(S+f'indomie/i{n}.png').convert('RGB')); m=Image.open(S+f'indomie/m{n}.png').convert('L')
    m=m.point(lambda v:min(255,int(v*1.4)))
    bg=im.filter(ImageFilter.GaussianBlur(26)); bg=ImageEnhance.Brightness(bg).enhance(bright)
    bg=Image.blend(bg,Image.new('RGB',(W,H),(10,24,23)),.25)
    sharp=Image.composite(im,bg,m)
    if zoom!=1.0 or dy:
        s=sharp.resize((round(W*zoom),round(H*zoom)),Image.LANCZOS); mm=m.resize(s.size)
        base=bg.resize((round(W*1.15),round(H*1.15))).crop((round(W*.075),round(H*.075),round(W*.075)+W,round(H*.075)+H))
        x=(W-s.width)//2; base.paste(s,(x,dy),mm.point(lambda v:255 if v>0 else 0).filter(ImageFilter.GaussianBlur(3)) if False else None) if False else None
        canvas=bg.copy(); canvas.paste(s,(x,dy)); 
        # blend seam: fade top of pasted region
        fm=Image.new('L',s.size,255); fd=ImageDraw.Draw(fm)
        for i in range(120): fd.line([(0,i),(s.width,i)],fill=int(255*i/120))
        canvas=bg.copy(); canvas.paste(s,(x,dy),fm); sharp=canvas
    # vignette
    v=Image.new('L',(W//4,H//4),0); vd=ImageDraw.Draw(v); vd.ellipse([-40,40,W//4+40,H//4+40],fill=255)
    v=v.filter(ImageFilter.GaussianBlur(40)).resize((W,H))
    sharp=Image.composite(sharp,ImageEnhance.Brightness(sharp).enhance(.55),v)
    return sharp.convert('RGBA')
def pill(img,XR,y,t='جديد عنّا'):
    d=ImageDraw.Draw(img); f=SB(32); w=tw(d,t,f)
    d.rounded_rectangle([XR-w-48,y,XR,y+58],radius=29,fill=(47,112,104)); d.text((XR-24,y+42),t,font=f,fill=WHITE,direction='rtl',anchor='rs')
def head(img,l1,a,b,XR=1010,y=270,f=None,gap=108):
    f=f or DB(84); d=ImageDraw.Draw(img); wa=tw(d,a,f) if a else 0
    hl(img,d,XR-wa,y+gap,b,f,pad=(16,4),skew=8); d=ImageDraw.Draw(img)
    text(d,XR,y,l1,f)
    if a: text(d,XR,y+gap,a,f)
    text(d,XR-wa,y+gap,b,f)
def lab(img,lx,ly,bo,su,arr):
    d=ImageDraw.Draw(img); hl(img,d,lx,ly,bo,SB(40),pad=(8,2),skew=3); d=ImageDraw.Draw(img)
    text(d,lx,ly,bo,SB(40)); text(d,lx,ly+42,su,SR(30)); arrow(img,arr)
out=[]
im=compose(1); pill(im,1010,100); head(im,'برّا بتشتّي...','وجوّا ','إندومـــي')
lab(im,1000,690,'إندومـــي','مع بيضة وبهار',[(860,700),(800,720),(740,760),(700,800)])
footer(im,ImageDraw.Draw(im)); out.append(im)
im=compose(2); pill(im,1010,100); head(im,'الطعم اللي كبرنا عليه...','صار ','عنّـــا',f=DB(78))
lab(im,330,860,'إندومـــي','سخنة ومن النار',[(345,820),(390,790),(440,800),(468,830)])
footer(im,ImageDraw.Draw(im)); out.append(im)
im=compose(3,dy=260,zoom=1.0); pill(im,1010,90); head(im,'بردانين؟','دفّوا حالكم ','بإندومـــي',y=250,f=DB(80),gap=104)
lab(im,300,700,'إندومي','سخنة وبتدفّي',[(240,760),(270,840),(350,900),(425,925)])
g=Image.new('L',(1,H))
for y in range(H): g.putpixel((0,y),int(255*min(1,max(0,(y-H*.86)/(H*.14))**1.2*.55)))
im.alpha_composite(Image.merge('RGBA',(*Image.new('RGB',(W,H),(8,10,10)).split(),g.resize((W,H)))))
footer(im,ImageDraw.Draw(im)); out.append(im)
for i,im in enumerate(out): im.convert('RGB').save(S+f'out/indomie_{i+1}.jpg',quality=95)
sh=Image.new('RGB',(540*3,675))
for i,im in enumerate(out): sh.paste(im.convert('RGB').resize((540,675)),(i*540,0))
sh.save(S+'out/indomie_sheet.jpg'); print('ok')
