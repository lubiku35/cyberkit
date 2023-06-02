

class Screenshot:

    def __init__(self, HTTP_SUBDOMAINS_REACHABILITY, HTTPS_SUBDOMAINS_REACHABILITY) -> None:
        self.HTTP_SUBDOMAINS_REACHABILITY = HTTP_SUBDOMAINS_REACHABILITY
        self.HTTPS_SUBDOMAINS_REACHABILITY = HTTPS_SUBDOMAINS_REACHABILITY

    def create_screenshots(self):

        def create_http_screenshots():
            pass
        def create_https_screenshots():
            pass
    
    def check(self):
        print(self.HTTP_SUBDOMAINS_REACHABILITY)
        print(self.HTTPS_SUBDOMAINS_REACHABILITY)