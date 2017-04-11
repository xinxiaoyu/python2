import re

f = open(r'F:\user\langyaofeng\Desktop\abc.txt','r')
for y,x in enumerate(f):
    pass
y = y + 1
f.close()

f1 = open(r'F:\user\langyaofeng\Desktop\abc.txt','r')
f2 = open(r'F:\user\langyaofeng\Desktop\def.txt','w')
f2.truncate()

count = 1
for i in f1:
    if y == count:
        m = re.sub(r'(.+)',r"'\1'",i)
        f2.write(m)
    else:
        m = re.sub(r'(.+)',r"'\1',",i)
        f2.write(m)
    count = count + 1

f2.close()
f1.close()

