
x = [['217.11.249.145', 'mycom.cz'], ['109.123.220.168', 'podpora.mycom.cz'], ['52.96.73.56', '52.96.79.200', '52.96.79.8', '52.96.79.40', 'autodiscover.mycom.cz'], ['81.2.195.30', 'test.mycom.cz'], ['109.123.220.171', 'ftp.mycom.cz'], ['109.123.220.169', 'reaqta.mycom.cz'], ['109.123.220.155', 'forticems.mycom.cz'], ['217.11.249.145', 'dev.mycom.cz'], ['antispam.mycom.cz'], ['109.123.220.168', 'support.mycom.cz'], ['217.11.249.145', 'www.mycom.cz'], ['23.236.62.147', 'seminar.mycom.cz']]

for i in x:
    for j in i:
        if j[0].isalpha() or j[1].isalpha() or j[2].isalpha():
            print(j)
            
# # Take the screenshot
# driver.save_screenshot("screenshot.png")

# # Quit the driver
# driver.quit()

str = "DSad"

str.isalpha()