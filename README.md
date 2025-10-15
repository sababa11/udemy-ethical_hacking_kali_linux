# udemy-ethical_hacking_kali_linux
## Udemy - Ethical Hacking With Python, JavaScript and Kali Linux  

### In Kali Linux use next tools:  
netdiscover -i eth0 -r 10.0.2.1/24  
zenmap     -- better tool to scan the network (uses nmap as a core command)  
airmon-ng  -- wlan tool that makes possible to cahange status from Managed to Monitor mode  
iwconfig wlan0 mode monitor  -- manually change mode to Monitor (used after executing "ifconfig wlan0 down/up")  
  
fern - GUI application to crack WI-FI  
airodump-ng --bssid --channel 6 --write demo-handshake wlan0mon  --capturing connection handshake  
aireplay-ng --deauth 4 -a (BSSID) -c (STA) wlan0mon  --force disconnect station and capture with previous app WPA handshake  
aircrack-ng demo-handshake-01.cap -w wordlist  --will crack demo-handshake against generated wordlist  