import xml.etree.ElementTree as ET

tree = ET.parse('sample_rss_feeds/sample_rss_feed_1.xml')
root = tree.getroot()



# def functionname( parameters ):
#    "function_docstring"
#    function_suite
#    return [expression]


articles = []

for article in root.iter('item'):
    title = article.find('title')
    link = article.find('link')
    description = article.find('description')
    tmp = {}
    tmp[title.tag] = title.text
    tmp[link.tag] = link.text
    tmp[description.tag] = description.text
    articles.append(tmp)

print(items)

# Building JSON
# data = {}
# data['key'] = 'value'
# json_data = json.dumps(data)


# xmlstr = ET.tostring(root, encoding='utf8', method='xml')
# print (xmlstr)

