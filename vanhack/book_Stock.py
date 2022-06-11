from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def get_pageSoup(myurl):
    uClient = uReq(myurl)

    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    return page_soup

def in_stock(title, topic):
    book_categories = [
        'Books', 'Travel', 'Mystery', 'Historical Fiction', 'Sequential Art', 'Classics', 'Philosophy', 'Romance',
        'Womens Fiction', 'Fiction',
        'Childrens', 'Religion', 'Nonfiction', 'Music', 'Default', 'Science Fiction', 'Sports and Games',
        'Add a comment', 'Fantasy', 'New Adult',
        'Young Adult', 'Science', 'Poetry', 'Paranormal', 'Art', 'Psychology', 'Autobiography', 'Parenting',
        'Adult Fiction', 'Humor', 'Horror',
        'History', 'Food and Drink', 'Christian Fiction', 'Business', 'Biography', 'Thriller', 'Contemporary',
        'Spirituality', 'Academic', 'Self Help',
        'Historical', 'Christian', 'Suspense', 'Short Stories', 'Novels', 'Health', 'Politics', 'Cultural', 'Erotica',
        'Crime'
    ]
    book_categories = list(map(lambda x: x.lower(), book_categories))
    topic = topic.lower()
    if topic not in book_categories:
        return False
    book_index = book_categories.index(topic) + 1
    book_topic = topic.replace(" ", "-").lower()
    book_url = book_topic + "_" + str(book_index)
    myurl = f"http://books.toscrape.com/catalogue/category/books/{book_url}/"
    page_soup = get_pageSoup(myurl)
    bookshelf_items = page_soup.findAll("form", {"class": "form-horizontal"})
    pages = [int(s) for s in bookshelf_items[0].text.split() if s.isdigit()][0] // 20 + 2
    if pages < 20:
        page_url = myurl + "index.html"
        book_soup = get_pageSoup(page_url)
        bookshelf = book_soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
        for books in bookshelf:
            book_title = books.h3.a["title"]
            if book_title.lower() == title.lower():
                return True
    for page in range(2, pages):
        page_url = myurl + "page-" + str(page) + ".html"
        book_soup = get_pageSoup(page_url)
        bookshelf = book_soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
        for books in bookshelf:
            book_title = books.h3.a["title"]
            if book_title.lower() == title.lower():
                return True
    return False
print(in_stock("the origin of species", "darwin"))

