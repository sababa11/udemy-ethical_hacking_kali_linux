'''
# Prerequesites:
pip install python-nmap  (Python package)
apt-get install nmap     (NMAP app on the host)
'''
import nmap


def main():
    scanner = nmap.PortScanner()
    print("Welcome to the NMAP scanner!")
    ip_addr = input("Enter the IP address to scan: ")
    print("The IP address is: ", ip_addr)
    type(ip_addr)
    read = input("""\nPlease enter the type of scan you want to perform:
    1. SYN ACK Scan
    2. UDP Scan
    3. Comprehensive scan\n""")
    print("The type of scan is: ", read)
    print("NMAP version: %s", scanner.nmap_version())

    if read == "1":
        scanner.scan(ip_addr, '1-1024', arguments="-v -sS")
        print(scanner.scaninfo())
        print("IP status: %s", scanner[ip_addr])
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: %s", scanner[ip_addr]['tcp'].keys())
    elif read == "2":
        scanner.scan(ip_addr, '1-1024', arguments="-v -sU")
        print(scanner.scaninfo())
        print("IP status: %s", scanner[ip_addr])
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: %s", scanner[ip_addr]['udp'].keys())
    elif read == "3":
        scanner.scan(ip_addr, '1-1024', arguments="-v -sS -sV -sC -A -O")
        print(scanner.scaninfo())
        print("IP status: %s", scanner[ip_addr])
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: %s", scanner[ip_addr]['tcp'].keys())
    else:
        print("Please enter a valid option (1, 2 or 3)")

if __name__ == "__main__":
    main()
