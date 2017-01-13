 #get my private ip
 def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
    
 #get public ip
 from urllib.request import urlopen
 import re
 def getPublicIp():
     data = str(urlopen('http://checkip.dyndns.com/').read())
	   return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
