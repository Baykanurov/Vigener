from application.function.vigenereCipher import LETTERS

LETTERS_AND_SPACE = LETTERS + LETTERS.lower() + ' \t\n'


def loadDictionary():
    dictionaryFile = open('D:/Devops/Vigner/application/function/russian.txt', encoding="utf-8")
    englishWords = []
    for word in dictionaryFile.read().split('\n'):
        englishWords.append(word.upper())
    dictionaryFile.close()
    return englishWords


ENGLISH_WORDS = loadDictionary()


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0  # No words at all, so return 0.0.

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def isEnglish(message, wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
