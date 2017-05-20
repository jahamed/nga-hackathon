import xml.etree.ElementTree as ET
import json

tree = ET.parse('sample_rss_feeds/sample_rss_feed_1.xml')
root = tree.getroot()

items = []
for article in root.iter('item'):
    title = article.find('title')
    link = article.find('link')
    description = article.find('description')
    item = {}
    item[title.tag] = title.text
    item[link.tag] = link.text
    item[description.tag] = description.text
    items.append(item)

articles = {}
articles['articles'] = items
json_data = json.dumps(articles)
print(json_data)
