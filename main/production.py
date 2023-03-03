import modules.target as target             # defined as callback_target
import modules.virustotal as virustotal     # defined as callback_virustotal
import modules.dns as dns                   # defined as callback_dns
import modules.output as output             # defined as callback_output
import modules.whois as whois               # defined as callback_whois
import modules.shodan as shodan             # defined as callback_shodan
import modules.ports as ports               # defined as callback_ports
import modules.screenshots as screenshots   # defined as callback_screenshots
import modules.services as services         # defined as callback_services
import modules.menu as menu                 # # defined as callback_menu


def main():
    vt = virustotal.Virustotal()
    vt.read_env()
    print(vt.headers)

