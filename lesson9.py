def exercise4():
    filename = input("Enter file :")
    try:
        file = open(filename)
    except:
        print("Incorrect filename")
        exit()
    t=[]
    for line in file:
        l = line.split()
        for word in l:
            if not word in t:
                t.append(word)
    t.sort()
    print(t)

def exercise5():
    filename = input("Enter file :")
    try:
        file = open(filename)
    except:
        print("Incorrect filename")
        exit()
    count = 0
    for line in file:
        if line.startswith("From "):
            l = line.split()
            print(l[1])
            count+=1

    print("There were " +str(count)+" lines in the file with From as the first word")

def exercise6():
    num = []
    while(True):
        inp = input("Enter a number : ")
        if inp == "done":
            break
        try :
            n = float(inp)
            num.append(n)
        except:
            print("is not a number")

    print("Maximum :" + str(max(num)))
    print("Minimum :" + str(min(num)))


            
        
