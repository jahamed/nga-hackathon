from gensim.summarization import summarize, keywords

def generate_summary(text, r):
    return summarize(text, ratio=.2)

def generate_tags(text):
    return keywords(text, lemmatize=True, words=5, scores=False, split=True, pos_filter=['NN'])

if __name__ == '__main__':
    article = """And just as he opened the first chapter of our partnership, today we begin a new chapter that will bring lasting benefits to all of our citizens. Let me now also extend my deep and heartfelt gratitude to each and every one of the distinguished heads of state who made this journey here today. You greatly honor us with your presence and I send the warmest regards from my country to yours. """

    minimumSummaryLength = 400
    ratio = minimumSummaryLength/len(article)
    ratio = min(ratio, 1.0)

    summary = generate_summary(article, ratio)
    # print(len(summary))
    # print(summary)






# article = """Read the full transcript of President Trump's speech to Muslim leaders at Sunday's Arab Islamic American Summit:
#
# Thank you. I would like to thank King Salman for his extraordinary words, and the magnificent Kingdom of Saudi Arabia for hosting today's summit. I am honored to be received by such gracious hosts
#
#  I have always heard about the splendor of your country and the kindness of your citizens, but words do not do justice to the grandeur of this remarkable place and the incredible hospitality you have shown us from the moment we arrived
#
# You also hosted me in the treasured home of King Abdul Aziz, the founder of the kingdom who united your great people. Working alongside of another beloved leader, American President Franklin Roosevelt, King Abdul Aziz began the enduring partnership between our two countries. King Salman, your father would be very, very proud to see that you are continuing his legacy
#
# And just as he opened the first chapter of our partnership, today we begin a new chapter that will bring lasting benefits to all of our citizens. Let me now also extend my deep and heartfelt gratitude to each and every one of the distinguished heads of state who made this journey here today. You greatly honor us with your presence and I send the warmest regards from my country to yours. """
