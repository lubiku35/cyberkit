
    # print(check_https_subdomains_reachability(SUBDOMAINS=SUBDOMAINS))
    # print(check_http_subdomains_reachability(SUBDOMAINS=SUBDOMAINS))


    #     # Use Firefox as the web driver
    #     driver = webdriver.Firefox()
    #     # Set the timeout for the web driver to 10 seconds
    #     driver.set_page_load_timeout(10)

    #     HTTPS_SUBDOMAINS_REACHABILITY = []
    #     for i in SUBDOMAINS:
    #         try:
    #             URL = f"https://{i}"
    #             driver.get(url=URL)
    #             status_code = driver.execute_script("return window.performance.getEntries()[0].response.status")
    #             print(f'Domain is reachable with status code: {status_code}')
    #         except TimeoutException:
    #             print("Timed out while waiting for page to load")
    #         except WebDriverException:
    #             print("An error occurred while trying to load the page")
    #     driver.quit()
    
    # def check_http_subdomains_reachability(SUBDOMAINS):
    #     HTTP_SUBDOMAINS_REACHABILITY = []