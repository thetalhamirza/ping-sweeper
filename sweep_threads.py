import sys
import os
from scapy.all import ICMP, IP, sr1
from netaddr import IPNetwork
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping_host(host):
    response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)      
    return str(host) if response is not None else None

def ping_sweep(network, netmask, max_threads):
    live_hosts = []
    ip_network = IPNetwork(network + '/' + netmask)
    hosts = list(ip_network.iter_hosts())

    print(f"Number of threads: {max_threads}")

    print(f"Scanning {len(hosts)} hosts...")

    with ThreadPoolExecutor(max_threads=50) as executor:
        future_to_host = {executor.submit(ping_host, host): host for host in hosts}
        for i,future in enumerate(as_completed(future_to_host)):
            host = future_to_host[future]
            try:
                result = future.result()
                if result:
                    live_hosts.append(result)
                    print(f"Host {host} is online.")
            except Exception as e:
                print(f"Error scanning host {host}: {e}")
            print(f"Scanned: {i+1}/{len(hosts)}", end="\r", flush=True)

    return live_hosts

def main():
    if os.geteuid() != 0:       # checking root
        print("This script requires root privileges.")
        sys.exit(1)


    if len(sys.argv) < 3:
        print("Usage: python3 sweep.py <network> <netmask> [threads]")
        sys.exit(1)
    
    network = sys.argv[1]
    netmask = sys.argv[2]

    max_threads = 50

    if len(sys.argv) >= 4:
        try:
            max_threads = int(sys.argv[3])
            if max_threads < 1:
                raise ValueError
        except ValueError:
            print("Error: Number of threads must be a positive integer.")
            sys.exit(1)

    live_hosts = ping_sweep(network, netmask, max_threads)
    print("\nCompleted")
    print(f"Live hosts: {live_hosts}")






if __name__=="__main__":
    main()