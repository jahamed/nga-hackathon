import xml.etree.ElementTree as ET
from urllib.request import urlopen
from scraper import parseFoxNews
from utilities.unicode_utils import replace_unicode_chars
from summarizer import *

# Works for rss specification 2.0
# Transform RSS Feed (in XML) into JSON blob containing article summary, tags, etc.
def parseRSS(source):
    tree = ET.parse(source)
    root = tree.getroot()

    items = []
    for article in root.iter('item'):
        title = replace_unicode_chars(article.find('title').text)
        source = article.find('link').text
        description = replace_unicode_chars(article.find('description').text)
        date = article.find('pubDate')

        if date is None:
            date = 'UNKNOWN'
        else:
            date = date.text

        body = parseFoxNews(source)
        summary = generate_summary(body)

        tags = generate_tags(body)

        item = {}
        item['title'] = title
        item['source'] = source
        item['description'] = description
        item['body'] = body
        item['date'] = date
        item['summary'] = summary
        item['tags'] = tags

        items.append(item)

    articles = {}
    articles['articles'] = items
    return articles

def parseFoxRSS(fox_rss_url):
    file = downloadrss(fox_rss_url)
    return parseRSS(file)


# Generate an rss .xml file for a rss feed
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
    relative_path = "rss_feeds/"
    return relative_path + filename

if __name__ == '__main__':
    # Test of parsing and scraping a news feed into json
    fox_url = "http://feeds.foxnews.com/foxnews/politics"
    to_return = parseFoxRSS(fox_url)
    import json
    print(json.dumps(to_return))


