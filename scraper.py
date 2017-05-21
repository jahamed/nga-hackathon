from urllib.request import urlopen
from bs4 import BeautifulSoup


def parseFoxNews(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    article_body = soup.body.find('div', attrs={'class': 'article-body'})
    paragraphs = article_body.findAll('p')
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



if __name__ == '__main__':
    print("In main for scraper.py")
    # str = parseFoxNews("http://www.foxnews.com/politics/2017/05/20/gop-candidate-running-for-governor-presses-mcauliffe-on-climate-change.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+foxnews%2Fpolitics+%28Internal+-+Politics+-+Text%29")
