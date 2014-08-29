# Purpose: practice using strings
# Using the multi-line string below containing quotes from Einstein, please fill in the necessary code for the respective task.

quotes = """
(1) "A person who never made a mistake never tried anything new."
(2) "Look deep into nature, and then you will understand everything better."
(3) "Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop questioning."
(4) "Insanity: doing the same thing over and over again and expecting different results."
"""

# 1. Print quotes
print(quotes)

# 2. Count the number of occurrences of the string "i", and print the result
print(quotes.count("i"))

# 3. Create a new quote string with all the occurrences of the string "i" capitalized, and print the result
new_quotes = quotes.replace("i", "I")
print(new_quotes)

# 4. (a) Replace each of the following keys words with all caps: "new", "Look", "nature", "Learn", "live", "hope", "Insanity", and print the updated quotes
quotes1 = quotes
quotes1 = quotes1.replace("new", "NEW")
quotes1 = quotes1.replace("Look", "LOOK")
quotes1 = quotes1.replace("nature", "NATURE")
quotes1 = quotes1.replace("Learn", "learn".upper())
quotes1 = quotes1.replace("live", "live".upper())
quotes1 = quotes1.replace("hope", "hope".upper())
quotes1 = quotes1.replace("Insanity", "insanity".upper())

print(quotes1)

# 4. (b) Replace each of the following keys words with all caps: "new", "Look", "nature", "Learn", "live", "hope", "Insanity", and print the updated quotes
key_words = ["new", "Look", "nature", "Learn", "live", "hope", "Insanity" ]
quotes2 = quotes
for key_word in key_words:
	quotes2 = quotes2.replace(key_word, key_word.upper())

print(quotes2)


