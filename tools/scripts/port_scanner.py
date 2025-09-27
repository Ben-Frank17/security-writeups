#!/usr/bin/env python3
"""
Basic Port Scanner - My First Security Tool
Author: Braxton
Educational use only!
"""

import socket
import sys
from datetime import datetime

def simple_port_scanner(target, ports):
    """
    Simple port scanner for learning purposes
    """
    print(f"Scanning target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)
    
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            
            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")
            
            sock.close()
            
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

if __name__ == "__main__":
    # Define target and ports to scan
    target = "scanme.nmap.org"  # NMAP's test server (legal to scan)
    ports = [21, 22, 80, 443, 8080]  # Common ports
    
    print("🔒 Basic Port Scanner - Educational Use Only")
    print("⚠️  Only scan systems you own or have permission to scan!")
    print("📚 Learning: Socket programming, network basics")
    print()
    
    simple_port_scanner(target, ports)
