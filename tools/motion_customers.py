exec(open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/post.py').read())
import os,math,numpy as np
M=S+'motion/'; FD=M+'frames/'; os.makedirs(FD,exist_ok=True)
for f in os.listdir(FD): os.remove(FD+f)
VW,VH=1080,1920; FPS=30; SEG=75; CREAM=(240,232,218); MUT=(190,205,202)
def R(d,x,y,t,f,fill=WHITE,anchor='rs'): d.text((x,y),t,font=f,fill=fill,direction='rtl',anchor=anchor)
# background
bg=Image.new('RGB',(VW,VH),(14,20,19)); g=Image.new('L',(VW,VH),0); gd=ImageDraw.Draw(g); gd.ellipse([90,700,990,1600],fill=150); g=g.filter(ImageFilter.GaussianBlur(170))
bg.paste(Image.new('RGB',(VW,VH),(35,92,86)),(0,0),g)
n=Image.effect_noise((VW,VH),14).convert('RGB'); bg=Image.blend(bg,ImageChops.overlay(bg,n),.12)
lg=Image.open(S+'logo_white.png').convert('RGBA')
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
SEGS=[('مبرمج ذكـــي','espresso','بيطلب إسبريسو...','وبيسأل عن باسورد الواي فاي قبل ما يقعد'),
      ('معلّم صبـــور','tea','صابر على الطلاب...','بس مش على الشاي البارد'),
      ('عريس جديـــد','qunbula','العروس طلبت قنبلة النُّص...','وهو لسا بيحسب الميزانية'),
      ('حدّاد صامـــد','americano','صامد متل الحديد...','وقهوته متله: سودا وبلا سكر'),
      ('فنان حالـــم','watermelon','بيرسم بالخيال...','وبيشرب الصيف بعز الشتا'),
      ('مصمم طموح','coffee','"فاينل فاينل 3"...','والكوفي نوتيلا هو اللي فاينل')]
fr=0
def save(im):
    global fr; im.convert('RGB').save(FD+f'{fr:05d}.jpg',quality=90); fr+=1
for title,prod,p1,p2 in SEGS:
    pi=Image.open(M+prod+'.png').convert('RGBA'); s=min(620/pi.width,640/pi.height); pi=pi.resize((round(pi.width*s),round(pi.height*s)),Image.LANCZOS)
    # pre-render title layer
    tl=Image.new('RGBA',(VW,VH),(0,0,0,0)); d=ImageDraw.Draw(tl); f=DB(132)
    w=tw(d,title,f); XR=VW/2+w/2
    hl(tl,d,XR,500,title,f,pad=(22,6),skew=10); d=ImageDraw.Draw(tl); R(d,XR,500,title,f)
    bb=tl.getbbox()
    for i in range(SEG):
        im=bg.copy().convert('RGBA'); d=ImageDraw.Draw(im)
        # pill
        pt='مين إنت من زبائن النُّص؟'; fp=SB(34); pw=tw(d,pt,fp)
        d.rounded_rectangle([VW/2-pw/2-32,170,VW/2+pw/2+32,236],radius=33,outline=CREAM,width=2); R(d,VW/2,215,pt,fp,CREAM,'ms')
        # title reveal (RTL wipe)
        t=ease(i/16); rx=bb[2]-(bb[2]-bb[0])*t
        m=Image.new('L',(VW,VH),0); ImageDraw.Draw(m).rectangle([rx-2,bb[1],bb[2],bb[3]],fill=255)
        im.paste(tl,(0,0),Image.composite(tl.getchannel('A'),Image.new('L',(VW,VH),0),m))
        # product pop + float
        sc=0.55+0.45*back((i-8)/18) if i>=8 else 0
        if sc>0:
            fl=math.sin(i/9)*8 if i>26 else 0
            pw2,ph2=max(1,int(pi.width*sc)),max(1,int(pi.height*sc)); pimg=pi.resize((pw2,ph2),Image.LANCZOS)
            cx,by=VW//2,1330+fl
            sh=Image.new('RGBA',(VW,VH),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([cx-pw2*.42,by-22,cx+pw2*.42,by+22],fill=(0,0,0,int(150*min(1,sc))))
            im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18))); im.alpha_composite(pimg,(int(cx-pw2/2),int(by-ph2)))
        # punchline
        for j,(txt,fnt,yy,st) in enumerate([(p1,SB(48),1480,30),(p2,SR(40),1550,36)]):
            a=ease((i-st)/10)
            if a>0:
                lay=Image.new('RGBA',(VW,VH),(0,0,0,0)); ld=ImageDraw.Draw(lay)
                ff=fnt
                while tw(ld,txt,ff)>960: ff=SR(ff.size-2)
                R(ld,VW/2,yy+int(30*(1-a)),txt,ff,CREAM if j==0 else MUT,'ms')
                al=lay.getchannel('A').point(lambda v:int(v*a)); lay.putalpha(al); im.alpha_composite(lay)
        # logo small
        l2=lg.resize((110,round(lg.height*110/lg.width)),Image.LANCZOS); im.alpha_composite(l2,(VW//2-55,VH-200))
        # fade edges
        if i>=SEG-5:
            k=(i-(SEG-5))/5; im=Image.blend(im.convert('RGB'),Image.new('RGB',(VW,VH),(14,20,19)),k).convert('RGBA')
        save(im)
# end card 3s
for i in range(90):
    im=bg.copy().convert('RGBA'); d=ImageDraw.Draw(im); a=ease(i/15)
    l3=lg.resize((380,round(lg.height*380/lg.width)),Image.LANCZOS); l3.putalpha(l3.getchannel('A').point(lambda v:int(v*a))); im.alpha_composite(l3,((VW-380)//2,430))
    if i>8:
        f=DB(100); t='مكان بيوسع الكـــل'; w=tw(d,t,f); hl(im,d,VW/2+w/2,1060,t,f,pad=(20,6),skew=10); d=ImageDraw.Draw(im); R(d,VW/2+w/2,1060,t,f)
    if i>16:
        R(d,VW/2,1200,'إنت مين فيهم؟ قلّنا بالكومنت',SB(48),CREAM,'ms')
        R(d,VW/2,1330,'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',SR(34),MUT,'ms')
        R(d,VW/2,1400,'كل يوم من 9 الصبح لـ 9 المسا',SB(38),MUT,'ms')
    save(im)
print(fr)
