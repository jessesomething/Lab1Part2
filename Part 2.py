
# User input and splits the string into words
sentence = input("Enter a sentence to parse: ")
sentence = sentence.split(" ")

# Camelcase parser
def camelCase(word):
    # Returns the first letter in upper and the rest in lowercase
    return word[0].upper() + word[1:].lower()

# Lowercase parser
def parseLowers(word):
    # Returns full word in lowercase
    return word.lower()

# Takes the first word from the phrase into a string
firstWord = parseLowers(sentence[0])

# Takes the last words from the phrase and adds to last word list
lastWordsList = sentence[1:]

# String init
lastWords = ''

# Reads words in list to apply to camelcase method
for word in range(len(lastWordsList)):
    lastWordsList[word] = camelCase(lastWordsList[word])

# Adds up the words to the last word string
for word in lastWordsList:
    lastWords = lastWords + word

print(firstWord + lastWords)