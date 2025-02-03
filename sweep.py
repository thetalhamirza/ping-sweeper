import sys
import os
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import ICMP, IP, sr1
from netaddr import IPNetwork
from colorama import init
from termcolor import colored

init()

def ping_sweep(network, netmask):
    live_hosts = []
    total_hosts = 0
    scanned_hosts = 0

    ip_network = IPNetwork(network + '/' + netmask)
    for host in ip_network.iter_hosts():
        total_hosts += 1

    for host in ip_network.iter_hosts():
        scanned_hosts += 1
        print(f"[+] Scanning: {scanned_hosts}/{total_hosts}", end="\r")
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is not None:
            live_hosts.append(str(host))
            print(f"[+] Host {host} is online.")

    return live_hosts


def main():
    if os.geteuid() != 0:       # checking root
        print("[!] This script requires root privileges.")
        sys.exit(1)


    network = sys.argv[1]
    netmask = sys.argv[2]

    live_hosts = ping_sweep(network, netmask)
    print(colored("\n[+] Completed", "green"))
    print(colored(f"[+] Live hosts:\n\n", "green"))
    for host in live_hosts:
        print(colored(f"--> {host}", "green"))


if __name__=="__main__":
    main()