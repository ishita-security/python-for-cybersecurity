# log_analysis.py
# Simple log analysis script for cybersecurity use cases

from collections import defaultdict

# Sample log data (simulating authentication logs)
logs = [
    "192.168.1.10 - Failed login",
    "192.168.1.10 - Failed login",
    "192.168.1.10 - Failed login",
    "192.168.1.12 - Successful login",
    "192.168.1.15 - Failed login",
    "192.168.1.15 - Failed login",
    "192.168.1.20 - Successful login"
]

failed_attempts = defaultdict(int)

# Analyze logs
for log in logs:
    if "Failed" in log:
        ip = log.split(" ")[0]
        failed_attempts[ip] += 1

# Flag suspicious IPs
print("Suspicious IPs with multiple failed login attempts:\n")

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"⚠️  {ip} has {count} failed login attempts")
