sentence = input("Enter a sentence to parse: ")

sentence = sentence.split(" ")

parsedSentence = ''

# Started working on the methods instead after struggling with the code below

# Uppercase parser
def parseUppers(word):
    letterStr = word
    letterStr = letterStr.upper()
    return letterStr

# Lowercase parser
def parseLowers(word):
    letterStr = word
    letterStr = letterStr.lower()
    return letterStr

firstWord = parseLowers(sentence[0])

# Need to use this method with a loop instead of trying to apply to a range
# lastWords = parseLowers(sentence[0:])

print(firstWord)
# print(lastWords)

# wordCount = 0
#
# while wordCount < len(sentence):
#     firstUpper = ''
#     restLetters = ''
#     if wordCount == 0:
#         firstWord = sentence[wordCount].lower()
#         parsedSentence = firstWord
#     else:
#         letterCount = 0
#         while letterCount < len(sentence[wordCount]):
#         # for letter in sentence[wordCount]:
#             if letterCount == 0:
#                 sentence[wordCount[0]].upper()
#             else:
#                 sentence[wordCount[1:]].lower()
#             letterCount = letterCount + 1
#
#     wordCount = wordCount + 1
#     parsedSentence = parsedSentence
#
# print(parsedSentence)

# for letter in sentence:
#     sentence[letter] =

#
# for letter in sentence:
#     if letter == ' ':
#         letter.next.upper()


# print(sentence)