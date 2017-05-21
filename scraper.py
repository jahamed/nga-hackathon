from urllib.request import urlopen
from bs4 import BeautifulSoup, UnicodeDammit
from utilities import ascii_dammit

def parseFoxNews(url):
    page = urlopen(url)
    # soup = BeautifulSoup(page, "html.parser", from_encoding='utf-8')
    soup = BeautifulSoup(page, "html.parser")

    article_body = soup.body.find('div', attrs={'class': 'article-body'})
    paragraphs = article_body.findAll('p')
    body = []
    for paragraph in paragraphs:
        body.append(paragraph.getText())
    body = ' '.join(body)
    tmp = body.encode('ascii', 'replace')
    # print(body)
    # body = UnicodeDammit(body, ["windows-1252"], smart_quotes_to="ascii").unicode_markup
    body = remove_smart_quotes(body)
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
    return body

# Doesn't work
def replaceBadStrings(strings):
    return strings # remove this if you want to edit
    new_strings = []
    for string in strings:
        new_string = string.replace('\\xa0', ' ')
        new_strings.append(new_string)
    return new_strings

def remove_smart_quotes (text):
    text = text.replace(u"\u2018", "'") \
            .replace(u"\u2019", "'") \
            .replace(u"\u201c", '"') \
            .replace(u"\u201d", '"') \
            .replace(u"\u2013", '') \
            .replace(u"\u00a0", '')

    return text


if __name__ == '__main__':
    print("In main for scraper.py")
    parseFoxNews("http://www.foxnews.com/politics/2017/05/20/gop-candidate-running-for-governor-presses-mcauliffe-on-climate-change.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+foxnews%2Fpolitics+%28Internal+-+Politics+-+Text%29")
    # parseCNN("http://www.cnn.com/2017/05/20/middleeast/iran-rouhani-election/index.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+rss%2Fcnn_world+%28RSS%3A+CNN+-+World%29")
