# Subdomain Finder & Availability Checker

This is a Python tool that:
1. Fetches SSL certificate data from [crt.sh](https://crt.sh/) for a given domain.
2. Extracts potential subdomains using regex.
3. Pings each subdomain to check whether it is **UP** or **DOWN**.

---

## Features
- Scrapes **crt.sh** for SSL/TLS certificate data.
- Extracts and lists unique subdomains.
- Pings each subdomain to determine availability.
- Simple CLI interface.

---

## Requirements
- Python 3.x  
- The dependencies listed in `requirements.txt`  

Install them with:
```bash
pip install -r requirements.txt
