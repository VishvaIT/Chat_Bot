# Definition: Final clean data is the preprocessed text obtained after applying the required NLP preprocessing techniques. It can be used for further NLP tasks like sentiment analysis, text classification and chatbot development.

# Lemmatized words from previous step
lemmatized_words = [
    'hello', 'learn', 'natural', 'language',
    'processing', 'student', 'run', 'play',
    'happily', 'visit', 'information'
]

# Combine words into a sentence
final_text = " ".join(lemmatized_words)

print("FINAL PREPROCESSED TEXT:")
print(final_text)


# FINAL PREPROCESSED TEXT:
# hello learn natural language processing student run play happily visit information






# " " – inserts a space between words.



# join() – combines all list elements into one string.



# final_text – stores the final preprocessed sentence.