l =input().split()
n = int(l[0])
m = int(l[1])
pattern = ".|."
welcome = "WELCOME"
patt = -1
pattlen = 3
dash = "-"

for i in range(n):
    #for j in range(n):
    if (i==int(n/2)):
        for k in range(int((m-7)/2)):
            print(dash,end = "")
        print(welcome,end = "")
        for k in range(int((m-7)/2)):
            print(dash,end = "")
        print("")
    
    elif (i < int(n/2)):
        patt +=2
        pattlen = 3*patt
        for k in range(int((m-pattlen)/2)):
            print(dash,end="")
        for k in range(patt):
            print(pattern,end="")
        for k in range(int((m-pattlen)/2)):
            print(dash,end="")
        print("")
        
    else:
        for k in range(int((m-pattlen)/2)):
            print(dash,end="")
        for k in range(patt):
            print(pattern,end="")
        for k in range(int((m-pattlen)/2)):
            print(dash,end="")
        print("")
        patt -=2
        pattlen = patt*3
