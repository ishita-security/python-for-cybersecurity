# Python for Cybersecurity

This repository contains beginner-to-intermediate Python projects focused on **real-world cybersecurity use cases**.  
The goal is to demonstrate how Python can be used to automate security tasks, analyze logs, and support SOC operations.

## What This Repository Covers

- Log analysis and parsing
- Password security checks
- IP reputation and blacklist checks
- Basic security automation using Python

These scripts reflect tasks commonly performed by **SOC analysts and blue team professionals**.

## Technologies Used

- Python 3
- Standard Python libraries
- Basic file handling and string processing

## Project Structure

# python-for-cybersecurity
---

## 📄 Working with Log Files

The `log_analysis.py` script reads authentication logs from a file named `auth.log`.  
This simulates how SOC analysts analyze system logs to detect suspicious login behavior such as brute-force attempts.

###  How to Run
python log_analysis.py

###  Sample Log File
192.168.1.10 Failed login
192.168.1.10 Failed login
192.168.1.10 Failed login
192.168.1.12 Successful login

###  Sample Output
192.168.1.10 has 3 failed login attempts
