import random
rng = random.SystemRandom()


def roll():
    return rng.randint(1, 6)


def rollx5():
    num5 = ''
    count = 0
    while count < 5:
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


def genWords():
    d = wordDict()
    count = 0
    while count < 6:
        wordKey = rollx5()
        print(d.get(wordKey))
        count += 1
