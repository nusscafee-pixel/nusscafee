import os,math,shutil
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageEnhance
S='/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/'; RP='/home/user/nusscafee/'
VW,VH=1080,1920; FPS=30
TEAL=(47,112,104); WHITE=(245,243,238); CREAM=(244,238,226); GOLD=(216,190,128); MUT=(200,212,208); INK=(12,18,17)
RQ=ImageFont.Layout.RAQM
def F(w,s): return ImageFont.truetype(S+f'fonts/thmanyahsans-{w}.otf',s,layout_engine=RQ)
def tw(d,t,f): b=d.textbbox((0,0),t,font=f,direction='rtl',anchor='rs'); return b[2]-b[0]
def R(d,x,y,t,f,fill=WHITE,anchor='rs'): d.text((x,y),t,font=f,fill=fill,direction='rtl',anchor=anchor)
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def eio(t): t=max(0,min(1,t)); return t*t*(3-2*t)
def back(t):
    t=max(0,min(1,t)); c=1.70158; return 1+(c+1)*(t-1)**3+c*(t-1)**2
FD=S+'lm3/f/'; shutil.rmtree(FD,ignore_errors=True); os.makedirs(FD)
LG=Image.open(RP+'brand/logo_official_white.png').convert('RGBA')
QR=Image.open(S+'qr_card.png').convert('RGBA')
def cover(im,w,h):
    s=max(w/im.width,h/im.height); im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=(im.width-w)//2; y=(im.height-h)//2; return im.crop((x,y,x+w,y+h))
def grade(im,dark=0.75):
    im=ImageEnhance.Color(im).enhance(.9)
    ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(im.height):
        t=y/im.height; a=int(255*(0.62 if t<.32 else 0.22+0.0*t) if t<.7 else 255*(0.22+0.55*(t-.7)/.3))
        d.line([(0,y),(im.width,y)],fill=(8,12,11,a))
    o=im.convert('RGBA'); o.alpha_composite(ov); return o
BGS={}
def bg(name,k,zoom=(1.0,1.12),pan=0):
    if name not in BGS:
        p=RP+('brand/owner_scenes/' if name.startswith('o') else 'brand/real_photos/')+name+'.png'
        im=Image.open(p).convert('RGB'); BGS[name]=grade(cover(im,int(VW*1.18),int(VH*1.18)))
    big=BGS[name]; z=zoom[0]+(zoom[1]-zoom[0])*eio(k)
    w,h=int(VW*1.18/z*1.0),int(VH*1.18/z*1.0); w=min(w,big.width); h=min(h,big.height)
    cx=big.width/2+pan*(k-.5)*80; cy=big.height/2
    c=big.crop((int(cx-w/2),int(cy-h/2),int(cx+w/2),int(cy+h/2))).resize((VW,VH),Image.LANCZOS); return c
def hlblock(img,xr,y,t,f,skew=9):
    d=ImageDraw.Draw(img); b=d.textbbox((xr,y),t,font=f,direction='rtl',anchor='rs'); h=b[3]-b[1]
    x0,x1=b[0]-22,b[2]+22; y0=b[1]+h*.12; y1=b[3]+h*.22
    lay=Image.new('RGBA',img.size,(0,0,0,0)); ImageDraw.Draw(lay).polygon([(x0,y0+skew),(x1,y0-skew/2),(x1,y1),(x0,y1+skew/2)],fill=TEAL+(240,)); img.alpha_composite(lay)
def caption(img,l1,l2,k,y1=330,y2=470):
    if k<=0: return
    lay=Image.new('RGBA',(VW,VH),(0,0,0,0)); d=ImageDraw.Draw(lay)
    if l1:
        f1=F('Bold',66)
        while tw(d,l1,f1)>960: f1=F('Bold',f1.size-4)
        w=tw(d,l1,f1); R(d,VW/2+w/2,y1,l1,f1)
    if l2:
        f2=F('Black',88)
        while tw(d,l2,f2)>940: f2=F('Black',f2.size-4)
        w=tw(d,l2,f2); hlblock(lay,VW/2+w/2,y2,l2,f2); d=ImageDraw.Draw(lay); R(d,VW/2+w/2,y2,l2,f2)
    a=ease(k); lay.putalpha(lay.getchannel('A').point(lambda v:int(v*a))); img.alpha_composite(lay,(0,int(26*(1-a))))
def cupicon(d,cx,cy,r,filled):
    col=CREAM if filled else (120,170,162)
    if filled: d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(40,128,118,255),outline=(120,190,180),width=2)
    w=r; h=r*.75
    d.rounded_rectangle([cx-w/2,cy-h/2+4,cx+w/2-6,cy+h/2+4],radius=8,fill=col if filled else None,outline=col,width=4)
    d.arc([cx+w/2-18,cy-h/4+2,cx+w/2+8,cy+h/4+8],-90,90,fill=col,width=4); d.line([(cx-w/2-6,cy+h/2+12),(cx+w/2,cy+h/2+12)],fill=col,width=4)
def star(d,cx,cy,r,col):
    d.polygon([(cx+r*math.cos(math.pi/2+k*math.pi/5)*(1 if k%2==0 else .42),cy-r*math.sin(math.pi/2+k*math.pi/5)*(1 if k%2==0 else .42)) for k in range(10)],fill=col)
CARDS={}
def card(st,won=False):
    key=(st,won)
    if key in CARDS: return CARDS[key]
    W0=900; H0=567; c=Image.new('RGBA',(W0,H0),(0,0,0,0))
    m=Image.new('L',(W0,H0),0); ImageDraw.Draw(m).rounded_rectangle([0,0,W0-1,H0-1],radius=40,fill=255)
    g=Image.new('RGBA',(W0,H0)); gd=ImageDraw.Draw(g)
    for y in range(H0): t=y/H0; gd.line([(0,y),(W0,y)],fill=(int(47-20*t),int(112-40*t),int(104-38*t),255))
    gl=Image.new('RGBA',(W0,H0),(0,0,0,0)); ImageDraw.Draw(gl).ellipse([-W0*.3,-H0*.9,W0*.9,H0*.45],fill=(255,255,255,26)); g.alpha_composite(gl)
    c.paste(g,(0,0),m); d=ImageDraw.Draw(c)
    d.rounded_rectangle([12,12,W0-13,H0-13],radius=32,outline=GOLD+(160,),width=2)
    l=LG.resize((120,round(LG.height*120/LG.width)),Image.LANCZOS); c.alpha_composite(l,(W0-160,30))
    R(d,W0-180,90,'بطاقة الولاء',F('Bold',40),CREAM); R(d,W0-180,132,'NUSS CLUB',F('Bold',24),GOLD)
    gap=(W0-140)/5
    for k in range(10):
        r_,cc=divmod(k,5); cx=W0-90-cc*gap; cy=250+r_*120
        if k==9:
            if won: d.ellipse([cx-46,cy-46,cx+46,cy+46],fill=GOLD); star(d,cx,cy,28,INK)
            else: d.ellipse([cx-44,cy-44,cx+44,cy+44],outline=GOLD,width=4); star(d,cx,cy,26,GOLD)
        else: cupicon(d,cx,cy,44,k<st)
    R(d,W0-50,H0-56,'معالي الزبون',F('Regular',24),(190,215,210)); R(d,W0-50,H0-22,'ضيفنا العزيز',F('Bold',32),CREAM)
    d.text((50,H0-26),'NUSS-2026-0007',font=F('Bold',26),fill=(190,215,210),anchor='ls')
    CARDS[key]=c; return c
def put_card(img,c,cx,cy,sc,rot,glow=0):
    cw=max(4,int(c.width*sc)); ch=max(4,int(c.height*sc)); cc=c.resize((cw,ch),Image.LANCZOS).rotate(rot,expand=True,resample=Image.BICUBIC)
    if glow>0:
        g=Image.new('RGBA',(VW,VH),(0,0,0,0)); ImageDraw.Draw(g).rounded_rectangle([cx-cw/2-30,cy-ch/2-30,cx+cw/2+30,cy+ch/2+30],radius=60,fill=GOLD+(int(170*glow),)); img.alpha_composite(g.filter(ImageFilter.GaussianBlur(40)))
    sh=Image.new('RGBA',(VW,VH),(0,0,0,0)); blk=Image.new('RGBA',cc.size,(0,0,0,255)); blk.putalpha(cc.getchannel('A').point(lambda v:int(v*.6))); sh.alpha_composite(blk,(int(cx-cc.width/2+16),int(cy-cc.height/2+30)))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22))); img.alpha_composite(cc,(int(cx-cc.width/2),int(cy-cc.height/2)))
def logo_small(img):
    l=LG.resize((104,round(LG.height*104/LG.width)),Image.LANCZOS); img.alpha_composite(l,(VW//2-52,VH-185))
def xfade(a,b,k): return Image.blend(a.convert('RGB'),b.convert('RGB'),eio(k)).convert('RGBA')
T=lambda s:int(s*FPS)
# timeline (seconds, voice starts at 0.4)
SC=[('o10',0.0,4.7),('r71',4.7,7.2),('o13',7.2,10.95),('o14',10.95,12.4),('o12',12.4,14.0),('o9',14.0,19.0)]
def scene_at(t):
    for n,a,b in SC:
        if a<=t<b: return n,a,b
    return SC[-1]
N=T(19.0); fr=0
def frame(t):
    n,a,b=scene_at(t); k=(t-a)/(b-a)
    im=bg(n,k,pan=1 if n in('o10','o13') else -1)
    if t<4.7:
        caption(im,'في ناس بتمرق علينا كل يوم...',None,(t-0.4)/0.5)
        caption(im,None,'وإحنا بنعرفهم من أول رشفة',(t-2.5)/0.5)
    elif t<7.2:
        caption(im,'عشان هيك...','عملنالك بطاقة الولاء',(t-4.8)/0.45)
        sc=back((t-5.6)/0.7)*0.92; 
        if t>=5.6: put_card(im,card(0),VW/2,1420+math.sin(t*2)*8,sc*0.85,-5,glow=0.5*ease((t-5.9)/0.6))
    elif t<10.95:
        caption(im,'كل طلب بختم...','وكل ما تيجي بتقرّب أكتر',(t-7.3)/0.45)
        st=min(8,int((t-7.4)/0.4)+1) if t>7.4 else 0
        put_card(im,card(st),VW/2,1420+math.sin(t*2)*8,0.8,-5+ (t-7.2)*0.6)
    elif t<12.4:
        caption(im,None,'ولما تكمّل الأختام؟',(t-11.05)/0.4)
        st=9 if t>11.4 else 8; z=0.92+0.10*eio((t-10.95)/1.4)
        put_card(im,card(st),VW/2,1420,z*0.87,-3+math.sin(t*9)*0.6*(t>11.8))
    elif t<14.0:
        caption(im,None,'قهوتك علينـــا!',(t-12.4)/0.3)
        put_card(im,card(9,won=True),VW/2,1420,0.9,0,glow=0.6+0.4*math.sin(t*6))
        d=ImageDraw.Draw(im); kk=(t-12.4)/1.6
        for j in range(40):
            ang=j*2.39; r=80+620*ease(kk); px=VW/2+r*math.cos(ang); py=1420+r*math.sin(ang)*.85+kk*kk*260
            s_=10 if j%3 else 14; col=[GOLD,(120,190,180),CREAM][j%3]
            d.rectangle([px-s_,py-s_/2,px+s_,py+s_/2],fill=col+(int(255*(1-max(0,kk-.6)/.4)),))
    else:
        a=ease((t-14.05)/0.6)
        dark=Image.new('RGBA',(VW,VH),(8,12,11,int(150*a))); im.alpha_composite(dark)
        l3=LG.resize((260,round(LG.height*260/LG.width)),Image.LANCZOS); l3.putalpha(l3.getchannel('A').point(lambda v:int(v*a))); im.alpha_composite(l3,((VW-260)//2,170))
        caption(im,'نُص كافيه...','مكان بيوسع الكـــل',(t-14.1)/0.5,y1=600,y2=740)
        if t>15.0:
            a2=ease((t-15.0)/0.5); lay=Image.new('RGBA',(VW,VH),(0,0,0,0)); dl=ImageDraw.Draw(lay)
            qs=420; qx=(VW-qs)//2; qy=840
            dl.rounded_rectangle([qx-24,qy-24,qx+qs+24,qy+qs+24],radius=36,fill=CREAM)
            lay.alpha_composite(QR.resize((qs,qs),Image.NEAREST),(qx,qy))
            R(dl,VW/2,qy+qs+110,'صوّر الكود... وطلّع بطاقة الولاء ببلاش',F('Bold',42),CREAM,'ms')
            R(dl,VW/2,qy+qs+170,'الرابط كمان موجود بالبيو',F('Regular',34),MUT,'ms')
            R(dl,VW/2,1660,'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',F('Regular',32),MUT,'ms')
            R(dl,VW/2,1720,'كل يوم من 9 الصبح لـ 9 المسا',F('Bold',34),MUT,'ms')
            sc=0.9+0.1*back((t-15.0)/0.5)
            if sc!=1: pass
            lay.putalpha(lay.getchannel('A').point(lambda v:int(v*a2))); im.alpha_composite(lay)
    if t<14.0: logo_small(im)
    return im
prev=None
for i in range(N):
    t=i/FPS; im=frame(t)
    # crossfade at scene boundaries
    for n,a,b in SC[1:]:
        if a<=t<a+0.25:
            im=xfade(frame(a-0.001),im,(t-a)/0.25); break
    if i<8: im=Image.blend(Image.new('RGB',(VW,VH),INK),im.convert('RGB'),i/8).convert('RGBA')
    im.convert('RGB').save(FD+f'{i:05d}.jpg',quality=90)
print(N)
