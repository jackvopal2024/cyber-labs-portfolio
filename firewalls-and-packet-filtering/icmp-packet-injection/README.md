# ICMP Packet Injection

This lab demonstrates how ICMP packets can be forged and injected into a network using Python and Scapy. By crafting spoofed ICMP echo requests, I observed how a target host processes packets that appear to originate from a trusted source.

## Environment
- Two Linux virtual machines
  - Attacker VM
  - Victim VM
- Network mode: Host-only
- Tools: Python, Scapy, tcpdump

## Attack Overview
- Crafted ICMP echo-request packets with a spoofed source IP
- Injected packets directly onto the network
- Verified whether the victim responded to the spoofed sender
- Observed traffic at both the attacker and victim

## Verification
Packet injection was verified by:
- Capturing traffic with tcpdump on the victim
- Confirming ICMP echo requests arrived with a forged source IP
- Observing ICMP echo replies sent to the spoofed address

## Key Takeaways
- ICMP does not provide authentication of packet origin
- Hosts respond to ICMP requests based solely on packet contents
- Packet injection can be used to manipulate network behavior if filtering is absent
