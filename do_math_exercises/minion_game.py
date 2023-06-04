#HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true


import re


def get_n_word(string, n):
    list_word_stuart = []
    list_word_kevin = []

    for i in range(len(string)-n+1):
        if string[i:i+n] not in list_word_stuart and not re.match(r'[aeiouAEIOU]', string[i]):
            list_word_stuart.append(string[i:i+n])    

        if string[i:i+n] not in list_word_kevin and re.match(r'[aeiouAEIOU]', string[i]):
            list_word_kevin.append(string[i:i+n])
    return [list_word_kevin, list_word_stuart]

def calculate_point(string):
    score_kevin = 0
    score_stuart = 0

    for len_word in range(1, len(string)+1):
        list_word = get_n_word(string, len_word)
        for word in list_word[0]:
            score_kevin += len(re.findall(word, string))
        for word in list_word[-1]:
            score_stuart += len(re.findall(word, string))

    if score_kevin > score_stuart:
        return 'Kevin {}'.format(score_kevin)
    elif  score_kevin < score_stuart:
        return 'Stuart {}'.format(score_stuart)
    else:
        return 'Draw'

print(calculate_point('banana'))