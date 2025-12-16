# Blacklist vs Whitelist Firewall Policies

## Objective
Demonstrate the behavioral differences between blacklist-based and whitelist-based firewall policies on a Linux system using iptables.

## Environment
- Two Linux virtual machines (VM1: firewall/target, VM2: tester)
- Network modes: NAT and Host-Only
- Tools: iptables, curl, ping

## Configuration
This lab tested both approaches:

### Blacklist Policy
- Default policies: INPUT ACCEPT, OUTPUT ACCEPT
- Explicit REJECT rules for outbound HTTP/HTTPS traffic
- Inbound web service allowed

### Whitelist Policy
- Default policies: INPUT DROP, OUTPUT DROP
- Explicit allows for:
  - ESTABLISHED,RELATED traffic
  - Loopback
  - ICMP echo-request/echo-reply
  - Selected TCP ports (SSH, HTTP/HTTPS)

## Verification
- curl tests confirmed outbound web traffic was blocked under blacklist rules
- VM2 could still access VM1’s HTTP service
- Under whitelist rules, only explicitly allowed traffic succeeded
- iptables counters confirmed rule matches

## Key Takeaways
- Blacklist policies are easier to configure but risk unintended exposure
- Whitelist policies enforce least privilege but require careful planning
- Default DROP policies significantly reduce attack surface

