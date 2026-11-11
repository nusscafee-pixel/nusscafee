src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/ployal.py').read()
exec(src[:src.index('def place_card')])
import shutil
L=S+'lmotion/'; FD=L+'f2/'; shutil.rmtree(FD,ignore_errors=True); os.makedirs(FD)
VW,VH=1080,1920
INK=(14,20,19); MUT=(190,205,202); TEALL=(120,190,180)
b0=_open(S+'launch/t3.png').convert('RGB'); s=max(VW/b0.width,VH/b0.height); b0=b0.resize((round(b0.width*s),round(b0.height*s)),Image.LANCZOS)
x=(b0.width-VW)//2; BG=b0.crop((x,0,x+VW,VH)).convert('RGBA')
ov=Image.new('RGBA',(VW,VH),(0,0,0,0)); d=ImageDraw.Draw(ov)
for y in range(VH):
    t=y/VH; a=190 if t<.25 else (70 if t<.75 else 70+int(140*(t-.75)/.25)); d.line([(0,y),(VW,y)],fill=(8,12,11,a))
BG.alpha_composite(ov)
LG=_open(S+'logo_white.png').convert('RGBA')
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def eio(t): t=max(0,min(1,t)); return t*t*(3-2*t)
def back(t):
    t=max(0,min(1,t)); c=1.70158; return 1+(c+1)*(t-1)**3+c*(t-1)**2
CARD={k:card(900,stamps=k,total=10).resize((480,302),Image.LANCZOS) for k in range(11)}
PW,PH=580,1160; PX=(VW-PW)//2; PY0=640
SW,SH=PW-44,PH-44
def phone_frame():
    f=Image.new('RGBA',(PW,PH),(0,0,0,0)); d=ImageDraw.Draw(f)
    d.rounded_rectangle([0,0,PW-1,PH-1],radius=78,fill=(22,26,26,255),outline=(70,80,80,255),width=3)
    d.rounded_rectangle([PW//2-80,30,PW//2+80,62],radius=16,fill=(5,6,6,255)); return f
FRAME=phone_frame()
SMASK=Image.new('L',(SW,SH),0); ImageDraw.Draw(SMASK).rounded_rectangle([0,0,SW-1,SH-1],radius=58,fill=255)
def screen_base():
    sc=Image.new('RGBA',(SW,SH),(16,24,23,255)); d=ImageDraw.Draw(sc)
    d.text((40,70),'9:41',font=SB(26),fill=WHITE,anchor='ls')
    l=LG.resize((70,round(LG.height*70/LG.width)),Image.LANCZOS); sc.alpha_composite(l,(SW-110,110))
    R(d,SW-130,160,'نُص كافيه',SB(34)); R(d,SW-130,200,'المنيو',SR(24),MUT); return sc
def btn(d,cx,cy,w,t,fill=TEAL,fg=WHITE,f=None):
    f=f or SB(30); d.rounded_rectangle([cx-w/2,cy-38,cx+w/2,cy+38],radius=38,fill=fill); R(d,cx,cy+11,t,f,fg,'ms')
def tap(img,cx,cy,k):
    if k<0 or k>1: return
    d=ImageDraw.Draw(img); r=20+70*ease(k); a=int(200*(1-k)); d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=(255,255,255,a),width=6)
    if k<.5: d.ellipse([cx-22,cy-22,cx+22,cy+22],fill=(255,255,255,140))
STEPS=[(0,'بطاقة نُص...','صارت على جوالـــك'),(75,'افتح المنيو...','وطلّع بطاقتك ببـــلاش'),(180,'ضيفها لمحفظتك','بلمسة وحـــدة'),(255,'كل طلب بختـــم...','والأختام بتعبّى لحالها'),(390,'كمّلت الأختـــام؟','قهوتك علينـــا!')]
TOTAL=480; END=90
def headline(img,i):
    cur=[k for k,(a,_,_) in enumerate(STEPS) if i>=a][-1]; a0=STEPS[cur][0]; k=ease((i-a0)/12)
    _,l1,l2=STEPS[cur]; lay=Image.new('RGBA',(VW,VH),(0,0,0,0)); d=ImageDraw.Draw(lay)
    pt='جديد: بطاقة الولاء'; fp=SB(30); w=tw(d,pt,fp); d.rounded_rectangle([VW/2-w/2-30,120,VW/2+w/2+30,178],radius=29,fill=TEAL); R(d,VW/2,160,pt,fp,WHITE,'ms')
    f1=DB(72); w1=tw(d,l1,f1); R(d,VW/2+w1/2,320,l1,f1)
    f2=DB(88)
    while tw(d,l2,f2)>960: f2=DB(f2.size-4)
    w2=tw(d,l2,f2); hl(lay,d,VW/2+w2/2,440,l2,f2,pad=(18,5),skew=8); d=ImageDraw.Draw(lay); R(d,VW/2+w2/2,440,l2,f2)
    lay.putalpha(lay.getchannel('A').point(lambda v:int(v*k))); img.alpha_composite(lay,(0,int(20*(1-k))))
    d=ImageDraw.Draw(img); n=len(STEPS)
    for j in range(n):
        cx=VW/2+(n/2-.5-j)*44; on=j<=cur
        d.rounded_rectangle([cx-(16 if j==cur else 8),528,cx+(16 if j==cur else 8),544],radius=8,fill=WHITE if on else (255,255,255,90))
def screen(i):
    sc=screen_base(); d=ImageDraw.Draw(sc); taps=[]
    if i<75:
        for r_,(n,p) in enumerate([('آيس لاتيه','22'),('كريب','22'),('كيك نوتيلا','22')]):
            y=280+r_*120; d.rounded_rectangle([30,y,SW-30,y+96],radius=22,fill=(28,40,38)); R(d,SW-60,y+58,n,SB(30)); d.text((60,y+58),p+' ₪',font=SB(28),fill=TEALL,anchor='ls')
        k=ease((i-25)/20); sy=SH-int(520*k)
        d.rounded_rectangle([0,sy,SW,SH+40],radius=40,fill=(244,238,226))
        R(d,SW/2,sy+90,'بطاقة نُص على جوالك',SB(36),INK,'ms'); R(d,SW/2,sy+140,'كل طلب بختم… والمكافأة إلك',SR(28),(80,90,88),'ms')
        bc=(SW/2,sy+250); btn(d,*bc,380,'طلّع بطاقتي')
        taps.append((bc,(i-55)/14))
    elif i<180:
        R(d,SW/2,330,'طلّع بطاقتك ببلاش',SB(40),WHITE,'ms'); R(d,SW/2,380,'ما بدها تطبيق',SR(28),MUT,'ms')
        d.rounded_rectangle([40,460,SW-40,560],radius=24,fill=(28,40,38),outline=TEALL,width=2); R(d,SW-70,445,'رقم الجوال',SR(24),MUT)
        num='0599 123 456'; n=int(max(0,min(len(num),(i-90)/3.5))); d.text((70,525),num[:n]+('|' if (i//8)%2 else ''),font=SB(40),fill=WHITE,anchor='ls')
        d.rounded_rectangle([40,600,SW-40,700],radius=24,fill=(28,40,38)); R(d,SW-70,665,'الاسم (اختياري)',SR(28),MUT)
        bc=(SW/2,800); btn(d,*bc,420,'طلّع البطاقة'); taps.append((bc,(i-148)/14))
        if i>=162:
            k=ease((i-162)/14); d.rounded_rectangle([0,0,SW,SH],radius=58,fill=(16,24,23,int(255*k)))
    elif i<255:
        k=back((i-180)/16); c=CARD[0]; cw=max(4,int(c.width*min(1,k)))
        if k>0.02: cc=c.resize((cw,max(2,int(c.height*cw/c.width)))); sc.alpha_composite(cc,(int(SW/2-cw/2),300))
        R(d,SW/2,700,'بطاقتك جاهزة 🎉'.replace(' 🎉',''),SB(38),WHITE,'ms')
        bc=(SW/2,820); btn(d,*bc,440,'أضف إلى المحفظة',fill=(0,0,0),fg=WHITE)
        d.rounded_rectangle([bc[0]-205,bc[1]-24,bc[0]-170,bc[1]+18],radius=6,fill=(255,255,255))
        taps.append((bc,(i-222)/14))
        if i>=236:
            k2=ease((i-236)/16); sc2=Image.new('RGBA',(SW,SH),(0,0,0,0)); dd=ImageDraw.Draw(sc2)
            dd.rounded_rectangle([0,0,SW,SH],radius=58,fill=(8,10,10,int(240*k2))); sc.alpha_composite(sc2)
            cc=CARD[0]; sc.alpha_composite(cc,(int(SW/2-cc.width/2),int(300+380*k2*0) )) if k2<1 else None
            d=ImageDraw.Draw(sc); R(d,SW/2,180,'المحفظة',SB(40),(255,255,255,int(255*k2)),'ms')
    else:
        d2=ImageDraw.Draw(sc); d2.rounded_rectangle([0,0,SW,SH],radius=58,fill=(8,10,10,240)); R(d2,SW/2,180,'المحفظة',SB(40),WHITE,'ms')
        for j,col in enumerate([(52,56,64),(70,52,40)]):
            d2.rounded_rectangle([40,820+j*70,SW-40,820+j*70+260],radius=26,fill=col)
        st=0 if i<275 else min(10,1+(i-275)//11)
        c=CARD[min(st,10)]
        glow=i>=390
        cy=250
        if glow:
            g=Image.new('RGBA',(SW,SH),(0,0,0,0)); ImageDraw.Draw(g).rounded_rectangle([SW/2-c.width/2-20,cy-20,SW/2+c.width/2+20,cy+c.height+20],radius=40,fill=(216,190,128,int(120+60*math.sin(i/5))))
            sc.alpha_composite(g.filter(ImageFilter.GaussianBlur(24)))
        sc.alpha_composite(c,(int(SW/2-c.width/2),cy)); d2=ImageDraw.Draw(sc)
        left=max(0,10-st)
        if st<10:
            R(d2,SW/2,640,f'باقي {left} أختام على قهوتك',SB(34),WHITE,'ms')
            if 275<=i<390 and (i-275)%11<6:
                k=(i-275)%11/6; R(d2,SW/2,720,'+1 ختم',SB(40),(216,190,128,int(255*(1-k))),'ms')
        else:
            R(d2,SW/2,640,'قهوتك علينا!',DB(56),(216,190,128),'ms'); R(d2,SW/2,700,'ورجي الكود للكاشير',SR(30),MUT,'ms')
            for j in range(26):
                ang=j*2.4; r=60+300*ease((i-390)/40); px=SW/2+r*math.cos(ang); py=cy+150+r*math.sin(ang)*.8+((i-390)*3 if i>390 else 0)*.3
                d2.rectangle([px-6,py-6,px+6,py+6],fill=[(216,190,128),(120,190,180),(244,238,226)][j%3])
    return sc,taps
fr=0
for i in range(TOTAL):
    im=BG.copy(); headline(im,i)
    k=ease(i/22); py=PY0+int(700*(1-k))+int(math.sin(i/30)*6)
    sc,taps=screen(i)
    ph=FRAME.copy(); ph.paste(sc,(22,22),SMASK)
    sh=Image.new('RGBA',(VW,VH),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([PX+20,py+40,PX+PW-20,py+PH],radius=80,fill=(0,0,0,170)); im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
    im.alpha_composite(ph,(PX,py))
    for (cx,cy),kk in taps: tap(im,PX+22+cx,py+22+cy,kk)
    if i>=TOTAL-8: im=Image.blend(im.convert('RGB'),Image.new('RGB',(VW,VH),INK),(i-(TOTAL-8))/8).convert('RGBA')
    im.convert('RGB').save(FD+f'{fr:05d}.jpg',quality=90); fr+=1
for i in range(END):
    im=BG.copy(); d=ImageDraw.Draw(im); im.alpha_composite(Image.new('RGBA',(VW,VH),(8,12,11,150))); d=ImageDraw.Draw(im); a=ease(i/14)
    l3=LG.resize((380,round(LG.height*380/LG.width)),Image.LANCZOS); l3.putalpha(l3.getchannel('A').point(lambda v:int(v*a))); im.alpha_composite(l3,((VW-380)//2,430))
    if i>8:
        f=DB(100); t='نُصّك المفقـــود'; w=tw(d,t,f); hl(im,d,VW/2+w/2,1060,t,f,pad=(20,6),skew=9); d=ImageDraw.Draw(im); R(d,VW/2+w/2,1060,t,f)
    if i>16:
        R(d,VW/2,1200,'طلّع بطاقتك ببلاش من المنيو',SB(46),CREAM,'ms')
        R(d,VW/2,1320,'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',SR(34),MUT,'ms')
        R(d,VW/2,1390,'كل يوم من 9 الصبح لـ 9 المسا',SB(38),MUT,'ms')
    im.convert('RGB').save(FD+f'{fr:05d}.jpg',quality=90); fr+=1
print(fr)
