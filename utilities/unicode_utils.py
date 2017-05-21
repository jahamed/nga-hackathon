# Quick function to remove unicode characters like microsoft stylized quotes from scraped data
def replace_unicode_chars (text):
    text = text.replace(u"\u2018", "'") \
            .replace(u"\u2019", "'") \
            .replace(u"\u201c", '"') \
            .replace(u"\u201d", '"') \
            .replace(u"\u2013", '') \
            .replace(u"\u00a0", '')

    return text