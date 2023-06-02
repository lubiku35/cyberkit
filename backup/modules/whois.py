import requests
from bs4 import BeautifulSoup

class Whois:

    def __init__(self, target_info) -> None:
        self.target_info = target_info

    def process_whois_lookup(self):
        
        def create_whois_output(data):
            with open(f"./out/{self.target_info.get('target_name')}/{self.target_info.get('target_name')}_whois.txt", "w") as file: file.write("\n".join(data))

        RESPONSE = requests.get(f"https://who.is/whois/{self.target_info.get('target_domain')}")

        if RESPONSE.status_code == 200:
            output = []
            for i in "".join(BeautifulSoup(RESPONSE.text, 'html.parser').pre.get_text.__str__()).split("\n"):
                if i.startswith("<") or i.startswith("%"):
                    continue
                else:
                    if i.find("<") != -1:
                        i = i[:i.find("<")]
                    output.append(i)
            create_whois_output(data = output)
            print("WHOIS lookup successfully created")
            return 
        else:
            return "Error: WHOIS lookup failed."


