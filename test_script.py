import json, xlsxwriter
import pandas as pd
def collect_subdomains_data(): 
    
    def create_subdomains_excel_output(DATA):
        data = []
        for subdomain, ips in DATA.items(): data.append({'SUBDOMAIN NAME': subdomain, 'SUBDOMAIN IPS': ', '.join(ips)})
        df = pd.DataFrame(data=data)

        # Write the dataframe to an Excel file
        writer = pd.ExcelWriter('subdomains.xlsx', engine='xlsxwriter')
        df.to_excel(writer, index=False)
        writer.close()
        return
    
    SUBDOMAINS_DATA = {}

    with open("./data/vt_subdomains.json", "r") as file: DATA = json.load(file)
    
    SUBDOMAINS_COUNT = DATA.get("meta").get("count")

    for i in DATA.get("data"):
        SUBDOMAIN_NAME = i.get("id")        
        LAST_DNS_RECORDS_DATA = i.get("attributes").get("last_dns_records")
        SUBDOMAIN_IPS = []
        for i in LAST_DNS_RECORDS_DATA:
            if i["type"] == "A": 
                SUBDOMAIN_IPS.append(i.get("value"))
            SUBDOMAINS_DATA[SUBDOMAIN_NAME] = SUBDOMAIN_IPS
            
    return create_subdomains_excel_output(DATA=SUBDOMAINS_DATA) 


print(collect_subdomains_data())
collect_subdomains_data()


