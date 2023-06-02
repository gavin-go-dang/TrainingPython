import re


def check_username(username):
    valid_char = re.compile(r"[A-Za-z0-9-_]+")
    if re.fullmatch(valid_char, username):
        return True
    else:
        return False
    

def check_companyname(companyname):
    valid_char =  re.compile(r"[A-Za-z0-9]+")
    if re.fullmatch(valid_char, companyname):
        return True
    else:
        return False

def check_extension(extension):
    valid_char = re.compile(r"[A-Za-z]+")
    if re.fullmatch(valid_char, extension):
        return True
    else:
        return False
    

def check_all_extension(extensions):
    if len(extensions) > 3 or len(extensions) < 1:
        return False
    if not all(map(check_extension, extensions)):
            return False
    return True


def valid(email):
    if len(re.findall('@', email)) != 1:
        return False
    
    email_component = email.split('@')

    if not check_username(email_component[0]):
        return False
    
    tail = email_component[1].split('.')

    if not check_companyname(tail[0]):
        return False

    if not check_all_extension(tail[1:]):
        return False

    return True

list_email = [
    'greenrock@gmail.com.vn.net.us',
    'abc@mail.com.vn',
    'cd09..@gmail.com',
    'regedit@gmail.abc101.vn',
    'greenrock@gmail.com.vn.net.us',
    'abc@gmail'
]

a = list(map(valid, list_email))

print(a)


list_email_valid = list(filter(lambda x: valid(x), list_email))
print(list_email_valid)