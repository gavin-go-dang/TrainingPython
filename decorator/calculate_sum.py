#get a positive number and calculate sum in range from 1 to n
def calculate_sum(create_list):
    def get_sum(len_of_list):
        s = 0
        for number in create_list(len_of_list):
            s += number
        return s
    
    return get_sum

@calculate_sum
def create_list(len_of_list):
    return list(range(0, len_of_list+1)) # calculate_sum(create_list(len_of_list))


print(create_list(10))
