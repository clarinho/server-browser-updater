import requests
from bs4 import BeautifulSoup
import json
import re

# URL of the webpage you want to scrape
url = "https://master.iw4.zip/servers#"

# Maximum number of servers to collect
max_servers = 1500

# Define a regex pattern for IPv4 addresses
ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

# Define a regex pattern for domain names
domain_pattern = re.compile(
    r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
)

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all server rows with class 'server-row'
    server_rows = soup.find_all('tr', class_='server-row')
    
    # Extract IP addresses and ports, filtering for IPv4 or domain names
    servers = []
    for row in server_rows:
        ip = row.get('data-ip')
        port = row.get('data-port')
        if ip and port and (ipv4_pattern.match(ip) or domain_pattern.match(ip)):
            servers.append(f"{ip}:{port}")
        # Stop collecting if the limit is reached
        if len(servers) >= max_servers:
            break
    
    # Save the list of servers (IP:Port) to a .json file
    with open('favourites.json', 'w') as json_file:
        json.dump(servers, json_file, indent=4)

    # Print confirmation to the console
    print(f"Server data saved to favourites.json")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
