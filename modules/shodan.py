from shodan import Shodan
import shodan
import pandas as pd

class ShodanLookup:

    def __init__(self, target_info, api_key, SUBDOMAINS_DATA, SHODAN_DATA_INFO = []) -> None:
        self.target_info = target_info
        self.api_key = api_key
        self.SUBDOMAINS_DATA = SUBDOMAINS_DATA

        self.SHODAN_DATA_INFO = SHODAN_DATA_INFO    # [ ("subdomain", "ip_address", ) ]

    def collect_shodan_data(self):

        def modify_data_to_excel_format():

            def check_if_null(data):
                return "No Data" if data == "" or data == [] or data == " " else data

            excel_subdomain, excel_ip, excel_os, excel_isp, excel_hostnames, excel_domains, excel_country_name, excel_organization, excel_ports = [], [], [], [], [], [], [], [], []
            for i in self.SHODAN_DATA_INFO:
                excel_subdomain.append(check_if_null(i[0]))
                excel_ip.append(check_if_null(i[1]))
                excel_os.append(check_if_null(i[2]))
                excel_isp.append(check_if_null(i[2]))
                excel_hostnames.append(check_if_null(i[4]))
                excel_domains.append(check_if_null(i[5]))
                excel_country_name.append(check_if_null(i[6]))
                excel_organization.append(check_if_null(i[7]))
                excel_ports.append(check_if_null(i[8]))

            df = pd.DataFrame({
                "Domain": excel_subdomain,
                "Ip Address": excel_ip,
                "Domains / Subdomains": excel_domains,
                "ISP": excel_isp,
                "Country Name": excel_country_name,
                "OS": excel_os,
                "Hostnames": excel_domains,
                "Related Domains": excel_domains,
                "Ports": excel_ports,
                "Organization": excel_organization,
            })

            return df.to_excel(f'./out/{self.target_info.get("target_name")}/shodan_data.xlsx', index=False)

        
        def get_ipinfo(ip):
            try:
                api = Shodan(self.api_key)
                ipinfo = api.host(ip)
                return ipinfo["os"], ipinfo["isp"], ipinfo["hostnames"], ipinfo["domains"], ipinfo["country_name"], ipinfo["org"], ipinfo["ports"]
            except shodan.APIError:
                return "No Data", "No Data", "No Data", "No Data", "No Data", "No Data", "No Data"

        print("Collecting data about subdomains from Shodan API...")
        for i in self.SUBDOMAINS_DATA.items():
            for ip in i[1]:
                os, isp, hostnames, domains, country_name, org, ports = get_ipinfo(ip=ip)
                self.SHODAN_DATA_INFO.append((i[0], ip, os, isp, hostnames, domains, country_name, org, ports))

        print("Modifying collected data from Shodan API...")
        modify_data_to_excel_format()

        return 


    def check(self):
        print(self.target_info)
        print(self.api_key)
        print(self.SUBDOMAINS_DATA)
