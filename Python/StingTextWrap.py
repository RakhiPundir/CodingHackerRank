def wrap(string, max_width):
    para = ""
    for i in range(len(string)):
        j=i+1
        if (j % max_width==0):
            para = para + string[i] + "\n"
        else:
            para = para + string[i]    
    return(para)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
