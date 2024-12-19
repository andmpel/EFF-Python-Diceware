import random

rng = random.SystemRandom()

def roll():
    return rng.randint(1, 6)

def rollx5():
    return ''.join(str(roll()) for _ in range(5))

def wordDict():
        with open('eff_large_wordlist.txt') as f:
            return {key: val for key, val in (line.strip().split() for line in f)}

def genWords(wordCount = int(input("Enter number of words to generate: "))):
    print(' '.join([wordDict().get(str(rollx5())) for _ in range(wordCount)]))

if __name__ == '__main__':
    genWords()
