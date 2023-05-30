#only print list if the first element in list is 0


def decorator_print_list(checklist):
    def print_list(list_numbers):
        if checklist(list_numbers):
            for number in list_numbers:
                print(number)
        else:
            print('invalid list')
    return print_list


@decorator_print_list
def checklist(list_numbers):
    if list_numbers[0]==0:
        return True
    return False

checklist([2,1,2,3,4,5])