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

