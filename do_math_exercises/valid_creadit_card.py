#HackerRank: https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true

import re

def check_first_number(digits):
    if digits[0] not in ['4' ,'5', '6']:
        return False
    return True



def check_len(digits):
    if len(digits.replace('-', '')) != 16:
        return False
    
    return True

def check_group(digits):
    group_digit = []
    if '-' in digits:
        group_digit = digits.split('-')
    else:
        for i in range(int(len(digits) / 4)):
            group_digit.append(digits[i * 4 : 4 * (i + 1)])
    
    valid_char = re.compile(r"[0-9]+")
    
    if not all(list(map(lambda x: True if re.fullmatch(valid_char, x) else False, group_digit))):
        return False
    
    if not all(list(map(lambda x: True if len(x) == 4 else False, group_digit))):
        return False
     
    return True

def check_separator_and_ditgit(credit_number):
    
    valid_char = re.compile(r"[0-9-]+")
    if re.fullmatch(valid_char, credit_number):
        return True
    else:
        return False
    
def check_repeat(credit_number):
    credit_number = credit_number.replace('-', '')
    for i in range(len(credit_number)-4):
        if (int(credit_number[i : i+4]) % 1111 == 0):
            return False
        
    return True
        

def check_credit_number(credit_number):
    if not check_first_number(credit_number):
        return 'Invalid'
    
    if not check_len(credit_number):
        return 'Invalid'
    
    if not check_group(credit_number):
        return 'Invalid'
    
    if not check_separator_and_ditgit(credit_number):
        return 'Invalid'
    
    if not check_repeat(credit_number):
        return 'Invalid'

    return 'Valid'


list_credit_card = [
'4123456789123456',
'5123-4567-8912-3456',
'61234-567-8912-3456',
'4123356789123456',
'5133-3367-8912-3456',
'5123 - 3567 - 8912 - 3456'
]

for x in list(map(check_credit_number, list_credit_card)):
    print(x)