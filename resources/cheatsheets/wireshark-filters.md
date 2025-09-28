# Useful Wireshark Filters

## IP Address Filters
- ip.addr == 10.0.0.1 - Traffic to/from specific IP
- ip.src == 10.0.0.1 - Traffic from specific IP
- !(ip.addr == 10.0.0.1) - Exclude specific IP

## Protocol Filters  
- tcp.port == 80 - HTTP traffic
- udp.port == 53 - DNS traffic
- icmp - ICMP packets only

## Advanced Filters
- http.request.method == "GET" - HTTP GET requests
- tcp.flags.syn == 1 - TCP SYN packets
- frame.len > 1000 - Large packets only

Essential for network analysis and CTFs!
