import os,math,shutil,json,sys
src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/plm3.py').read()
exec(src[:src.index('BGS={}')])
exec(src[src.index('def hlblock'):src.index('def logo_small')])
FD=S+'mg/f/'; shutil.rmtree(FD,ignore_errors=True); os.makedirs(FD)
TM=json.load(open(S+'mg/times.json'))   # keys: l2,l3,l4,l5,l6,end,total
# static background
BG=Image.new('RGB',(VW,VH),(11,18,17)); g=Image.new('L',(VW,VH),0); gd=ImageDraw.Draw(g); gd.ellipse([-100,620,1180,1700],fill=170); g=g.filter(ImageFilter.GaussianBlur(220))
BG.paste(Image.new('RGB',(VW,VH),(35,92,86)),(0,0),g)
n=Image.effect_noise((VW,VH),12).convert('L'); BG=Image.blend(BG,Image.merge('RGB',(n,n,n)),.045).convert('RGBA')
wm=LG.resize((900,round(LG.height*900/LG.width)),Image.LANCZOS); wm.putalpha(wm.getchannel('A').point(lambda v:int(v*.045))); BG.alpha_composite(wm,((VW-900)//2,700))
d=ImageDraw.Draw(BG)
for k in range(9): d.line([(60,1820-k*0),(60,1820)],fill=(0,0,0))
def cup(img,cx,cy,s,a,t):
    lay=Image.new('RGBA',(VW,VH),(0,0,0,0)); d=ImageDraw.Draw(lay); w=int(260*s); h=int(220*s)
    d.rounded_rectangle([cx-w/2,cy-h/2,cx+w/2,cy+h/2],radius=int(40*s),fill=CREAM)
    d.arc([cx+w/2-30*s,cy-h/4,cx+w/2+70*s,cy+h/4+20*s],-90,90,fill=CREAM,width=int(22*s))
    d.rounded_rectangle([cx-w/2-40*s,cy+h/2+6*s,cx+w/2+40*s,cy+h/2+32*s],radius=int(13*s),fill=CREAM)
    l=LG.resize((int(130*s),int(130*s*LG.height/LG.width)),Image.LANCZOS); lc=Image.merge('RGBA',(*Image.new('RGB',l.size,TEAL).split(),l.getchannel('A'))); lay.alpha_composite(lc,(int(cx-l.width/2),int(cy-l.height/2)))
    for j in range(3):
        x0=cx-60*s+j*60*s; pts=[(x0+math.sin(t*3+j+y/40)*14*s,cy-h/2-20*s-y) for y in range(0,int(150*s),6)]
        d.line(pts,fill=(244,238,226,int(170*(0.6+0.4*math.sin(t*2+j)))),width=int(10*s),joint='curve')
    lay.putalpha(lay.getchannel('A').point(lambda v:int(v*a))); img.alpha_composite(lay)
def rings(img,cx,cy,t,a):
    d=ImageDraw.Draw(img)
    for j in range(3):
        k=((t*0.6+j/3)%1); r=180+320*k; d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=(120,190,180,int(110*(1-k)*a)),width=3)
def frame(t):
    im=BG.copy()
    if t<TM['l2']:
        rings(im,VW/2,1180,t,ease((t-0.2)/0.6)); cup(im,VW/2,1200,1.25*back((t-0.15)/0.6) if t>0.15 else 0.01,ease((t-0.15)/0.4),t)
        caption(im,'في ناس بتمرق علينا كل يوم...',None,(t-0.4)/0.5)
        caption(im,None,'وإحنا بنعرفهم من أول رشفة',(t-TM['l1b'])/0.5)
        if t>TM['l2']-0.35:
            k=(t-(TM['l2']-0.35))/0.35; im=Image.blend(im.convert('RGB'),BG.convert('RGB'),eio(k)).convert('RGBA')
    elif t<TM['l3']:
        caption(im,'عشان هيك...','عملنالك بطاقة الولاء',(t-TM['l2'])/0.45)
        k=(t-TM['l2']-0.5)/0.8
        if k>0:
            fl=abs(math.cos(min(1,ease(k))*math.pi/2+math.pi/2)) if k<1 else 1
            c=card(0); sx=max(0.02,ease(k)); cw=int(c.width*0.9*sx)
            cc=c.resize((max(4,cw),int(c.height*0.9)),Image.LANCZOS)
            put_card(im,cc,VW/2,1250,1.0,-4*ease(k),glow=0.45*ease(k-0.5))
    elif t<TM['l4']:
        caption(im,'كل طلب بختم...','وكل ما تيجي بتقرّب أكتر',(t-TM['l3'])/0.45)
        dur=TM['l4']-TM['l3']-0.5; st=min(8,int(max(0,t-TM['l3']-0.3)/dur*8)+ (1 if t>TM['l3']+0.3 else 0))
        put_card(im,card(st),VW/2,1250+math.sin(t*2)*8,0.9,-4)
        d=ImageDraw.Draw(im); ph=((t-TM['l3']-0.3)/dur*8)%1
        if t>TM['l3']+0.3 and st<=8: R(d,VW/2,1600-ph*60,'+1 ختم',F('Black',54),GOLD+(int(255*(1-ph)),),'ms')
    elif t<TM['l5']:
        caption(im,None,'ولما تكمّل الأختام؟',(t-TM['l4'])/0.4)
        k=(t-TM['l4'])/(TM['l5']-TM['l4']); st=9 if k>0.25 else 8
        put_card(im,card(st),VW/2,1250,0.9+0.12*eio(k),-4+4*eio(k)+math.sin(t*14)*0.8*(k>0.6))
    elif t<TM['end']:
        caption(im,None,'قهوتك علينـــا!',(t-TM['l5'])/0.3)
        put_card(im,card(9,won=True),VW/2,1250,1.02,0,glow=0.6+0.4*math.sin(t*6))
        d=ImageDraw.Draw(im); kk=(t-TM['l5'])/1.6
        for j in range(46):
            ang=j*2.39; r=80+640*ease(kk); px=VW/2+r*math.cos(ang); py=1250+r*math.sin(ang)*.85+kk*kk*280
            s_=10 if j%3 else 15; col=[GOLD,(120,190,180),CREAM][j%3]
            d.rectangle([px-s_,py-s_/2,px+s_,py+s_/2],fill=col+(int(255*max(0,1-max(0,kk-.6)/.4)),))
    else:
        a=ease((t-TM['end'])/0.5)
        l3=LG.resize((250,round(LG.height*250/LG.width)),Image.LANCZOS); l3.putalpha(l3.getchannel('A').point(lambda v:int(v*a))); im.alpha_composite(l3,((VW-250)//2,170))
        caption(im,'نُص كافيه...','المكان مكانـــك',(t-TM['end']-0.1)/0.5,y1=590,y2=730)
        if t>TM['end']+0.7:
            a2=ease((t-TM['end']-0.7)/0.5); lay=Image.new('RGBA',(VW,VH),(0,0,0,0)); dl=ImageDraw.Draw(lay)
            qs=420; qx=(VW-qs)//2; qy=830
            dl.rounded_rectangle([qx-24,qy-24,qx+qs+24,qy+qs+24],radius=36,fill=CREAM); lay.alpha_composite(QR.resize((qs,qs),Image.NEAREST),(qx,qy))
            R(dl,VW/2,qy+qs+110,'صوّر الكود... وطلّع بطاقة الولاء ببلاش',F('Bold',42),CREAM,'ms')
            R(dl,VW/2,qy+qs+170,'الرابط كمان موجود بالبيو',F('Regular',34),MUT,'ms')
            R(dl,VW/2,1660,'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',F('Regular',32),MUT,'ms')
            R(dl,VW/2,1720,'كل يوم من 9 الصبح لـ 9 المسا',F('Bold',34),MUT,'ms')
            lay.putalpha(lay.getchannel('A').point(lambda v:int(v*a2))); im.alpha_composite(lay)
    if t<TM['end']:
        l=LG.resize((100,round(LG.height*100/LG.width)),Image.LANCZOS); im.alpha_composite(l,(VW//2-50,VH-180))
    return im
N=int(TM['total']*FPS)
for i in range(N):
    t=i/FPS; im=frame(t)
    if i<6: im=Image.blend(Image.new('RGB',(VW,VH),INK),im.convert('RGB'),i/6).convert('RGBA')
    im.convert('RGB').save(FD+f'{i:05d}.jpg',quality=90)
print(N)
