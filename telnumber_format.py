import re

f1 = open(r'F:\user\langyaofeng\Desktop\abc.txt','r')

f2 = open(r'F:\user\langyaofeng\Desktop\def.txt','a')
f2.truncate()

for i in f1:
    m = re.sub(r'(\d\d\d\d\d\d\d\d\d\d\d)',r"\'\1\',",i)
    n = re.sub(r'\\',r'',m)
    f2.write(n)

f2.close()
f1.close()
