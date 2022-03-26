from bs4 import BeautifulSoup
import requests, re
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

page_title = str(soup.title)
page_group = re.search('<title>(.*)</title>', page_title)
if page_group == None:
    print("")
else:
    print(page_group.group(1))

heading_list = []
for item in soup.select('h1'):
    heading_list.append(item.text)
print(" ".join(heading_list))

for item in soup.select('li'):
    for j in item.select('a'):
        print(j.text)
