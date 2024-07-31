import socket

def scan_port(ip, port):
    """Scan a specific port on an IP address."""
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the socket
        sock.settimeout(1)
        # Try to connect to the port
        result = sock.connect_ex((ip, port))
        # Check if the port is open
        if result == 0:
            print(f"Port {port} is open on {ip}")
        sock.close()
    except Exception as e:
        print(f"Error scanning {ip}:{port} - {e}")

def scan_ip_range(start_ip, end_ip, ports):
    """Scan a range of IPs on specific ports."""
    # Convert IPs to integers
    start_int = ip_to_int(start_ip)
    end_int = ip_to_int(end_ip)

    # Iterate over the IP range
    for ip_int in range(start_int, end_int + 1):
        ip = int_to_ip(ip_int)
        print(f"Scanning IP: {ip}")
        for port in ports:
            scan_port(ip, port)

def ip_to_int(ip):
    """Convert an IP string to an integer."""
    return int.from_bytes(socket.inet_aton(ip), 'big')

def int_to_ip(ip_int):
    """Convert an integer to an IP string."""
    return socket.inet_ntoa(ip_int.to_bytes(4, 'big'))

# Define IP range and ports to scan
start_ip = "192.168.1.1"
end_ip = "192.168.1.10"
ports = [22, 80, 443]  # Example ports to scan

# Start scanning
scan_ip_range(start_ip, end_ip, ports)
