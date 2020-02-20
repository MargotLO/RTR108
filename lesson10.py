def exercise2():
    filename = input("Enter file :")
    try:
        file = open(filename)
    except:
        print("file not exist ", filename)
        exit()

    d = dict()

    for line in file:
        if line.startswith("From"):
            words = line.split()
            if (len(words)>2 and words[2] in d):
                d[words[2]]+=1
            elif(len(words)>2):
                d[words[2]]=1
    print(d)

def exercise3():
    filename = input("Enter file :")
    try:
        file = open(filename)
    except:
        print("file not exist ", filename)
        exit()

    d = dict()

    for line in file:
        if line.startswith("From "):
            words = line.split()
            if (len(words)>1 and words[1] in d):
                d[words[1]]+=1
            elif(len(words)>1):
                d[words[1]]=1
    print(d)
    return d

def exercise4():
    dico = exercise3()
    num = list(dico.values())
    print(dico.get(0,max(num)))#error here
    print(max(num))
exercise4()
