import requests
from parsers import parseRSS

payload = {
    'articles' : [
        {
            "title": "some random title",
            "body": "This is the articles content",
            "source": "www.google.com",
            "date": "5/20/2019",
            "tags": ["tag1", "blah"]
        },
        {
            "title": "UPDATED TITLE",
            "body": "Different content",
            "source": "www.cnn.com",
            "date": "5/20/2019",
            "tags": ["tag2", "whatever"]
        }
    ]
}

payload = parseRSS('sample_rss_feeds/sample_rss_feed_1.xml')
print(payload)

r = requests.post('http://ec2-13-58-7-84.us-east-2.compute.amazonaws.com:8080/articles', json=payload)
# r = requests.get('http://ec2-13-58-7-84.us-east-2.compute.amazonaws.com:8080/articles')
# print (r.json())
# print (r.status_code)
print(r.text)
