import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'example_daily_posts.py')).read().split("for n,XR")[0])
import numpy as np
SW,SH=1080,1920
def find_off(exp,orig):
    e=np.asarray(exp.convert('L').resize((184,328)),dtype=float)
    o=orig.convert('L'); oh=round(o.height*184/o.width); o=np.asarray(o.resize((184,oh)),dtype=float)
    best=min(range(0,328-oh+1),key=lambda y: np.abs(e[y:y+oh]-o).mean())
    return best/328  # fraction of height
def make_story(n,XR,y1,l1,a,b,lab,arr):
    exp=Image.open(S+f'gen10/st{n:02d}.png').convert('RGB'); orig=Image.open(S+f'gen10/d{n:02d}.png').convert('RGB')
    fy=find_off(exp,orig)
    big=exp.resize((SW,round(exp.height*SW/exp.width)),Image.LANCZOS)
    oh=round(orig.height*SW/orig.width); o=orig.resize((SW,oh),Image.LANCZOS)
    yo=round(fy*big.height)
    m=Image.new('L',(SW,oh),255); md=ImageDraw.Draw(m)
    for i in range(70): v=int(255*i/70); md.line([(0,i),(SW,i)],fill=v); md.line([(0,oh-1-i),(SW,oh-1-i)],fill=v)
    big.paste(o,(0,yo),m); st=big.crop((0,0,SW,SH)).convert('RGBA')
    global W,H
    W,H=SW,SH
    # crop offset of post (cover) inside original: post y = (orig_y*scale) ; post was cover() of orig to 1080x1350
    s_post=max(1080/orig.width,1350/orig.height); s_st=SW/orig.width
    oy_post=(orig.height*s_post-1350)/2; ox_post=(orig.width*s_post-1080)/2
    mp=lambda x,y: (round((x+ox_post)/s_post*s_st), round((y+oy_post)/s_post*s_st)+yo)
    scrim(st,(380,220,1060,600),120)
    headline(st,1010,330,l1,a,b,DB(88),gap=112)
    lx,ly,bo,su=lab; X,Y=mp(lx,ly)
    label(st,X,Y,bo,su,[mp(*p) for p in arr])
    g=Image.new('L',(1,SH))
    for y in range(SH): g.putpixel((0,y),int(255*min(1,max(0,(y-SH*.80)/(SH*.20))**1.2*.75)))
    st.alpha_composite(Image.merge('RGBA',(*Image.new('RGB',(SW,SH),(8,10,10)).split(),g.resize((SW,SH)))))
    H=1700; footer(st,ImageDraw.Draw(st)); H=SH
    # CTA chip
    d=ImageDraw.Draw(st); f=SB(34); t='تعال جرّبه اليوم'
    w=tw(d,t,f); d.rounded_rectangle([1010-w-60,490,1010,556],radius=33,fill=(47,112,104))
    d.text((1010-30,536),t,font=f,fill=WHITE,direction='rtl',anchor='rs')
    W,H=1080,1350
    st.convert('RGB').save(S+f'out/story{n:02d}.jpg',quality=95)
    return fy
