import random
rng = random.SystemRandom()


def roll():
    return rng.randint(1, 6)


def rollx5():
    num5 = ''
    for count in range(5):
        num5 = num5 + str(roll())
        count += 1
    return num5


def wordDict():
    d = {}
    with open('eff_large_wordlist.txt') as f:
        for line in f:
            (key, val) = line.split()
            d[str(key)] = val
    return d


def genWords(wordCount = int(input("Enter number of words to generate: "))):
    d = wordDict()
    words = ""
    for count in range(wordCount - 1):
        wordKey = rollx5()
        words += str(d.get(wordKey)) + " "
        count += 1
    else:
        wordKey = rollx5()
        words += str(d.get(wordKey))
    print(words)


genWords()
