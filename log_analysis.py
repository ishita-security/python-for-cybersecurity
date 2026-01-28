# log_analysis.py
# Log file analysis for detecting suspicious login attempts

from collections import defaultdict

LOG_FILE = "auth.log"
THRESHOLD = 3

failed_attempts = defaultdict(int)

try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Failed login" in line:
                ip = line.split()[0]
                failed_attempts[ip] += 1

    print("\nSuspicious IPs with multiple failed login attempts:\n")

    for ip, count in failed_attempts.items():
        if count >= THRESHOLD:
            print(f"⚠️  {ip} has {count} failed login attempts")

except FileNotFoundError:
    print("Log file not found. Please ensure auth.log exists.")
