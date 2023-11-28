from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome()

products = []
prices = []
ratings = []

time.sleep(5)
driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
    name = a.find_next('div', attrs={'class': '_4rR01T'})
    price = a.find_next('div', attrs={'class': '_3tbKJL'})
    rating = a.find_next('div', attrs={'class': 'gUuXy-'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)


df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Ratings': ratings})

df.to_csv('products.csv', index=False, encoding='utf-8')


