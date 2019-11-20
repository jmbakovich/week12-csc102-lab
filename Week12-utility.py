#Jackson Bakovich
#CSCI102 - Section A
#Week 12 - Part A

def PrintOutput(something):
    print('OUTPUT', something)

def LoadFile(filename):
    with open(filename, 'r') as file:
        reader = file.read()
        read_list = reader.split('\n')
    PrintOutput(read_list)

def UpdateString(string, letter, num):
    string = list(string)
    string[num] = str(letter)
    new_string = str()
    for i in range(len(string)):
        new_string += string[i]
    PrintOutput(new_string)

def FindWordCount(file,string):
    with open(file, 'r') as filename:
        read = filename.read()
        count = read.count(string)
    PrintOutput(string)

def ScoreFinder(plist,slist,name):
    status = 0
    for i in range(len(plist)):
        if (plist[i].upper()) == (name.upper()):
            PrintOutput(plist[i],'got a score of', slist[i])
            status = 1
    if status == 0:
        PrintOutput('player not found')

def Union(slist,plist):
    finallist = slist + plist
    PrintOutput(finallist)

def Intersection(lista,listb):
    listc = []
    for i in range(len(lista)):
        for j in range(len(listb)):
            if lista[i] == listb[j]:
                listc.append(lista[i])
    PrintOutput(listc)

def NotIn(lista,listb):
    notlist = list(set(lista).difference(set(listb))) #https://stackoverflow.com/questions/51922547/python-contrast-2-lists

    PrintOutput(notlist)
 
