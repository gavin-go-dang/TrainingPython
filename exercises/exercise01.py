#solution on https://www.practicepython.org/exercise/2014/01/29/01-character-input.html 
#and write the result to file result.txt

from datetime import date


print('Enter your name: ')
name = input()
print('Enter your age: ')
age = int(input())

today = date.today()
current_year = today.strftime("%Y")
result = name + ' will turn 100 years old in ' + str(int(current_year )+ 100 - age)
print(result)

#write result to file result01.txt
f = open("results/result01.txt", "w")
f.write(result)
f.close()