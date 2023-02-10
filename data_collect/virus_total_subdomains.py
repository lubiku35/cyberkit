import requests


class VirusTotalSubdomains:
    pass

url = "https://www.virustotal.com/api/v3/domains/jhv.cz/subdomains?limit=1000"

headers = {
    "accept": "application/json",
    "x-apikey": "81dab74fef4524e13c1c17bfe5d33b7a63005282840bf4dbcc080d8ff164290f"
}

response = requests.get(url, headers=headers)


with open("./data_collect/subdomains.json", "w") as file:
    file.write(response.text)