#solution on https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#read number in file input02.txt
#and write the result to file result.txt


f = open("inputs/input02.txt", "r")

number = int(f.readline())

result = 'even' if number % 2== 0 else 'odd'
print(result)


f = open("results/result02.txt", "w")
f.write(result)
f.close()



