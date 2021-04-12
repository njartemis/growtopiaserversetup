import os, sys, requests
from time import sleep

# Banner
banner = """
    _       _       ___      _             
   /_\ _  _| |_ ___/ __| ___| |_ _  _ _ __ 
  / _ \ || |  _/ _ \__ \/ -_)  _| || | '_ |
 /_/ \_\_,_|\__\___/___/\___|\__|\_,_| .__/
                                     |_|   

            GrowtopiaServer-Setup
            Author   :   Artemis
       This program allows you to setup
    GTPS automatically, and not complicated.
"""

# UI
print(banner)
ask = input("? | Do you want to start the setup sections? : ")

# Functions
print("! | Turning off Windows Firewall...")
sleep(5)
os.system("netsh Advfirewall set publicprofile state off")
print("✓ | Windows Firewall has been turned off.")
sleep(3)
print("! | Adding TCP Port and UDP Port...")
sleep(3)
os.system("netsh firewall add portopening TCP 80 80")
print("✓ | TCP is setted up.")
sleep(3)
os.system("netsh firewall add portopening UDP 17091 17091")
print("✓ | UDP is setted up!")

if not os.path.exists('C://xampp/htdocs/'):
    print("! | Downloading XAMPP...")
    url = "https://www.apachefriends.org/xampp-files/7.3.27/xampp-windows-x64-7.3.27-1-VC15-installer.exe"
    r = requests.get(url, allow_redirects=True)
    open('xampp-windows-x64-7.3.27-1-VC15-installer.exe','wb').write(r.content)
    
    sleep(5)
    print("✓ | XAMPP has been installed!")
elif os.path.exists('C://xampp/htdocs/'):
    print("✓ | XAMPP already exists.")

# Server data
askdata = input("? | Do you want to make server data? (yes/no) : ")
if askdata == "yes":
    ip = input("! | Server IP : ")
    sport = input("! | UDP Port : ")
    maint = input("! | Maintenance Message : ")
    sd = open("server_data.php","w")
    sd.write(
    f"server|{ip}\nport|{sport}\ntype|1\n#maint|{maint}\n\nbeta_server|127.0.0.1\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001"
)
    sd.close()
    print("✓ | Server data has been created!")

print("✓ | The setup is completed, now start your server!")

sleep(100)