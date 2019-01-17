import os
s=input("Enter Wifi Name(ssid):")
os.system('netsh wlan show profile "'+s+'" key=clear > tmp.tmp')
f=open("tmp.tmp","r")
for l in f.readlines():
        if "Profile \""+s+"\" is not found on the system" in l:
                print("Password not found!!!")
                break
        if "Key Content" in l:
                print(l.replace("Key Content","Password").strip())           
f.close()
os.unlink("tmp.tmp")
input()
