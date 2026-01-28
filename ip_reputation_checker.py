# ip_reputation_checker.py
# Simple IP reputation checker for cybersecurity use cases

# Simulated blacklist of malicious IPs
blacklisted_ips = {
    "192.168.1.10",
    "203.0.113.45",
    "45.33.32.156"
}

def check_ip_reputation(ip_address):
    if ip_address in blacklisted_ips:
        return f"⚠️  {ip_address} is flagged as MALICIOUS"
    else:
        return f"✅ {ip_address} is not found in blacklist"

# Example usage
ip = input("Enter IP address to check: ")
result = check_ip_reputation(ip)
print(result)
