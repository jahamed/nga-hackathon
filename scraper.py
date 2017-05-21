from urllib.request import urlopen
from bs4 import BeautifulSoup
from utilities.unicode_utils import replace_unicode_chars

def parseFoxNews(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    article_body = soup.body.find('div', attrs={'class': 'article-body'})
    paragraphs = article_body.findAll('p')

    body = []

    for paragraph in paragraphs:
        body.append(paragraph.getText())

    body = '\n\n'.join(body)
    body = replace_unicode_chars(body)

    return body

def parseCNN(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    section = soup.body.find('section', attrs={'id': 'body-text'})
    div = section.find('div', attrs={'class': 'l-container'})
    paragraphs = div.findAll('div', attrs={'class': ['zn-body__paragraph', 'el__leafmedia']})
    body = []

    for paragraph in paragraphs:
        body.append(paragraph.getText())

    body = '\n\n'.join(body)
    body = replace_unicode_chars(body)

    return body

if __name__ == '__main__':
    print("In main for scraper.py")
    parseFoxNews("http://www.foxnews.com/politics/2017/05/20/gop-candidate-running-for-governor-presses-mcauliffe-on-climate-change.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+foxnews%2Fpolitics+%28Internal+-+Politics+-+Text%29")
    # parseCNN("http://www.cnn.com/2017/05/20/middleeast/iran-rouhani-election/index.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+rss%2Fcnn_world+%28RSS%3A+CNN+-+World%29")
