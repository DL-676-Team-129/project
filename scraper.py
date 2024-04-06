import requests
from bs4 import BeautifulSoup
import hashlib, io, requests, pandas as pd
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image

with open("./Labels.txt", 'r') as f:
    lines = f.readlines()
    labels = [line.replace('\n', '').replace(' ', '-').lower() for line in lines]


def getdata(url):
    r = requests.get(url)
    return r.text

for prod in labels:
    htmldata = getdata("https://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0&LH_TitleDesc=0&_ipg=120".format(prod))
    soup = BeautifulSoup(htmldata, 'html.parser')
    links = soup.find_all('img')

    import os
    with open("./image-urls/{}.txt".format(prod), "w") as f:
        for item in links:
            f.write(item['src'] + "\n")

