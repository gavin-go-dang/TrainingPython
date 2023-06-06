#Hackeerrank: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    def sub_string_to_string(sub_string):
        sub_string = list(sub_string)
        set_sub_string = []
        set_sub_string = [char for char in sub_string if char not in set_sub_string]
        return ''.join(set_sub_string)
    
    sub_strings = []
    for i in range(int(len(string) / k)):
        sub_strings.append(string[i * k : k * (i + 1)])
    result = [sub_string_to_string(sub_string) for sub_string in sub_strings]
    for sub_string in result:
        print(sub_string)

text = 'AAABCADDE'
print(merge_the_tools(text, 3))