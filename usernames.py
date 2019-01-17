#!/usr/local/bin/python3.5

# import required modules
import requests
import urllib.request, http.client
from urllib.parse import urlparse
import sys
import os
from bs4 import BeautifulSoup

os.system("clear")

print("      ________                __                                       ")
print("     |  |  |  |.-----.----.--|  |.-----.----.-----.-----.-----.        ")
print("     |  |  |  ||  _  |   _|  _  ||  _  |   _|  -__|__ --|__ --|        ")
print("     |________||_____|__| |_____||   __|__| |_____|_____|_____|        ")
print("                                 |__|                                  ")
print(" _____                __          _______ __           __              ")
print("|     |_.-----.-----.|__|.-----. |    ___|__|.-----.--|  |.-----.----. ")
print("|       |  _  |  _  ||  ||     | |    ___|  ||     |  _  ||  -__|   _| ")
print("|_______|_____|___  ||__||__|__| |___|   |__||__|__|_____||_____|__|   ")
print("              |_____|                                                  ")
print("-----------------------------------------------------------------------")
print("----------------------------------By Daniel----------------------------")
print('                "Just a basic tool I made to learn Python"             ')
print("-----------------------------------------------------------------------")
print("")



# enter a wordpress site.
site = input("Wordpress site to scan: ")
print("")
print("")

# set author numbers to enumerate
authNum = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]

for num in authNum:
    url = ("http://" + site + "/?author=" + num)
    res = requests.get(url)
    response = requests.get(url)

    if response.history:
        for resp in response.history:
            authURL = response.url
            authName = urlparse(authURL)
            login = authName.path
            login = login[8:]
            login = login[:-1]
            print("Author login: " + login)
        else:
            print("")
