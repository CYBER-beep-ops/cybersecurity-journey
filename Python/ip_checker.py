
import ipaddress

print("CYBERSECURITY IP ADDRESS CHECKER")
print("--------------------------------")

ip = input("Enter an IP address: ")

try:
    address = ipaddress.ip_address(ip)

    print("\nIP ADDRESS INFORMATION")
    print("Address:", address)
    print("Version: IPv", address.version)
    print("Private address:", address.is_private)
    print("Valid IP address: Yes")

except ValueError:
    print("Invalid IP address. Please try again.")
