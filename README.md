# SP1
A lightweight Python port scanner for basic network reconnaissance for my project cybersecurity.

## Requirements

- Python 3.6 or higher
- Standard Python libraries (socket, argparse, typing)

## Installation

 Clone the repository:
```bash
git clone https://github.com/miraclegalaxys/SP1.git
cd SP1
```

## Usage

Command syntax:
```bash
python scanner.py -t TARGET -p PORTS
```

Examples:
```bash
# Scan specific ports
python scanner.py -t 192.168.1.1 -p 80,443,8080

# Scan a hostname
python scanner.py -t example.com -p 22,80,443
```

### Arguments

- `-t, --target`: Target IP address or hostname (required)
- `-p, --ports`: Comma-separated list of ports to scan (required)

## Output

The scanner will display results in the following format:
```
Scanning target: 192.168.1.1
[+] Port 80 is open
[-] Port 443 is closed
```

## Security Notice

Only use this tool on networks you own or have explicit permission to test.

## License

[MIT License](LICENSE)

## Author

By ggalaxys_
