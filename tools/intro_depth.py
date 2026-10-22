src=open('/tmp/claude-0/-home-user-nusscafee/f7fad810-a083-54af-b56f-880f141af58a/scratchpad/pcombo.py').read()
exec(src[:src.index('C=[\n')])
O=S+'out/depth/'; os.makedirs(O,exist_ok=True)
def pill(img,t):
    d=ImageDraw.Draw(img); f=SB(28); w=tw(d,t,f); XR=1010
    d.rounded_rectangle([XR-w-44,60,XR,110],radius=25,fill=TEAL); d.text((XR-22,97),t,font=f,fill=WHITE,direction='rtl',anchor='rs')
def giant(img,t,y,size):
    d=ImageDraw.Draw(img); f=DBk(size)
    while tw(d,t,f)>980: f=DBk(f.size-6)
    w=tw(d,t,f); xr=W/2+w/2
    hl(img,d,xr,y,t,f,pad=(26,6),skew=12); d=ImageDraw.Draw(img); d.text((xr,y),t,font=f,fill=WHITE,direction='rtl',anchor='rs')
P=[
 (13,'o5','آيس لاتيه','وحدة إلـــك... ووحدة لصاحبتـــك','آيس لاتيـــه',405,200,
  [(1010,800,'آيس لاتيه','بارد وطبقات',[(880,840),(830,870),(770,905)])],'وحدة إلك ووحدة لصاحبتك… هيك الصحبة 🤍','#آيس_لاتيه'),
 (14,'o6','آيس سبانش لاتيه','على مهلـــك... الدنيا مش طايـــرة','سبانش لاتيـــه',395,185,
  [(1010,700,'آيس سبانش لاتيه','ناعم وطبقات',[(860,740),(760,760),(620,775)])],'ناعم من برّا، وقلبه إسبريسو… على مهلك 🤎','#سبانش_لاتيه'),
 (12,'o4','آيس أمريكانو','الغروب حلـــو... والأمريكانو أحلـــى','أمريكانـــو',470,220,
  [(1010,880,'آيس أمريكانو','بارد ومن الآخر',[(880,900),(720,930),(575,945)])],'بارد، صريح، ومن الآخر… متل الغروب 🌅','#آيس_أمريكانو'),
]
caps=[]
for i,name,pl,l1,gw,gy,gs,labs,cap,tag in P:
    base=cover(Image.open(S+f'owner/o{i}.png').convert('RGB')); im=topdark(base,520,180)
    fg=im.copy(); mask=cover(Image.open(S+f'owner/m{i}.png').convert('L')).filter(ImageFilter.GaussianBlur(1.2))
    CUR[0]=im.copy()
    pill(im,pl); d=ImageDraw.Draw(im); T(d,1010,200,l1,DB(52),WHITE)
    giant(im,gw,gy,gs)
    im.paste(fg,(0,0),mask)                     # subject in front of the text
    for lab in labs: mlabel(im,*lab)
    footer_c(im); im.convert('RGB').save(O+name+'.jpg',quality=95); caps.append((name,cap,tag))
sh=Image.new('RGB',(3*400+20,500),(30,30,30))
for k,(n,_,_) in enumerate(caps): sh.paste(Image.open(O+n+'.jpg').resize((400,500)),(k*410,0))
sh.save(O+'preview.jpg')
import json; json.dump(caps,open(O+'caps.json','w'),ensure_ascii=False); print('ok')
