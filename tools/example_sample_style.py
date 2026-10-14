import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'example_daily_posts.py')).read().split("P=[")[0])
TEALTXT=(92,176,165)
def head1(img,XR,y,pre,hlw,line2,f,f2=None,gap=105):
    """line1 = pre + highlighted word (sample style), line2 plain"""
    f2=f2 or f; d=ImageDraw.Draw(img); wp=tw(d,pre,f) if pre else 0
    shadow_text(img,[(XR,y,pre+hlw,f),(XR,y+gap,line2,f2)])
    d=ImageDraw.Draw(img); hl(img,d,XR-wp,y,hlw,f,pad=(16,4),skew=8); d=ImageDraw.Draw(img)
    if pre: text(d,XR,y,pre,f)
    text(d,XR-wp,y,hlw,f); text(d,XR,y+gap,line2,f2)
def colored_label(img,XR,y,pre,colw,post,line2,arr):
    f=SR(42); f2=SB(52); d=ImageDraw.Draw(img)
    shadow_text(img,[(XR,y,pre+colw+post,f),(XR,y+62,line2,f2)],blur=8,alpha=150); d=ImageDraw.Draw(img)
    w1=tw(d,pre,f); w2=tw(d,colw,SB(42))
    text(d,XR,y,pre,f); text(d,XR-w1,y,colw,SB(42),fill=TEALTXT); text(d,XR-w1-w2,y,post,f)
    text(d,XR,y+62,line2,f2); arrow(img,arr)
def plain_label(img,XR,y,t,arr):
    shadow_text(img,[(XR,y,t,SB(38))],blur=8,alpha=150); text(ImageDraw.Draw(img),XR,y,t,SB(38)); arrow(img,arr)
def load(n): 
    im=cover(Image.open(S+f'gen5/n{n}.png').convert('RGB')).convert('RGBA'); return im
out=[]
# 1 takeaway on car
im=load(1); scrim(im,(480,40,1060,330)); fade_bottom(im)
head1(im,1010,170,'يا ','طالـــب...','السهر مش كله دراسة',DB(84),DB(64))
colored_label(im,590,470,'خذ ','القهوة',' تيكاوي','وكمّل سهرتك',[(470,420),(530,395),(585,430),(612,510)])
footer(im,ImageDraw.Draw(im)); out.append(im)
# 2 hat + iced (sample 7 layout: logo top-left, headline bottom-right, no footer)
im=load(2)
g=Image.new('L',(1,H))
for y in range(H): g.putpixel((0,y),int(255*min(1,max(0,(y-H*.70)/(H*.30))**1.4*.7)))
im.alpha_composite(Image.merge('RGBA',(*Image.new('RGB',(W,H),(8,10,10)).split(),g.resize((W,H)))))
f=DB(120); shadow_text(im,[(1030,1190,'مزاجك اليوم؟',f),(1030,1280,'سبانش لاتيه... والباقي تفاصيل',SR(52))])
d=ImageDraw.Draw(im); text(d,1030,1190,'مزاجك اليوم؟',f); text(d,1030,1280,'سبانش لاتيه... والباقي تفاصيل',SR(52))
plain_label(im,300,520,'أيس سبانش لاتيه',[(200,550),(230,610),(300,650),(345,680)])
lg=Image.open(S+'logo.png'); lg=lg.resize((150,round(lg.height*150/lg.width)),Image.LANCZOS); im.alpha_composite(lg,(70,60)); out.append(im)
# 3 cappuccino windowsill
im=load(3); scrim(im,(250,40,880,340)); fade_bottom(im)
headline(im,820,170,'الصبح ما بيبلّش...','إلا بـ','كابتشينـــو',DB(80),gap=104)
label(im,1010,1080,'كابتشينـــو','صباح الخير بكاسة',[(890,1030),(850,980),(800,950),(755,930)])
footer(im,ImageDraw.Draw(im)); out.append(im)
# 4 espresso sofa corner (sample 6)
im=load(4); scrim(im,(420,60,1060,360)); fade_bottom(im)
head1(im,1010,210,'','إسبريســـو...','قصير... بس بيعمل الفرق',DB(96),DB(62),gap=110)
label(im,300,600,'إسبريســو','مع قطعة شوكولا',[(240,650),(250,700),(285,740),(320,770)])
footer(im,ImageDraw.Draw(im)); out.append(im)
# 5 pistachio cheesecake overhead (sample 4)
im=load(5); scrim(im,(480,960,1060,1240),120); fade_bottom(im)
head1(im,1030,1070,'خلّي الريجيم ','لبكـــرا','وهلّق... بستاشيو',DB(84),DB(62),gap=100)
label(im,640,1000,'تشيز كيـــك','بستاشيو',[(560,960),(545,940),(540,935)]) if False else None
plain_label(im,330,560,'تشيز كيك بستاشيو',[(250,590),(280,660),(350,720),(400,760)])
logo_br(im) if False else None
lg=Image.open(S+'logo.png'); lg=lg.resize((130,round(lg.height*130/lg.width)),Image.LANCZOS); im.alpha_composite(lg,(60,1180)); out.append(im)
for i,im in enumerate(out): im.convert('RGB').save(S+f'out/sample_style_{i+1}.jpg',quality=95)
sh=Image.new('RGB',(432*5,540))
for i,im in enumerate(out): sh.paste(im.convert('RGB').resize((432,540)),(i*432,0))
sh.save(S+'out/sample_style_sheet.jpg'); print('ok')
