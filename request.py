import requests
from parsers import parseRSS

fox_urls = [
    "http://feeds.foxnews.com/foxnews/national",
    "http://feeds.foxnews.com/foxnews/world",
    "http://feeds.foxnews.com/foxnews/politics",
]

for fox_url in fox_urls:
    payload = parseRSS(fox_url)
    r = requests.post('http://ec2-52-15-229-70.us-east-2.compute.amazonaws.com:8080/articles', json=payload)

# r = requests.get('http://ec2-52-15-229-70.us-east-2.compute.amazonaws.com:8080/articles')

# print (r.json())
# print (r.status_code)
# print(r.text)
