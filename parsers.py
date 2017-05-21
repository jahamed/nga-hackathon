import xml.etree.ElementTree as ET
from urllib.request import urlopen
from scraper import parseFoxNews

# Works for rss specification 2.0
def parseRSS(url):
    file = downloadrss(url)
    tree = ET.parse(file)
    root = tree.getroot()

    items = []
    for article in root.iter('item'):
        title = article.find('title').text
        source = article.find('link').text
        description = article.find('description').text
        date = article.find('pubDate')
        summary = article.find('summary')

        if date is None:
            date = 'UNKNOWN'
        else:
            date = date.text
        tags = []

        body = parseFoxNews(source)

        item = {}
        item['title'] = title
        item['source'] = source
        item['description'] = description
        item['body'] = body
        item['date'] = date
        item['tags'] = tags
        item['summary'] = summary

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
    return filename

def filenameFromUrl(url):
    domain = url.split('.')[1]
    tail = url.split('/')
    tail = [x for x in tail if x != '']
    tail = tail[-1]
    filename = domain + "_" + tail + ".xml"
    return filename



if __name__ == '__main__':
    print("in main")
    url = "http://feeds.foxnews.com/foxnews/politics"
    str = parseRSS(url)
    import json
    print(json.dumps(str))


