def numberofline(file):
    fhand = open(file)
    count =0
    for line in fhand:
        count +=1
    print('Line count :', count)
    fhand.close()

numberofline('mbox.txt')

def numberofchar(file):
    fhand = open(file)
    inp = fhand.read()
    print(len(inp))
    print(inp[:20])

numberofchar('mbox.txt')

def exercise1():
    filename= input('Enter a file name :')
    try:
        fhand = open(filename)
    except:
        print('File cannot be opened:', filename)
        exit()
    for line in fhand:
        print(line.upper())

    fhand.close()
        
#exercise1()

def exercise2():
    filename= input('Enter a file name :')
    try:
        fhand = open(filename)
    except:
        print('File cannot be opened:', filename)
        exit()
    count = 0
    cline =0
    for line in fhand:
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence:'):
            count += float(line[20:])
            cline+=1
    print(count/cline)

#exercise2()

def exercise3():
    filename= input('Enter a file name :')
    if(filename=='na na boo boo'):
        print('NA NA BOO BOO TO YOU - You have been punk \'d!')
        exit()
    try:
        fhand = open(filename)
        
    except:
        print('File cannot be opened:', filename)
        exit()
    count = 0
    for line in fhand:
        line = line.rstrip()
        if line.startswith('Subject'):
            count += 1

    print('There were',count, 'subject lines in', filename)
            
#exercise3()       
