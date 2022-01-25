def print_formatted(number):
    for i in range(1,number+1):
        l1 = len(bin(number)[2:])
        print(str(i).rjust(l1,' '), end=" ")
        # octal number
        print(octal(i).rjust(l1,' '), end=" ")
        print(hexa(i).rjust(l1,' '), end=" ")
        print(binary(i).rjust(l1,' '), end=" ")
        print ("")   
    # your code goes here
def octal(n):
    strn =''
    while(n>0):
        rem = n%8
        n = int(n/8)
        strn = strn + str(rem)
    string = "".join(reversed(strn)) 
    return(string)

def hexa(n):
    strn =''
    while(n>0):
        rem = n%16
        if(rem == 10):
            rem = 'A'
        if(rem == 11):
            rem = 'B'
        if(rem == 12):
            rem = 'C'
        if(rem == 13):
            rem = 'D'
        if(rem == 14):
            rem = 'E'
        if(rem == 15):
            rem = 'F'
        n = int(n/16)
        strn = strn + str(rem)
    string = "".join(reversed(strn)) 
    return(string)

    
def binary(n):
    strn =''
    while(n>0):
        rem = n%2
        n = int(n/2)
        strn = strn + str(rem)
    string = "".join(reversed(strn)) 
    return(string)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
