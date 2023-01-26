import re

pattern = re.compile(r'(\d+.){3}(\d+)')
print(pattern.pattern, pattern.flags, pattern.groups, pattern.groupindex, sep='  ', end='\n')

s = 'abc1fg12h'
s = 'abc192.168.0.1--192.168.1.1'
print(len(s))
try:
    match = pattern.match(s)
    if match != None:
        print(match, match.string, match.re, match.pos, match.endpos, match.lastindex, match.lastgroup, sep='  ', end='\n')
    search = pattern.search(s)
    if search != None:
        print(search, search.string, search.re, search.pos, search.endpos, search.lastindex, search.lastgroup, sep='  ', end='\n')
    print(pattern.findall(s))
    print(pattern.split(s))
    print(pattern.sub('x', s))
except:
    pass
'''
<_sre.SRE_Match object; span=(0,  3),  match='192'>
<_sre.SRE_Match object; span=(0,  3),  match='192'>
['192',  '168',  '0',  '1']
['',  '.',  '.',  '.',  '']
x.x.x.x
'''