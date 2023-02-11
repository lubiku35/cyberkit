import requests
from bs4 import BeautifulSoup

def whois_lookup(domain):
    response = requests.get(f"https://who.is/whois/{domain}")

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        pre_tag = soup.pre
        pre_tag = pre_tag.get_text
        x = pre_tag.__str__().split('\n')
        out = ""
        for i in x:
            if i.startswith("<") or i.startswith("%"):
                continue
            else:
                out += i + "\n"
        return out
    else:
        return "Error: WHOIS lookup failed."

print(whois_lookup("formaco.cz"))