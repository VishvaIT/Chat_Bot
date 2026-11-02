# Definition: Stemming is the process of removing prefixes or suffixes from words to obtain their root-like form.

# For example:
# - playing → play
# - running → run
# - students → student
# - happily → happili
# Note: A stemmed word may not be a valid dictionary word.

from nltk.stem import PorterStemmer

# Tokens from previous step
filtered_tokens = [
    'hello', 'learning', 'natural', 'language',
    'processing', 'students', 'running',
    'playing', 'happily', 'visit', 'information'
]

# Create a stemmer
stemmer = PorterStemmer()

# Apply stemming
stemmed_words = [
    stemmer.stem(word)
    for word in filtered_tokens
]

print("Before Stemming:")
print(filtered_tokens)

print("\nAfter Stemming:")
print(stemmed_words)



# Before Stemming:
# ['hello', 'learning', 'natural', 'language', 'processing', 'students', 'running', 'playing', 'happily', 'visit', 'information']

# After Stemming:
# ['hello', 'learn', 'natur', 'languag', 'process', 'student', 'run', 'play', 'happili', 'visit', 'inform']


# Understand the important lines
# - PorterStemmer() – creates the stemming algorithm.
# - stemmer.stem(word) – removes word endings to produce a stem.
# - List comprehension – applies stemming to every word.
# Remember:

# Stemming = Removes word endings, sometimes producing incomplete words.

# Example: happily → happili