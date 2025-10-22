import scapy.all as scapy


def scanner(ip_addr):
    # scapy.arping(ip_addr)

    request = scapy.ARP(pdst=ip_addr)  # ARP request created
    # request.show()
    request.pdst = ip_addr
    # print(request.summary())
    # scapy.ls(scapy.ARP())

    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"  # Broadcast MAC
    broadcast.show()

    request_broadcast = broadcast/request
    request_broadcast.show()

    resp1, resp2 = scapy.srp(request_broadcast, timeout=1, verbose=False)
    for element in resp1:
        print(element[1].psrc)
        print(element[1].hwsrc)

def main():
    scanner('10.100.102.1/24')

if __name__ == "__main__":
    main()
