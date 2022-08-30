"""
You might have heard of Markov text generators. They’ve become popular for enter‐
tainment purposes, as in the “That can be my next tweet!” app, as well as their use for
generating real-sounding spam emails to fool detection systems.
All of these text generators are based on the Markov model, which is often used to
analyze large sets of random events, where one discrete event is followed by another
discrete event with a certain probability.
******************* Notes ********************
1. All percentages leading away from the node must add up to exactly 100%. No matter how complicated the system,  there
must always be a 100% chance that it can lead somewhere else in the next step.
2. Although there are only three possibilities for the weather at any given time, you
can use this model to generate an infinite list of weather states.
3. Only the state of the current node you are on influences where you will go to next. If you’re on the Sunny node,
it doesn’t matter if the preceding 100 days were sunny or rainy—the chances of sun the next day are exactly the same: 70%.
4. It might be more difficult to reach some nodes than others.

"""

from urllib.request import urlopen
from random import randint


def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum


def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word


def buildWordDict(text):
    # remove newlines and quotes
    text = text.replace('\n', '')
    text = text.replace('"', '')

    # Make sure punctuation marks are treated as their own 'words',
    # so that they will be included in the Markov chain
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, f'{symbol}')

    words = text.split(' ')
    # Filter out empty words
    words = [word for word in words if word != '']
    wordDict = {}
    for i in range(1, len(words)):
        if words[i - 1] not in wordDict:
            # Create a new dictionary for this word
            wordDict[words[i - 1]] = {}
        if words[i] not in wordDict[words[i - 1]]:
            wordDict[words[i - 1]][words[i]] = 0
        wordDict[words[i - 1]][words[i]] += 1
    return wordDict


text = str(urlopen('https://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
wordDict = buildWordDict(text)
# Generate a Markov chain of length 100
length = 100
chain = ['I']
for i in range(0, length):
    newWord = retrieveRandomWord(wordDict[chain[-1]])
    chain.append(newWord)
print(' '.join(chain))
