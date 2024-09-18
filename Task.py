from textblob import TextBlob

text = "bad is better than good"
blob = TextBlob(text)
sentiment = blob.sentiment
print(sentiment.polarity)