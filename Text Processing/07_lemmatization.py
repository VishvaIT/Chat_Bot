# Definition: Lemmatization converts a word into its meaningful dictionary base form (lemma).

# Examples:
# - playing → play
# - running → run
# - students → student
# - better → good
# Difference from Stemming: Stemming may produce incomplete words, whereas lemmatization aims to produce valid dictionary words.

import nltk
from nltk.stem import WordNetLemmatizer

# Download required WordNet data
nltk.download('wordnet')

# Tokens from previous step
filtered_tokens = [
    'hello', 'learning', 'natural', 'language',
    'processing', 'students', 'running',
    'playing', 'happily', 'visit', 'information'
]

# Create lemmatizer
lemmatizer = WordNetLemmatizer()

# Apply lemmatization
lemmatized_words = []

for word in filtered_tokens:

    if word in ['running', 'playing', 'learning']:
        result = lemmatizer.lemmatize(word, pos='v')
    else:
        result = lemmatizer.lemmatize(word)

    lemmatized_words.append(result)

print("Before Lemmatization:")
print(filtered_tokens)

print("\nAfter Lemmatization:")
print(lemmatized_words)



# Before Lemmatization:
# ['hello', 'learning', 'natural', 'language', 'processing', 'students', 'running', 'playing', 'happily', 'visit', 'information']

# After Lemmatization:
# ['hello', 'learn', 'natural', 'language', 'processing', 'student', 'run', 'play', 'happily', 'visit', 'information']






# Understand the important lines
# - WordNetLemmatizer() – creates the lemmatizer.
# - lemmatize(word) – converts a word into its dictionary base form, assuming a noun by default.
# - pos='v' – tells the lemmatizer to treat the word as a verb.
# - append() – adds each processed word to the result list.
# Important: Lemmatization uses grammatical information (part of speech) to find the correct base form.


# Stemming vs Lemmatization
# Stemming	Lemmatization
# Removes word endings	Finds dictionary base form
# Faster and simpler	Uses linguistic knowledge
# happily → happili	happily → happily