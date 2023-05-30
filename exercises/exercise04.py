#solution on https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
#read number in file input04.txt
#and write the result to file result04.txt

def get_number_list(listNum):
    return [int(number) for number in listNum]

f = open("inputs/input04.txt", "r")

number_in_line1 = str(f.readline()).split()
number_in_line2 = str(f.readline()).split()

list_number1 = get_number_list(number_in_line1)
list_number2 = get_number_list(number_in_line2)

result = list()
for number in list_number1:
    if number in list_number2:
        result.append(number)

f = open("results/result04.txt", "w")
for number in result:
    f.write(str(number )+ ' ')
f.close()



