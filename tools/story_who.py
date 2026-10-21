exec(open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/post.py').read())
import os
SW,SH=1080,1920; BG=(12,20,19); MUT=(190,205,202)
O=S+'out/story_who/'; os.makedirs(O,exist_ok=True)
def fit(im,w,h,cy=.5):
    s=max(w/im.width,h/im.height); im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=(im.width-w)//2; y=int((im.height-h)*cy); return im.crop((x,y,x+w,y+h))
def canvas(): return Image.new('RGBA',(SW,SH),BG+(255,))
def fade(img,y0,y1,up=True):
    ov=Image.new('RGBA',(SW,SH),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(y0,y1):
        t=(y-y0)/(y1-y0); a=int(255*(t if up else 1-t)**1.2); d.line([(0,y),(SW,y)],fill=BG+(a,))
    img.alpha_composite(ov)
def pill(d,txt,y,xr=1010,f=None):
    f=f or SB(30); w=tw(d,txt,f); d.rounded_rectangle([xr-w-48,y,xr,y+56],radius=28,fill=TEAL); d.text((xr-24,y+41),txt,font=f,fill=WHITE,direction='rtl',anchor='rs')
def R(d,x,y,t,f,fill=WHITE,anchor='rs'): d.text((x,y),t,font=f,fill=fill,direction='rtl',anchor=anchor)
def HL(img,x,y,t,f):
    d=ImageDraw.Draw(img); hl(img,d,x,y,t,f,pad=(16,4),skew=8); d=ImageDraw.Draw(img); R(d,x,y,t,f)
def logo(img,x,y,w=120):
    lg=Image.open(S+'logo.png').convert('RGBA'); lg=lg.resize((w,round(lg.height*w/lg.width)),Image.LANCZOS); img.alpha_composite(lg,(x,y))
def foot(img):
    d=ImageDraw.Draw(img); logo(img,70,SH-200); R(d,1010,SH-120,'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',SR(26),MUT)
g1=Image.open(S+'who2/g01.png').convert('RGB'); g2=Image.open(S+'who2/g02.png').convert('RGB'); g5=Image.open(S+'who2/g05.png').convert('RGB')
# 1 hook
im=canvas(); im.paste(fit(g1,SW,1400,.55),(0,520)); fade(im,520,820,up=False); fade(im,1500,1920)
d=ImageDraw.Draw(im); pill(d,'كويز الشتا',150)
R(d,1010,330,'مين إنت',DB(120)); HL(im,1010,470,'بالشتـــا؟',DB(130))
d=ImageDraw.Draw(im); R(d,1010,1640,'اختار مشروبك... ومنقلّك مين إنت',SB(40)); R(d,1010,1700,'اسحب للستوري الجاي',SR(30),MUT); foot(im)
im.convert('RGB').save(O+'s1.jpg',quality=95)
# 2 poll split
im=canvas(); top=fit(g1,SW,760,.6); bot=fit(g2,SW,760,.62)
im.paste(top,(0,250)); im.paste(bot,(0,1110))
d=ImageDraw.Draw(im); pill(d,'مين إنت بالشتا؟',90)
band=Image.new('RGBA',(SW,150),BG+(235,)); im.alpha_composite(band,(0,935))
d=ImageDraw.Draw(im); R(d,SW/2,1032,'ولا',DB(70),WHITE,'ms')
for (y,num,a,b) in [(330,'1','البردان الدايم','هوت شوكليت'),(1190,'2','بيحب المطر','لاتيه سخن')]:
    d.ellipse([60,y-50,160,y+50],fill=TEAL); d.text((110,y+18),num,font=SB(56),fill=WHITE,anchor='ms')
    ov=Image.new('RGBA',(520,150),BG+(190,)); im.alpha_composite(ov,(530,y-70)); d=ImageDraw.Draw(im)
    R(d,1010,y,a,DB(56)); R(d,1010,y+56,b,SB(34),MUT)
R(d,SW/2,1960-80,'',SR(10))
R(d,SW/2,1905,'',SR(10))
d.text((SW/2,1880),'ابعتلنا 1 ولا 2 بالرسائل',font=SB(38),fill=WHITE,direction='rtl',anchor='ms')
im.convert('RGB').save(O+'s2.jpg',quality=95)
# 3 not cold
im=canvas(); im.paste(fit(g5,SW,1500,.55),(0,300)); fade(im,300,600,up=False); fade(im,1550,1920)
d=ImageDraw.Draw(im); pill(d,'مين إنت بالشتا؟',150)
R(d,1010,330,'"أنا مش بـــردان"',DB(90)); HL(im,1010,460,'وهو بيرجـــف',DB(100))
d=ImageDraw.Draw(im); R(d,1010,1690,'إنت آيس أمريكانو... رسمي',SB(44)); R(d,1010,1750,'تاغ صاحبك اللي هيك',SR(32),MUT); foot(im)
im.convert('RGB').save(O+'s3.jpg',quality=95)
# 4 CTA
im=canvas(); im.paste(fit(g2,SW,1920,.5),(0,0))
ov=Image.new('RGBA',(SW,SH),BG+(150,)); im.alpha_composite(ov); fade(im,900,1500)
d=ImageDraw.Draw(im); pill(d,'شو ما كنت',150)
R(d,1010,420,'مشروبك',DB(130)); HL(im,1010,570,'مستنّيـــك',DB(130))
d=ImageDraw.Draw(im)
y=1350
for t,f,c in [('كل يوم من 10 الصبح لـ 10 المسا',SB(44),WHITE),('الجمعة من 3 العصر',SB(40),MUT)]:
    R(d,1010,y,t,f,c); y+=70
hl(im,d,1010,1580,'عنواننا',SB(40),pad=(10,3),skew=4); d=ImageDraw.Draw(im); R(d,1010,1580,'عنواننا',SB(40))
R(d,1010,1650,'تقاطع شارع ملعب فلسطين، مع شارع التايلاندي',SR(32),MUT); logo(im,70,1560,150)
im.convert('RGB').save(O+'s4.jpg',quality=95)
sh=Image.new('RGB',(4*360+30,640),(30,30,30))
for i in range(4): sh.paste(Image.open(O+f's{i+1}.jpg').resize((360,640)),(i*370,0))
sh.save(O+'preview.jpg'); print('ok')
