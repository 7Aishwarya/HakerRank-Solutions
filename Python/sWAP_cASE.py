'''You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.'''


def swap_case(s):
    string = ""
    for i in s:
        if i.isupper() == True:
            string+=(i.lower())
        else:
            string+=(i.upper())
    return string
    
    

if __name__ == '__main__':