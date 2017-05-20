import xml.etree.ElementTree as ET
import json

def parseRSS(source):
    tree = ET.parse(source)
    root = tree.getroot()

    items = []
    for article in root.iter('item'):
        item = {}
        item['title'] = article.find('title').text
        item['source'] = article.find('link').text
        item['body'] = article.find('description').text
        items.append(item)

    articles = {}
    articles['articles'] = items
    json_data = json.dumps(articles)
    # print(json_data)
    return articles

if __name__ == '__main__':
    print("in main")
