# Lowercase Conversion

text = """
HELLO!!! I am learning Natural Language Processing.
The students are running and playing happily.
Visit https://google.com for more information.
"""

lower_text = text.lower()

print("ORIGINAL TEXT:")
print(text)

print("LOWERCASE TEXT:")
print(lower_text)



# ORIGINAL TEXT:

# HELLO!!! I am learning Natural Language Processing.
# The students are running and playing happily.
# Visit https://google.com for more information.

# LOWERCASE TEXT:

# hello!!! i am learning natural language processing.
# the students are running and playing happily.
# visit https://google.com for more information.


# Explanation
# - text – stores the original text.
# - .lower() – converts uppercase letters into lowercase.
# - lower_text – stores the converted text.
# - print() – displays the result.