import json

with open("./data_collect/subdomains.json", "r") as file:
    data = json.load(file)

# Now you can work with the JSON data as a Python dictionary

subdomains = []
counter = 0

for i in data["data"]:
    subdomain_data = []
    
    # Domain Name
    domain_id = data["data"][counter]["id"]

    # subdomain IP 
    last_dns_record_ip = data["data"][counter]["attributes"]["last_dns_records"][0]["value"]
    
    subdomain_data.append(last_dns_record_ip)
    subdomain_data.append(domain_id)
    
    print(subdomain_data)
    subdomains.append(subdomain_data)
    counter += 1

print(subdomains)

# data["meta"]["count"] -> count of subdomains