import os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'world20_layouts.py')).read()
exec(src[:src.index('\nP=[\n')])
im=cover(Image.open(S+'hours/h2.png').convert('RGB')).convert('RGBA'); CUR[0]=im.copy()
d=ImageDraw.Draw(im)
# pill
t='مواعيد الدوام'; f=SB(30); w=tw(d,t,f); d.rounded_rectangle([1010-w-48,60,1010,114],radius=27,fill=TEAL); d.text((1010-24,99),t,font=f,fill=WHITE,direction='rtl',anchor='rs')
# headline
f=DB(70); d.text((1010,210),'بنصحى بكّير...',font=f,fill=WHITE,direction='rtl',anchor='rs')
w=tw(d,'وبنام ',f); hl(im,d,1010-w,300,'بكّيـــر',f,pad=(14,4),skew=7); d=ImageDraw.Draw(im)
d.text((1010,300),'وبنام ',font=f,fill=WHITE,direction='rtl',anchor='rs'); d.text((1010-w,300),'بكّيـــر',font=f,fill=WHITE,direction='rtl',anchor='rs')
# two cards
def card(x0,x1,day,hrs,note=None):
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(lay)
    ld.rounded_rectangle([x0,340,x1,500],radius=22,fill=(14,30,28,215),outline=(47,112,104,255),width=3)
    im.alpha_composite(lay); dd=ImageDraw.Draw(im)
    dd.text((x1-26,390),day,font=SB(32),fill=(130,200,190),direction='rtl',anchor='rs')
    dd.text((x1-26,455),hrs,font=DB(50),fill=WHITE,direction='rtl',anchor='rs')
    if note: dd.text((x1-26,488),note,font=SR(22),fill=(190,205,202),direction='rtl',anchor='rs')
card(530,1010,'من السبت للخميس','10 الصبح – 10 المسا')
card(70,510,'الجمعة','3 العصر – 10 المسا','(الجمعة بنتدلّع شوي)')
# funny label on the sleeping cup
lx,ly=1010,640
hl(im,d,lx,ly,'نايمـــة',SB(40),pad=(8,2),skew=3); d=ImageDraw.Draw(im)
d.text((lx,ly),'نايمـــة',font=SB(40),fill=WHITE,direction='rtl',anchor='rs')
d.text((lx,ly+42),'وبتصحى الساعة 10 الصبح',font=SR(30),fill=WHITE,direction='rtl',anchor='rs')
d.text((lx,ly+80),'بعد الـ10 المسا؟ روح نام إنت كمان',font=SR(26),fill=(200,212,209),direction='rtl',anchor='rs')
arrow_c(im,[(770,700),(760,740),(780,770),(800,800)] if False else [(665,705),(625,690),(595,720),(575,770)],WHITE)
footer_c(im)
im.convert('RGB').save(S+'out/hours_post.jpg',quality=95)
# story version (framed like campaign)
st=Image.new('RGBA',(1080,1920),(12,20,19,255)); clean=cover(Image.open(S+'hours/h2.png').convert('RGB')).convert('RGBA')
st.paste(clean,(0,120)); dd=ImageDraw.Draw(st); dd.line([(0,120),(1080,120)],fill=TEAL,width=3); dd.line([(0,1470),(1080,1470)],fill=TEAL,width=3)
import copy
ov=im.crop((0,0,W,520)); st.alpha_composite(ov,(0,120)) if False else None
st.paste(im.crop((0,0,W,H)),(0,120))
dd=ImageDraw.Draw(st)
dd.text((1010,1565),'إحنا بنسكّر 10 المسا...',font=DB(64),fill=WHITE,direction='rtl',anchor='rs')
w=tw(dd,'تعال ',DB(80)); hl(st,dd,1010-w,1660,'بكّيـــر',DB(80),pad=(14,4),skew=7); dd=ImageDraw.Draw(st)
dd.text((1010,1660),'تعال ',font=DB(80),fill=WHITE,direction='rtl',anchor='rs'); dd.text((1010-w,1660),'بكّيـــر',font=DB(80),fill=WHITE,direction='rtl',anchor='rs')

st.convert('RGB').save(S+'out/hours_story.jpg',quality=95); print('ok')
