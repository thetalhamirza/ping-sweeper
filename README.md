# Ping Sweeper

A Python-based network scanning tool that detects active hosts within a given subnet using **ICMP ping requests**. It is designed for **fast and efficient scanning** using **multithreading**, making it useful for network reconnaissance and security assessments.

## Features

- **Multithreaded Scanning** – Scans multiple hosts simultaneously for faster results.
    
- **ICMP-Based Host Detection** – Identifies live devices using ICMP echo requests.
    
- **Automatic Timeout Handling** – Skips unresponsive hosts to improve efficiency.
    
- **Real-Time Progress Tracking** – Displays live scan updates and results.
    
- **Customizable Thread Count** – Users can adjust the number of threads for optimal performance.
    

## Installation

### **Prerequisites**

Ensure you have Python 3 installed along with the required dependencies:

```
pip install scapy netaddr colorama termcolor
```

## Usage

Run the script with the following command:

```
sudo python3 sweep_pro.py <network> <netmask> [threads]
```

### **Arguments:**

- `<network>` – The base network address (e.g., `192.168.1.0`)
    
- `<netmask>` – The subnet mask (e.g., `24` for `/24`)
    
- `[threads]` _(optional)_ – Number of concurrent threads (default: `50`)
    

### **Example Usage:**

```
sudo python3 sweep_pro.py 192.168.1.0 24 100
```

This will scan the **192.168.1.0/24** network using **100 threads** for faster execution.

## How It Works

1. The tool takes a **network address** and **subnet mask** as input.
    
2. It generates all possible **host IPs** in the subnet.
    
3. Each IP is sent an **ICMP echo request** (ping).
    
4. If a response is received, the host is marked **online**.
    
5. The tool provides **real-time progress updates** and a final list of active hosts.
    

## Screenshots

Example output of a successful scan:

```
[+] Scanning 254 hosts...
[+] Host 192.168.1.1 is online.
[+] Host 192.168.1.100 is online.
[+] Host 192.168.1.150 is online.
[+] Completed

[+] Live hosts:
--> 192.168.1.1
--> 192.168.1.100
--> 192.168.1.150
```

## Disclaimer

This tool is intended for **educational and ethical purposes only**. Do not use it on networks without **explicit permission**. Unauthorized scanning may be illegal in some regions.

## Credits

Special thanks to **faanross** for creating a really good tutorial that helped in building this tool.

## Contributing

Feel free to contribute to this project! If you have suggestions or improvements, submit a pull request.

## License

This project is open-source and available under the **MIT License**.

## Author

Developed by **Talha** as part of learning cybersecurity and network reconnaissance.
