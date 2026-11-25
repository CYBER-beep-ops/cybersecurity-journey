
import socket

target = "127.0.0.1"

ports = [22, 53, 80, 443, 8000, 8080]
print("CYBERSECURITY PORT SCANNER")
print("--------------------------")
print(f"Scanning your own computer: {target}\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    sock.close()

print("\nScan completed.")
