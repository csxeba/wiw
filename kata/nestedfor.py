import socket

# Az alábbi listában találsz néhány IP címet.
# Futtass le rajtuk egy portscant az első 100 porton!
# A portscan nevű függvénnyel tudsz portot scannelni :)

def portscan(ip, port):
  try:
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.settimeout(0.1)
    
    result = sck.connect_ex((ip, port))
    if result == 0:
      print("{0}:{1} OPEN!".format(ip, port))
    else:
      print("{0}:{1} CLOSED!".format(ip, port))
    sck.close()
  except KeyboardInterrupt:
    print("Stopped!")
    quit()
  except socket.gaierror:
    print("Hostname cannot be resolved")
    quit()
  except socket.error:
    print("Connection cannot be established")
    quit()
     

# Ne feledd, ifjú padawan, a portokat 0-tól számozzuk!

ip_cimek = [
  "192.168.1.2",
  "192.168.1.3",
  "192.168.1.4",
  "192.168.1.5"
  ]
