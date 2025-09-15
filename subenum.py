import requests
import re
import subprocess

def is_host_up(host):
    try:
        # Ping the host once, timeout 2 seconds
        output = subprocess.run(
            ["ping", "-c", "1", "-W", "2", host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return output.returncode == 0
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return False

# Domain that we'll be searching
domain = str(input("insert your domain: "))

# We'll search into crt.sh (a website that indentify certificates SSL)
crt = f"https://crt.sh/?q={domain}"

# Now we're goin to request to the website our domain
requests = requests.get(crt)
print("Loading request...")
# Get the html to sanitizate
crt_html = str(requests.content)
# Pattern
pattern = rf"\b[\w.-]+\.{re.escape(domain)}\b"
# Regex to get the subdomains
matches = re.findall(pattern, crt_html)

# Remove duplicates 
unique_matches = list(set(matches))

for sub in unique_matches:
    status = "UP" if is_host_up(sub) else "DOWN"
    print(f"{sub} is {status}")
