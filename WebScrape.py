import numpy as np
import requests
import csv
from bs4 import BeautifulSoup

url = "https://coreyms.com"
file = 'cms_scrape.csv'
source = requests.get(url).text

csv_file = open(file, 'w') # pass in csv path
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

csv_writer.write()


with open(url) as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.prettify())

titles = soup.title.text
match = soup.find('div', class_='footer')

# iterate through all html article tags
for article in soup.find_all('div', class_='article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    try:
        # get titles of youtube videos
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

print(match)

