# Definition: Text cleaning is the process of removing unwanted URLs, special characters, numbers and extra spaces from text.
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

text = """
hello!!! i am learning natural language processing.
the students are running and playing happily.
visit https://google.com for more information.
"""

# Step 1: Tokenization
tokens = word_tokenize(text)

# Step 2: Remove URLs    ---- List Comphrension[x:for in ]
clean_words = [
    word for word in tokens
    if not word.startswith(("https://", "http://", "www."))
]

# Step 3: Remove special characters and numbers
final_words = [
    word for word in clean_words
    if word.isalpha()
]

# Step 4: Combine words
clean_text = " ".join(final_words)

print("Cleaned Text:")
print(clean_text)




# hello i am learning natural language processing the students are running and playing happily visit https for more information