#!/usr/bin/python3
from scapy.all import *

def spoof_pkt(pkt):
    print("\nOriginal packet sniffed:")
    print("Source IP:", pkt[IP].src)
    print("Destination IP:", pkt[IP].dst)
    print("Upper Layer Protocol:", pkt[IP].proto)
    print("TTL value:", pkt[IP].ttl)

    # Only spoof ICMP packets
    if pkt[IP].proto == 1:  # 1 = ICMP
        if pkt[ICMP].type == 0:  # Echo reply
            # Build a spoofed echo request
            ip = IP(src='10.0.1.15', dst=pkt[IP].src, ttl=64)
            icmp = ICMP(type=8, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
            data = "Test Msg"
            newPkt = ip / icmp / data

            send(newPkt, verbose=0)
            print("Spoofed packet sent: {} -> {}".format(ip.src, ip.dst))

print("Starting sniffer... press Ctrl+C to stop.")
sniff(filter='icmp', prn=spoof_pkt)
