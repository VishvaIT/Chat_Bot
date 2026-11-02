# Definition: Stopword removal eliminates common words that may not add much meaning to a sentence, such as is, am, the, are, and, for.

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
nltk.download('punkt_tab')
nltk.download('stopwords')

# Cleaned text from previous step
clean_text = """
hello i am learning natural language processing
the students are running and playing happily
visit for more information
"""

# Step 1: Tokenization
tokens = word_tokenize(clean_text)

# Step 2: Get English stopwords
stop_words = set(stopwords.words('english'))

# Step 3: Remove stopwords
filtered_tokens = [
    word for word in tokens
    if word not in stop_words
]

print("Original Tokens:")
print(tokens)

print("\nAfter Stopword Removal:")
print(filtered_tokens)



# Original Tokens:
# ['hello', 'i', 'am', 'learning', 'natural', 'language', 'processing', 'the', 'students', 'are', 'running', 'and', 'playing', 'happily', 'visit', 'for', 'more', 'information']

# After Stopword Removal:
# ['hello', 'learning', 'natural', 'language', 'processing', 'students', 'running', 'playing', 'happily', 'visit', 'information']



# Understand the important lines
# - stopwords.words('english') – gets the English stopword list.
# - set() – stores the words in a set for efficient lookup.
# - word not in stop_words – keeps only words that are not stopwords.
# - filtered_tokens – stores the remaining words.
# Real-world note: Don't always remove stopwords. For example, removing not from "I am not happy" can change the sentence's meaning.