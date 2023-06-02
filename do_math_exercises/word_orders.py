#HackerRank: https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

def count_word(list_word):
    count_result = dict()

    for i in list_word:
        if i not in count_result.keys():
            count_result[i] = 1
        else:
            count_result[i] += 1

    sorted_count_result = sorted(count_result.items(), key = lambda key: key[1],  reverse=True)
    return sorted_count_result


# list_word = [
#     'abc',
#     'abcde',
#     'ab',
#     'avds',
#     'ab'
# ]

n = int(input())
list_word = []
for i in range(n):
    list_word.append(input())
result = count_word(list_word)
print(len(result))
for value in result:
    print(value[1])
