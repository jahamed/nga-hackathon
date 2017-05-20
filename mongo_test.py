from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['pymongo_test']

#title, link, description

articles = db.articles

article_1_data = {
    'title': 'North Korea Launched Nukes',
    'link': 'http://www.google.com',
    'description': 'North Korea launched some nukes :('
}

article_2_data = {
    'title': 'Test CNN Title',
    'link': 'http://www.cnn.com',
    'description': 'CNN News Description'
}

insert_result = articles.insert_many([article_1_data, article_2_data])
print('Multiple posts: {0}'.format(insert_result.inserted_ids))

# Retrieve Articles
korea_article = articles.find_one({
    'title': 'North Korea Launched Nukes'
})

# Multiple Articles
korea_articles = articles.find({
    'title': 'North Korea Launched Nukes'
})

print(korea_article)

for article in korea_articles:
    print(article)