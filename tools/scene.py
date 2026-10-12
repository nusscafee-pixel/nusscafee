import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'post.py')).read())
import random
def radial(size,center,radius,inner,outer):
    w,h=size; m=Image.new('L',(w//4,h//4),0); d=ImageDraw.Draw(m)
    cx,cy=center[0]/4,center[1]/4; r=radius/4
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=255); m=m.filter(ImageFilter.GaussianBlur(r*.6)).resize(size,Image.LANCZOS)
    return Image.composite(Image.new('RGB',size,inner),Image.new('RGB',size,outer),m)

def frond(d,base,angle,length,curl=.35,leaves=26,lw=70,seed=0):
    rnd=random.Random(seed); pts=[]
    for i in range(leaves+1):
        t=i/leaves; a=angle+curl*t
        if i==0: x,y=base
        else:
            x=pts[-1][0]+math.cos(a)*length/leaves; y=pts[-1][1]+math.sin(a)*length/leaves
        pts.append((x,y))
    d.line(pts,fill=255,width=6)
    for i,(x,y) in enumerate(pts[2:],2):
        t=i/leaves; a=angle+curl*t; L=lw*(1-abs(t-.45))*rnd.uniform(.85,1.1)
        for s in (1,-1):
            la=a+s*1.0+rnd.uniform(-.1,.1)
            tip=(x+math.cos(la)*L,y+math.sin(la)*L)
            n=(math.cos(a)*7,math.sin(a)*7)
            d.polygon([(x,y),(x+n[0]+math.cos(la)*L*.5,y+n[1]+math.sin(la)*L*.5),tip,(x+math.cos(la)*L*.5,y+math.sin(la)*L*.5)],fill=255)

def leaf_shadow(specs,blur=10):
    m=Image.new('L',(W,H),0); d=ImageDraw.Draw(m)
    for sp in specs: frond(d,**sp)
    return m.filter(ImageFilter.GaussianBlur(blur))

def scene(arch_x=None,table_y=1010,wall=(44,48,47),light=(120,112,100),light_c=(560,640),shadows=None):
    img=radial((W,H),light_c,620,light,wall)
    # leaf shadows
    sh=leaf_shadow(shadows or [
        dict(base=(-40,40),angle=.35,length=620,curl=.5,seed=1),
        dict(base=(-60,260),angle=-.05,length=520,curl=.6,seed=2,lw=60),
        dict(base=(1120,-30),angle=2.45,length=560,curl=-.45,seed=3),
        dict(base=(1130,330),angle=3.0,length=420,curl=-.5,seed=4,lw=55)],blur=5)
    dark=ImageEnhance.Brightness(img).enhance(.38)
    img=Image.composite(dark,img,sh.point(lambda v:int(v*.95)))
    d=ImageDraw.Draw(img)
    if arch_x is not None:
        aw,ah=300,640; x0=arch_x; y1=table_y; y0=y1-ah
        lay=Image.new('L',(W,H),0); ld=ImageDraw.Draw(lay)
        ld.rectangle([x0,y0+aw//2,x0+aw,y1],fill=255); ld.ellipse([x0,y0,x0+aw,y0+aw],fill=255)
        archc=radial((W,H),(x0+aw*.6,y0+aw*.6),aw*.9,(32,34,33),(16,17,17))
        img=Image.composite(archc,img,lay)
        # inner edge highlight
        edge=lay.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(1.2))
        img=Image.composite(Image.new('RGB',(W,H),(90,90,86)),img,edge.point(lambda v:min(255,v*2)//3))
    # table
    tab=Image.new('RGB',(W,H-table_y)); td=ImageDraw.Draw(tab)
    for y in range(H-table_y):
        t=y/(H-table_y); c=tuple(int(a*(1-t)+b*t) for a,b in zip((30,78,73),(8,24,23)))
        td.line([(0,y),(W,y)],fill=c)
    tab=Image.composite(radial(tab.size,(light_c[0],0),520,(48,108,100),(14,40,38)),tab,Image.new('L',tab.size,110))
    img.paste(tab,(0,table_y))
    d=ImageDraw.Draw(img); d.line([(0,table_y),(W,table_y)],fill=(80,140,132),width=2)
    return img

def put(img,cut,cx,base_y,height,table_y,warm=.92):
    a0=cut.getchannel('A').point(lambda v:255 if v>140 else 0); c=cut.crop(a0.getbbox()); c.putalpha(ImageChops.multiply(c.getchannel('A'),c.getchannel('A').point(lambda v:255 if v>40 else 0))); s=height/c.height; c=c.resize((round(c.width*s),height),Image.LANCZOS)
    rgb=ImageEnhance.Brightness(c.convert('RGB')).enhance(warm); c=Image.merge('RGBA',(*rgb.split(),c.getchannel('A')))
    x=int(cx-c.width/2); y=base_y-height
    img=img.convert('RGBA')
    # contact + cast shadow
    sh=Image.new('L',(W,H),0); sd=ImageDraw.Draw(sh)
    sd.ellipse([x+c.width*.08,base_y-14,x+c.width*.92,base_y+16],fill=230)
    sd.polygon([(x+c.width*.15,base_y),(x+c.width*.85,base_y),(x-c.width*.55,base_y-40),(x-c.width*.9,base_y-30)],fill=110)
    sh=sh.filter(ImageFilter.GaussianBlur(14))
    img.alpha_composite(Image.merge('RGBA',(*Image.new('RGB',(W,H),(5,10,10)).split(),sh)))
    # reflection
    ref=c.transpose(Image.FLIP_TOP_BOTTOM).crop((0,0,c.width,int(height*.35)))
    a=ref.getchannel('A'); g=Image.linear_gradient('L').resize(ref.size).point(lambda v:int((255-v)*.22))
    ref.putalpha(ImageChops.multiply(a,g)); img.alpha_composite(ref,(x,base_y-4))
    img.alpha_composite(c,(x,y)); return img
