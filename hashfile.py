import hashlib
import time

filename = r'F:\user\langyaofeng\Desktop\abc.txt'
hashfile = hashlib.md5(open(filename, 'rb').read()).hexdigest()

print hashfile

time.sleep(10)
