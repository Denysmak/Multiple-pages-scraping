import requests
import pandas as pd
from bs4 import BeautifulSoup



books = []

for i in range(1, 50):

    url = f'https://books.toscrape.com/catalogue/page-{i}.html'

    response = requests.get(url)

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    ol = soup.find('ol', class_='row')

    articles = ol.find_all('article', class_ = 'product_pod')

    for article in articles:
        image = article.find('img')
        title = image['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:]) 
        books.append([title, price, star])

df = pd.DataFrame(books, columns=['Title', 'Price', 'Star rating'])
df.to_csv('Books.csv')

