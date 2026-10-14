import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'post.py')).read())
def load(n,bright=1.0):
    im=cover(Image.open(S+'gen/'+n+'.png').convert('RGB'))
    if bright!=1.0: im=ImageEnhance.Brightness(im).enhance(bright)
    return im
def bottom_fade(im,start=.86,amt=.6):
    g=Image.new('L',(1,H))
    for y in range(H): g.putpixel((0,y),int(255*min(1,max(0,(y-H*start)/(H*(1-start)))**1.3*amt)))
    return Image.composite(Image.new('RGB',(W,H),(8,10,10)),im,g.resize((W,H)))
def teal_blocks(img,boxes,a=90):
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(lay)
    for b in boxes: ld.rectangle(b,fill=(38,96,92,a))
    img.alpha_composite(lay)
def swipe(img,n):
    d=ImageDraw.Draw(img); f=SR(26)
    d.text((W-60,H-60),f'{n} / 5',font=f,fill=(225,225,220),anchor='rs')
HF=DB(80)
# ---------- latte redo
im=bottom_fade(load('latte2',.95)).convert('RGBA')
teal_blocks(im,[(130,90,330,280),(780,330,1000,520),(0,420,170,600)])
headline(im,1010,140,'نـاعــم من بـرّا...','وقلبه ','إسبريســـو',HF)
label(im,1010,1110,'آيـــس','سبانش لاتيه',[(900,1060),(860,1010),(780,990),(690,1000)])
footer(im,ImageDraw.Draw(im))
im.convert('RGB').save(S+'out/post3_spanish_latte_magnific.jpg',quality=95)

# ---------- carousel
# 1 teaser: dark with light only on top of dome
im=load('s1')
dark=ImageEnhance.Brightness(im).enhance(.22)
m=Image.new('L',(W//4,H//4),0); dm=ImageDraw.Draw(m); dm.ellipse([95,120,175,175],fill=255)
m=m.filter(ImageFilter.GaussianBlur(14)).resize((W,H))
im=Image.composite(ImageEnhance.Brightness(im).enhance(.9),dark,m).convert('RGBA')
headline(im,1010,190,'في إشي بالمنيو...','حامل ','اسمنـــا',DB(88),gap=112)
d=ImageDraw.Draw(im); text(d,1010,420,'خمّن شو هو؟',SR(40),fill=(220,220,215))
arrow(im,[(260,1180),(200,1210),(130,1200),(90,1170)])
d=ImageDraw.Draw(im); text(d,560,1200,'اسحب',SB(34))
logo_br(im); im.convert('RGB').save(S+'out/carousel_1.jpg',quality=95)

# 2 reveal
im=bottom_fade(load('s2')).convert('RGBA')
teal_blocks(im,[(0,330,200,520),(890,700,1080,880)])
headline(im,520,170,'قنبلـــة','','النُّص',DB(110),gap=130)
d=ImageDraw.Draw(im); shadow_text(im,[(440,390,'وصلت يا جماعة...',SR(38))]); d=ImageDraw.Draw(im); text(d,440,390,'وصلت يا جماعة...',SR(38))
label(im,420,660,'صوص','بستاشيو لايف',[(430,610),(470,585),(505,600),(522,640)])
swipe(im,2); im.convert('RGB').save(S+'out/carousel_2.jpg',quality=95)

# 3 inside
im=bottom_fade(load('s3a')).convert('RGBA')
headline(im,1010,170,'شو','جوّاتهـــا','؟',DB(96),gap=118) if False else None
headline(im,1010,190,'شو جوّاتهـــا؟','','',DB(96))
label(im,250,420,'بستاشيـــو','مكسّر عالوجه',[(290,445),(330,470),(360,510),(380,540)])
label(im,1010,450,'كريمـــة','ناعمة وخفيفة',[(830,470),(760,490),(700,540),(660,590)])
label(im,760,1040,'نوتيـــلا','بالقلب',[(560,1020),(520,980),(500,920),(500,840)])
label(im,1040,1000,'شوكولاتة','القشرة',[(960,950),(950,880),(920,820),(900,780)])
swipe(im,3); im.convert('RGB').save(S+'out/carousel_3.jpg',quality=95)

# 4 pairing
im=bottom_fade(load('s4')).convert('RGBA')
teal_blocks(im,[(850,820,1060,1000),(80,620,260,760)])
headline(im,1010,190,'ما بتكمل إلا مع...','قهوة ','تركـــي',HF)
swipe(im,4); im.convert('RGB').save(S+'out/carousel_4.jpg',quality=95)

# 5 CTA
im=bottom_fade(load('s5'),.80,.85).convert('RGBA')
teal_blocks(im,[(860,330,1060,520)])
headline(im,1010,170,'تعال','','فجّرهـــا عنّا',DB(100),gap=124)
footer(im,ImageDraw.Draw(im))
im.convert('RGB').save(S+'out/carousel_5.jpg',quality=95)
print('ok')
