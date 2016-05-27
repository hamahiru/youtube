import csv
import urllib2
import requests
from bs4 import BeautifulSoup

def getwiki():
    url = "https://en.wikipedia.org/wiki/List_of_The_100_episodes"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    return "bai"
