# Definition: Tokenization is the process of splitting text into smaller units called tokens, such as words and punctuation.


import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

# Cleaned text from previous step
clean_text = """
hello i am learning natural language processing
the students are running and playing happily
visit for more information
"""

# Tokenization
tokens = word_tokenize(clean_text)

print("Cleaned Text:")
print(clean_text)

print("\nTokens:")
print(tokens)



# Cleaned Text:

# hello i am learning natural language processing
# the students are running and playing happily
# visit for more information


# Tokens:
# ['hello', 'i', 'am', 'learning', 'natural', 'language', 'processing', 'the', 'students', 'are', 'running', 'and', 'playing', 'happily', 'visit', 'for', 'more', 'information']







# Explanation
# - word_tokenize() – converts the sentence into individual tokens.
# - tokens – stores the resulting list of words.
# - print() – displays the tokens.