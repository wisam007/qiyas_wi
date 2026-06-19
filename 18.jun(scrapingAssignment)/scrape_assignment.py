import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#First we scrape the website
URL = "https://toscrape.com"
response =  requests.get(URL)

soup = BeautifulSoup(response.text,'html.parser')

print(soup)
raw_titles = []
raw_prices = []



books = soup.find_all("article",class_="product_pod")

print(books)