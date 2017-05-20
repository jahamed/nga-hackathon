import xml.etree.ElementTree as ET

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

if __name__ == '__main__':
    print("in main")

