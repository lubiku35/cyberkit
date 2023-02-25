import socket

target_domain = "www.michalmuskolay.com"

try:
    ip_address = socket.gethostbyname(target_domain)
    print("IP address:", ip_address)
except socket.gaierror:
    print("Failed to get IP address for target domain")