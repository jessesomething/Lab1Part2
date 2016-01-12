sentence = input("Enter a sentence to parse: ")

sentence = sentence.split(" ")

parsedSentence = ''

wordCount = 0

while wordCount < len(sentence):
    restWords = ''
    if wordCount == 0:
        firstWord = sentence[wordCount].lower()
        parsedSentence = firstWord
    else:
        for word in sentence[wordCount]:
            firstUpper = word[0].upper()
            lastLetters = word[1:].lower()
            restWords = restWords + firstUpper + lastLetters

    wordCount = wordCount + 1
    parsedSentence = parsedSentence + restWords

print(parsedSentence)

# for letter in sentence:
#     sentence[letter] =

#
# for letter in sentence:
#     if letter == ' ':
#         letter.next.upper()

def parseUppers(letter):
    letterStr = letter
    for letter in letterStr:
        letter.upper()
    return letterStr

def parseLowers(letter):
    letterStr = letter
    for letter in letterStr:
        letterStr.lower()
    return letterStr

print(sentence)