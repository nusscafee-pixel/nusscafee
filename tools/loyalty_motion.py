src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/ployal.py').read()
exec(src[:src.index('def place_card')])
import shutil
L=S+'lmotion/'; FD=L+'f/'; shutil.rmtree(FD,ignore_errors=True); os.makedirs(FD)
VW,VH=1080,1920; FPS=30
base=Image.open(S+'real/r71.png').convert('RGB'); s=max(VW/base.width,VH/base.height); base=base.resize((round(base.width*s),round(base.height*s)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,90,2))
x=(base.width-VW)//2; bg=base.crop((x,0,x+VW,VH)).convert('RGBA')
ov=Image.new('RGBA',(VW,VH),(0,0,0,0)); d=ImageDraw.Draw(ov)
for y in range(VH): t=abs(y-VH*0.5)/(VH*0.5); d.line([(0,y),(VW,y)],fill=(8,12,11,int(150+90*min(1,t))))
bg.alpha_composite(ov)
lg=Image.open(S+'logo_white.png').convert('RGBA')
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; return 1+(c1+1)*(t-1)**3+c1*(t-1)**2
def text_layer(lines):
    tl=Image.new('RGBA',(VW,VH),(0,0,0,0)); d=ImageDraw.Draw(tl)
    for (t,f,y,hlit) in lines:
        w=tw(d,t,f); xr=VW/2+w/2
        if hlit: hl(tl,d,xr,y,t,f,pad=(20,6),skew=9); d=ImageDraw.Draw(tl)
        R(d,xr,y,t,f)
    return tl
TXT=[ (0,90, text_layer([('بطاقة نُص...',DB(90),380,False),('صارت على جوالك',DB(104),520,True)])),
      (90,210,text_layer([('كل طلب بختـــم...',DB(90),380,False),('والقهوة علينـــا',DB(104),520,True)])),
      (210,300,text_layer([('ما بدها تطبيق',DB(90),380,False),('بتنحفظ بمحفظتك',DB(104),520,True)]))]
fr=0
def save(im):
    global fr; im.convert('RGB').save(FD+f'{fr:05d}.jpg',quality=90); fr+=1
cards={}
for i in range(300):
    im=bg.copy(); 
    for a,b,tl in TXT:
        if a<=i<b:
            al=min(ease((i-a)/10),1-ease((i-(b-8))/8) if i>b-8 else 1)
            l2=tl.copy(); l2.putalpha(l2.getchannel('A').point(lambda v:int(v*al))); im.alpha_composite(l2)
    st=0 if i<100 else min(9,1+(i-100)//11)
    if st not in cards: cards[st]=card(900,stamps=st,total=10)
    c=cards[st]
    sc=back((i-6)/22)*1.0 if i>=6 else 0
    if sc>0:
        rot=-6+math.sin(i/20)*2; fl=math.sin(i/14)*10
        cw=max(2,int(c.width*sc)); ch=max(2,int(c.height*sc)); cc=c.resize((cw,ch),Image.LANCZOS).rotate(rot,expand=True,resample=Image.BICUBIC)
        cx,cy=VW//2,1060+fl
        shd=Image.new('RGBA',(VW,VH),(0,0,0,0)); blk=Image.new('RGBA',cc.size,(0,0,0,255)); blk.putalpha(cc.getchannel('A').point(lambda v:int(v*.6))); shd.alpha_composite(blk,(int(cx-cc.width/2+16),int(cy-cc.height/2+30)))
        im.alpha_composite(shd.filter(ImageFilter.GaussianBlur(20))); im.alpha_composite(cc,(int(cx-cc.width/2),int(cy-cc.height/2)))
        if 200<=i<240:
            k=(i-200)/40; d=ImageDraw.Draw(im)
            for j in range(14):
                ang=j*2*math.pi/14; r=120+380*ease(k); px=cx+r*math.cos(ang); py=cy+r*math.sin(ang)*0.7
                a2=int(255*(1-k)); d.ellipse([px-9,py-9,px+9,py+9],fill=(216,190,128,a2) if j%2 else (120,190,180,a2))
    l2=lg.resize((110,round(lg.height*110/lg.width)),Image.LANCZOS); im.alpha_composite(l2,(VW//2-55,VH-190))
    save(im)
for i in range(90):
    im=bg.copy(); d=ImageDraw.Draw(im); a=ease(i/14)
    l3=lg.resize((400,round(lg.height*400/lg.width)),Image.LANCZOS); l3.putalpha(l3.getchannel('A').point(lambda v:int(v*a))); im.alpha_composite(l3,((VW-400)//2,420))
    if i>8:
        f=DB(100); t='نُصّك المفقـــود'; w=tw(d,t,f); hl(im,d,VW/2+w/2,1080,t,f,pad=(20,6),skew=9); d=ImageDraw.Draw(im); R(d,VW/2+w/2,1080,t,f)
    if i>16:
        R(d,VW/2,1220,'طلّع بطاقتك ببلاش من المنيو',SB(46),CREAM,'ms')
        R(d,VW/2,1340,'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',SR(34),(190,205,202),'ms')
        R(d,VW/2,1410,'كل يوم من 9 الصبح لـ 9 المسا',SB(38),(190,205,202),'ms')
    save(im)
print(fr)
