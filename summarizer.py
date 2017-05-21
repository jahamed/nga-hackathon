from gensim.summarization import summarize, keywords

# Use Gensim (TextRank Algorithm) to generate article summary.
def generate_summary(text):
    return summarize(text, ratio=0.2)

# Generate Tags/Keywords using Gensim.
def generate_tags(text):
    return keywords(text, lemmatize=True, words=5, scores=False, split=True, pos_filter=['NN'])
