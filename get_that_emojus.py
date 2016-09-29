import sys
import urllib.request
import json

f = urllib.request.urlopen('https://slack.com/api/emoji.list?token=' + sys.argv[1])
s = f.read().decode('utf-8')
emojidict = json.loads(s)
count = 0
for k,v in emojidict['emoji'].items():
    if v.startswith('alias'):
        continue
    dlname = k + v[v.rfind('.'):]
    print(dlname)
    #urllib.request.urlretrieve (v, dlname)
    count += 1
print(count, 'emoji downloaded.')
