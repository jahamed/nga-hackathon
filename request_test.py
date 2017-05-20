import requests

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
            "title": "another random title",
            "body": "Different content",
            "source": "www.cnn.com",
            "date": "5/20/2019",
            "tags": ["tag2", "whatever"]
        }
    ]
}

# r = requests.post('http://ec2-13-58-7-84.us-east-2.compute.amazonaws.com:8080/raw-articles', data=payload)
r = requests.get('http://ec2-13-58-7-84.us-east-2.compute.amazonaws.com:8080/articles')
print (r.json())
print (r.status_code)
