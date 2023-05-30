#add tag to format text: bold, italic, underline

def make_bold(fn):
    def wrap():
        return '<b>' + fn() + '</b>'
    return wrap

def make_italic(fn):
    def wrap():
        return '<i>' + fn() + '</i>' 
    return wrap

def make_underline(fn):
    def wrap():
        return '<u>' + fn() + '</u>'  
    return wrap


@make_bold
@make_italic
@make_underline
def input_text():
    text = input()
    return 'hello' + text

hello_message = input_text()
print(hello_message)