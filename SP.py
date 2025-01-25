import socket
import argparse
from typing import List


def scan_port(target: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1.0)
            result = sock.connect_ex((target, port))
            return result == 0  
    except Exception:
        return False


def scan_target(target: str, ports: List[int]) -> None:
    print(f"Scanning target: {target}")
    for port in ports:
        if scan_port(target, port):
            print(f"[+] Port {port} is open")
        else:
            print(f"[-] Port {port} is closed")


def main():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-p", "--ports", required=True, help="(e.g., 22,80,443)")

    args = parser.parse_args()
    target = args.target
    ports = [int(port) for port in args.ports.split(",")]

    scan_target(target, ports)


if __name__ == "__main__":
    main()
