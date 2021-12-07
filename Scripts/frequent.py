# Return 100 most common words with the count
from nltk import FreqDist
from nltk.corpus import stopwords

def frequent(text):
    stopword = stopwords.words()
    #content = [w for w in text if w.lower() not in stopword]
    content = [w for w in text]
    cfd = FreqDist(content)
    mostcommon = cfd.most_common(100)
    return mostcommon