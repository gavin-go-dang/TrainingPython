#solution on https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
#read number in file input03.txt
#and write the result to file result03.txt


f = open("inputs/input03.txt", "r")

number_in_line = str(f.readline())

list_number = number_in_line.split()
small10 = list()
for number in list_number:
    if int(number) < 10:
        small10.append(number)


f = open("results/result03.txt", "w")
for number in small10:
    f.write(number + ' ')
f.close()



