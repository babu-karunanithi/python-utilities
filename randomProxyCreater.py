from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import requests
class createFreeProxyList:
    proxies=[]
    currentProxy=[]
    currentUserAgent=[]
    currentProxyIndex=0
    ua=""
    def __init__(self):
        self.userAgent = UserAgent()
        self.currentUserAgent = ""
        self.proxies=[]
        self.currentProxy=[]
        self.currentProxyIndex=0

    def random_agent(self):
        self.currentUserAgent = { "User-Agent": self.userAgent.random }

    def createProxyList(self):
        url ='https://www.sslproxies.org/'
        self.random_agent()
        headers = { 'User-Agent': self.userAgent.random}
        html = requests.get(url,headers = headers)
        soup = BeautifulSoup(html.text, 'lxml')
        proxies_table = soup.find(id='proxylisttable')
        for row in proxies_table.tbody.find_all('tr'):
            self.proxies.append(row.find_all('td')[0].string+":"+row.find_all('td')[1].string)

    def rotateProxy(self):
        if(len(self.proxies)<=1):
            self.createProxyList()
            print('Proxy list is ready')
            return self.proxies

        else:
            del self.proxies[self.currentProxyIndex]
            self.random_agent()
            print('Something went wrong!')
p =createFreeProxyList()
proxyList=p.rotateProxy()
print('----------------------- generated proxy list ------------------------')
print(proxyList,end='\n')