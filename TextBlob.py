from calendar import month

import wiki
from nltk.book import text1
from nltk.chat import zen_chat, zen
from textblob import TextBlob
from textblob.en import Sentiment, sentiment
from nltk.corpus import brown
from textblob import Word
from textblob.wordnet import VERB

# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# test =
# text = """
# The titular threat of The Blob has always struck me as the ultimate movie
# monster: an insatiably hungry, amoeba-like mass able to penetrate
# virtually any safeguard, capable of--as a doomed doctor chillingly
# describes it--"assimilating flesh on contact.
# Snide comparisons to gelatin be damned, it's a concept with the most
# devastating of potential consequences, not unlike the grey goo scenario
# proposed by technological theorists fearful of
# artificial intelligence run rampant.
# """
# blob = TextBlob(text)
# blob.tags
# # first text
# wiki = TextBlob("Python is a high-level, general-purpose programming language.")
# wiki.tags
# # Sentiment Analysis
#
#
#



# test - 03-Spelling Correction
# b= TextBlob("I have good speling!")
# print(b.correct())

# text 04 -Get Word and Noun Phrase Frequencies

# monty = TextBlob("We are no longer the Knights who say Ni. "
#                     "We are now the Knights who say Ekki ekki ekki PTANG.")
# monty.word_counts['ekki']
# monty.words.count('ekki')
# monty.words.count('ekki', case_sensitive=True)
# wiki.noun_phrases.count('python')

# text -Parsing

# b = TextBlob("And now for something completely different")
# print(b.parse())

# text - TextBlobs Are Like Python Strings
# zen[0:19]
# zen.upper()
# zen.find("simple")


# text


# Define the text
# animals = TextBlob("cat dog octopus")
# animals.words
# animals.words.pluralize()




#text
# word = Word("octopus")
# word.synsets
# Word("hack").get_synsets(pos=VERB)

# text
# animals = TextBlob("cat dog octopus")
# animals.words
# animals.words.pluralize()

# task 01

text = "bad is better than good"
blob = TextBlob(text)
sentiment = blob.sentiment
print(sentiment.polarity)

