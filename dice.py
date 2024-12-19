import random

def roll():
    return random.SystemRandom().randint(1, 6)

def rollx5():
    return ''.join(str(roll()) for _ in range(5))

def wordDict():
    with open('eff_large_wordlist.txt') as f:
        return dict(line.strip().split() for line in f)

def genWords(word_dict, wordCount):
    print(' '.join([word_dict.get(str(rollx5())) for _ in range(wordCount)]))

if __name__ == '__main__':
    genWords(word_dict = wordDict(), word_count = int(input("Enter number of words to generate: ")))
