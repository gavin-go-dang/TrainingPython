#Hackerrank: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

def create_list_fibonaci(n):
    list_num = [1]
    if n ==1: 
        return list_num
    list_num.append(1)
    if n == 2: 
        return list_num
    for i in range(2, n):
        fibo = list_num[-1]+ list_num[-2]
        list_num.append(fibo)
    return list_num

def cube(n):
    return n**3

def cubes_fibonaci_map(n):
    return list(map(cube, create_list_fibonaci(n)))

print(cubes_fibonaci_map(6))


cube_lambda = lambda list_nums: list(i ** 3 for i in list_nums)
print(cube_lambda(create_list_fibonaci(6)))