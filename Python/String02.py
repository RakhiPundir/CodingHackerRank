def swap_case(s):
    string=""
    for i in s:
        if (i.isalpha()):
            if (i.isupper()):
                i = i.lower()
                string = string+i
            elif (i.islower()):
                i = i.upper()
                string = string+i
        else:
            string = string+i
    return(string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
