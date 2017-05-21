import requests
from parsers import *

EC2_URL = 'http://ec2-52-15-229-70.us-east-2.compute.amazonaws.com:8080/articles'

fox_urls = [
    "http://feeds.foxnews.com/foxnews/national",
    "http://feeds.foxnews.com/foxnews/world",
    "http://feeds.foxnews.com/foxnews/politics",
    'http://feeds.foxnews.com/foxnews/internal/travel/mixed',
]

reuters_urls = [
    "http://feeds.reuters.com/Reuters/worldNews",
    "http://feeds.reuters.com/reuters/environment",
    "http://feeds.reuters.com/news/wealth",
    "http://feeds.reuters.com/reuters/technologyNews"
]

# Upload RSS Feed data to our MongoDB
for fox_url in fox_urls:
    print("Uploading this url: ", fox_url)
    payload = parseFoxRSS(fox_url)
    r = requests.post(EC2_URL, json=payload)
    print("Status code: ", r.status_code)

for reuters_url in reuters_urls:
    print("Uploading this url: ", reuters_url)
    payload = parseReutersRSS(reuters_url)
    r = requests.post(EC2_URL, json=payload)
    print("Status code: ", r.status_code)

# Get all Feeds in our MongoDB
# r = requests.get('http://ec2-52-15-229-70.us-east-2.compute.amazonaws.com:8080/articles')
# print(r.text)
