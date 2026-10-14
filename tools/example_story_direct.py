import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'story.py')).read())
def direct(n,src,l1,a,b,lab,arr):
    global W,H
    W,H=SW,SH
    st=cover(Image.open(S+'gen10/'+src).convert('RGB')).convert('RGBA')
    scrim(st,(380,220,1060,600),120)
    headline(st,1010,330,l1,a,b,DB(88),gap=112)
    lx,ly,bo,su=lab; label(st,lx,ly,bo,su,arr)
    g=Image.new('L',(1,SH))
    for y in range(SH): g.putpixel((0,y),int(255*min(1,max(0,(y-SH*.80)/(SH*.20))**1.2*.75)))
    st.alpha_composite(Image.merge('RGBA',(*Image.new('RGB',(SW,SH),(8,10,10)).split(),g.resize((SW,SH)))))
    H=1700; footer(st,ImageDraw.Draw(st)); H=SH
    d=ImageDraw.Draw(st); f=SB(34); t='تعال جرّبه اليوم'; w=tw(d,t,f)
    d.rounded_rectangle([1010-w-60,490,1010,556],radius=33,fill=(47,112,104)); d.text((1010-30,536),t,font=f,fill=WHITE,direction='rtl',anchor='rs')
    W,H=1080,1350
    st.convert('RGB').save(S+f'out/story{n:02d}.jpg',quality=95)
direct(7,'v07.png','ارفعهـــا...','وخلّي الكل ','يغـــار',(1010,920,'ميلك شيـــك','أوريو'),[(840,900),(780,890),(720,910),(665,950)])
direct(9,'v09.png','الكرسي محجوز...','','إلـــك',(400,880,'هوت','شوكليـــت'),[(330,920),(360,975),(410,1005),(455,1015)])
