sentence = input("Enter a sentence to parse: ")

sentence = sentence.split(" ")

parsedSentence = ''

wordCount = 0

while wordCount < len(sentence):
    firstUpper = ''
    restLetters = ''
    if wordCount == 0:
        firstWord = sentence[wordCount].lower()
        parsedSentence = firstWord
    else:
        letterCount = 0
        while letterCount < len(sentence[wordCount]):
        # for letter in sentence[wordCount]:
            if letterCount == 0:
                sentence[wordCount[0]].upper()
            else:
                sentence[wordCount[1:]].lower()
            letterCount = letterCount + 1

    wordCount = wordCount + 1
    parsedSentence = parsedSentence

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