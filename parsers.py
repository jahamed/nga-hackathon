import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Works for rss specification 2.0
def parseRSS(source):
    tree = ET.parse(source)
    root = tree.getroot()

    items = []
    for article in root.iter('item'):
        title = article.find('title').text
        source = article.find('link').text
        body = article.find('description').text
        date = article.find('pubDate')
        if date is None:
            date = 'UNKNOWN'
        else:
            date = date.text
        tags = []

        item = {}
        item['title'] = title
        item['source'] = source
        item['body'] = body
        item['date'] = date
        item['tags'] = tags

        items.append(item)

    articles = {}
    articles['articles'] = items
    return articles

def downloadrss(url):
    s = urlopen(url)
    contents = s.read()
    filename = filenameFromUrl(url)
    file = open(filename, 'wb')
    file.write(contents)
    file.close()

def filenameFromUrl(url):
    domain = url.split('.')[1]
    tail = url.split('/')
    tail = [x for x in tail if x != '']
    tail = tail[-1]
    filename = domain + "_" + tail + ".xml"
    return filename

def parseFoxNews(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    article_body = soup.body.find('div', attrs={'class': 'article-body'})
    paragraphs = article_body.findAll('p')
    body = []
    for paragraph in paragraphs:
        body.append(paragraph.getText())
    print(body)
    return body

if __name__ == '__main__':
    print("in main")
    # url = "http://feeds.foxnews.com/foxnews/politics"
    # downloadrss(url)
    parseFoxNews("http://www.foxnews.com/politics/2017/05/20/gop-candidate-running-for-governor-presses-mcauliffe-on-climate-change.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+foxnews%2Fpolitics+%28Internal+-+Politics+-+Text%29")

