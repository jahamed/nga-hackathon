from gensim.summarization import summarize, keywords

def generate_summary(text):
    return summarize(text, ratio=0.2)

def generate_tags(text):
    return keywords(text, lemmatize=True, words=4, scores=False)