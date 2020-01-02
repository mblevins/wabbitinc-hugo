# modify caps
import sys
import re

md=sys.stdin.read()
done=False
regex = r'\\\[caption.*caption="([^"]+)".*(http:[^)]+)\).*http:.*\\\[/caption\\\]'
#regex = r'caption'
loc=0
done=False
while not done:
    m=re.search( regex, md[loc:] )
    if m:
        md=md[:m.start()] + '\n{{{{< figure src="{}" caption="*{}*" >}}}}\n'.format( m.group(2), m.group(1) ) + md[m.end()+1:]
        loc=loc+1
    else:
        done=True


regex = r'\\\[caption.*(http:[^)]+)\).*http:[^)]+\)(.*)\\\[/caption\\\]'
loc=0
done=False
while not done:
    m=re.search( regex, md[loc:] )
    if m:
        md=md[:m.start()] + '\n{{{{< figure src="{}" caption="*{}*" >}}}}\n'.format( m.group(1), m.group(2).strip() ) + md[m.end()+1:]
        loc=loc+1
    else:
        done=True


print(md)
