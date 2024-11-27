import random

rng = random.SystemRandom()

def roll():
    return rng.randint(1, 6)

def rollx5():
    return ''.join(str(roll()) for _ in range(5))

def wordDict():
    try:
        with open('eff_large_wordlist.txt') as f:
            return {key: val for key, val in (line.strip().split() for line in f)}
    except FileNotFoundError:
        print("Word list file 'eff_large_wordlist.txt' not found.")
        exit(1)

def genWords(wordCount = int(input("Enter number of words to generate: "))):
    d = wordDict()
    words = []
    for _ in range(wordCount):
        wordKey = rollx5()
        word = d.get(wordKey)
        words.append(word)
    print(' '.join(words))

if __name__ == '__main__':
    genWords()
