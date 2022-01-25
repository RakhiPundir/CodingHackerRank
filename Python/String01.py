if __name__ == '__main__':
    s = input()
    alnum = 0
    upper = 0
    lower = 0
    alpha = 0
    num = 0
    for i in s:
        if(i.isalnum()):
            alnum += 1
        
        if(i.isalpha()):
            alpha += 1
        if(i.isdigit()):
            num += 1
        if(i.isupper()):
            upper += 1
        if(i.islower()):
            lower += 1
    
    if(alnum > 0):
        print("True")
    else:
        print("False")
    
    if(alpha > 0):
        print("True")
    else:
        print("False")
    
    if(num > 0):
        print("True")
    else:
        print("False")
    
    if(lower > 0):
        print("True")
    else:
        print("False")
        
        
    if(upper > 0):
        print("True")
    else:
        print("False")
    
