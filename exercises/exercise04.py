#solution on https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#read number in file input04.txt
#and write the result to file result04.txt

def getNumberList(listNum):
    return [int(number) for number in listNum]

f = open("inputs/input04.txt", "r")

number_in_line1 = str(f.readline()).split()
number_in_line2 = str(f.readline()).split()

listNumber1 = getNumberList(number_in_line1)
listNumber2 = getNumberList(number_in_line2)

result = list()
for number in listNumber1:
    if number in listNumber2:
        result.append(number)

f = open("results/result04.txt", "w")
for number in result:
    f.write(str(number )+ ' ')
f.close()



