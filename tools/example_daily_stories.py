import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'story.py')).read())
import sys
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'example_daily_posts.py')).read(); exec(src[src.index('P=['):src.index('for n,XR')])
only=[int(x) for x in sys.argv[1:]] or range(1,11)
for n,XR,y1,l1,a,b,lab,arr,sb in P:
    if n==4: lab,arr=(1030,640,'سان سيباستيـــان','مع شوكولا وبستاشيو'),[(880,670),(800,700),(730,740),(700,770)]
    if n in only: print(n,round(make_story(n,XR,y1,l1,a,b,lab,arr),3))
