# Ping Sweeper

This repository contains two Python scripts for performing a ping sweep to identify live hosts on a network.

## Scripts

### 1. `sweep.py`

A basic ping sweep script that scans a given network sequentially.

#### Features:

- Uses `scapy` to send ICMP Echo Requests.
- Displays progress while scanning.
- Identifies live hosts.
- Requires root privileges.

#### Usage:

```sh
sudo python3 sweep.py <network> <netmask>
```

Example:

```sh
sudo python3 sweep.py 192.168.1.0 24
```

#### Example Output:

```
[+] Scanning: 5/254
[+] Host 192.168.1.5 is online.
[+] Scanning: 10/254
[+] Host 192.168.1.10 is online.
[+] Completed
[+] Live hosts:
--> 192.168.1.5
--> 192.168.1.10
```

### 2. `sweep_pro.py`

An advanced ping sweep script with multithreading support for faster scanning.

#### Features:

- Uses `ThreadPoolExecutor` for concurrent scanning.
- Allows customizable number of threads (default: 50).
- Uses `colorama` and `termcolor` for colored output.
- Displays real-time progress.
- Identifies live hosts efficiently.
- Requires root privileges.

#### Usage:

```sh
sudo python3 sweep_pro.py <network> <netmask> [threads]
```

Example:

```sh
sudo python3 sweep_pro.py 192.168.1.0 24 100
```

#### Example Output:

```
[+] Number of threads: 100
[+] Scanning 254 hosts...
[+] Host 192.168.1.5 is online.
[+] Host 192.168.1.10 is online.
[+] Scanned: 254/254
[+] Completed
[+] Live hosts:
--> 192.168.1.5
--> 192.168.1.10
```

## Dependencies

Ensure you have the following Python libraries installed:

```sh
pip install scapy netaddr colorama termcolor
```

## Credits

These scripts were developed with guidance from [faanross](https://github.com/faanross), who provided a tutorial and valuable insights. Additional improvements, such as threading and enhanced output formatting, were contributed by the author of this repository.

## Disclaimer

**Use these scripts responsibly and only on networks you have permission to scan. Unauthorized scanning may violate legal and ethical guidelines.**
