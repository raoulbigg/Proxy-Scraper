import requests
from bs4 import BeautifulSoup

def scrape():
    url = "http://ipaddress.com/proxy-list/"
    r = requests.get(url)

    soup = BeautifulSoup(r.text)
    f1 = soup.findAll('table', attrs={'class':'table table-striped'})
    ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:[0-9]+')
    for line in f1:
        proxies = re.findall(ipPattern,line.text)
        for proxy in proxies:
            f = open('proxies2.txt', 'a')
            f.write(proxy+'\n')
            f.close()
scrape()

