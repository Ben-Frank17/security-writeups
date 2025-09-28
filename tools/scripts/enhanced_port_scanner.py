#!/usr/bin/env python3
"""
Enhanced Port Scanner - Braxton's Security Tool v2
Added features: Colors, save to file, custom ports
"""

import socket
import sys
from datetime import datetime
import argparse

# Color codes for better output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def scan_port(target, port):
    """Scan a single port and return result"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except:
        return False

def enhanced_port_scanner(target, ports, output_file=None):
    """Enhanced port scanner with better output and logging"""
    print(f"{Colors.BLUE}🔒 Enhanced Port Scanner - By Braxton{Colors.END}")
    print(f"{Colors.YELLOW}⚠️  Educational Use Only!{Colors.END}")
    print(f"Target: {Colors.GREEN}{target}{Colors.END}")
    print(f"Time: {datetime.now()}")
    print("-" * 60)
    
    open_ports = []
    
    for port in ports:
        is_open = scan_port(target, port)
        status = f"{Colors.GREEN}Open{Colors.END}" if is_open else f"{Colors.RED}Closed{Colors.END}"
        print(f"Port {port:5}: {status}")
        
        if is_open:
            open_ports.append(port)
    
    # Summary
    print(f"{Colors.BLUE}\n📊 Scan Summary:{Colors.END}")
    print(f"Open ports: {Colors.GREEN}{open_ports}{Colors.END}")
    print(f"Total ports scanned: {len(ports)}")
    
    # Save to file if requested
    if output_file:
        with open(output_file, 'w') as f:
            f.write(f"Port Scan Results - {datetime.now()}\n")
            f.write(f"Target: {target}\n")
            f.write(f"Open ports: {open_ports}\n")
        print(f"{Colors.GREEN}Results saved to: {output_file}{Colors.END}")

def main():
    parser = argparse.ArgumentParser(description='Enhanced Port Scanner')
    parser.add_argument('-t', '--target', default='scanme.nmap.org', help='Target to scan')
    parser.add_argument('-p', '--ports', default='21,22,80,443,8080', help='Ports to scan (comma-separated)')
    parser.add_argument('-o', '--output', help='Save results to file')
    
    args = parser.parse_args()
    
    # Parse ports
    ports = [int(p) for p in args.ports.split(',')]
    
    enhanced_port_scanner(args.target, ports, args.output)

if __name__ == "__main__":
    main()
