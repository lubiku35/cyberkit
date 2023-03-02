import modules.virustotal as virustotal 
import modules.dns as dns
import modules.output as output 
import modules.whois as whois 
import modules.shodan as shodan 
import modules.ports as ports 
import modules.screenshots as screenshots 
import modules.services as services

class Main:

    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    virustotal = virustotal.Virustotal()
    dns = dns.Dns()
    output = output.Output()
    whois = whois.Whois()
    shodan = shodan.Shodan()
    ports = ports.Ports()
    screenshots = screenshots.Screenshots()
    services = services.Services()
    
    print(virustotal.test())
    print(dns.test())
    print(output.test())
    print(whois.test())
    print(shodan.test())
    print(ports.test())
    print(screenshots.test())
    print(services.test())
   