#Link Hackkerrank: https://www.hackerrank.com/challenges/python-quest-1/problem?isFullScreen=true
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i * (int(round(111111111 / (10 ** (9 - i)), 0))))