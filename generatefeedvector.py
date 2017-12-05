import feedparser
import re

# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
    # Parse the feede
    d = feedparser.parse(url)
    wc = {}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e: sumary = e.summary
        else: summary = e.description

        print(summary)
        # Exctract a list of words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1
    return d.feed.title, wc

def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>] + >').sub('', html)

    # Split word by all non-alpha characters
