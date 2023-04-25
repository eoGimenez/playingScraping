import bs4
import requests
url_original = "https://books.toscrape.com/catalogue/page-{}.html"
# result = requests.get(url_original.format('1'))

# soup = bs4.BeautifulSoup(result.text, "lxml")

# books = soup.select(".product_pod")


filtered = {}
for page in range(2, 21):
    url_page = url_original.format(page)
    result = requests.get(url_page)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        if book.select('.star-rating.Four'):
            title = book.select('a')[1]['title']
            filtered[title] = '4 stars'
        if book.select('.star-rating.Five'):
            title = book.select('a')[1]['title']
            filtered[title] = '5 stars'
        else:
            pass


print(filtered)
