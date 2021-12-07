# Calculate sentiment
import nltk

def sentiment_function(tokens, LabMT_dict):
    text = nltk.Text(tokens)
    freq_text = nltk.FreqDist(text)
    hapiness = {k:v for k,v in LabMT_dict.items() if k in tokens}
    hapiness_dict = dict(sorted(hapiness.items()))
    freq_all = sum(freq_text.values())
    hapiness_norm = {k:v/freq_all for k,v in freq_text.items()}
    hapiness_dict_norm = dict(sorted(hapiness_norm.items()))
    sentiment = sum(hapiness_dict[k]*hapiness_dict_norm[k] for k in hapiness_dict)
    return sentiment