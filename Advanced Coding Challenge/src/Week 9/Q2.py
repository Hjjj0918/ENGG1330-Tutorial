'''
@ENGG1330: Computer Programming 1
The suggested solution for Advanced Coding Challenge # 2
'''


def addNumbers(phonebook, name, phones):
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].extend(phones)


def showNumbers(phonebook ,name):
    if name in phonebook:
        print(sorted(phonebook[name],reverse=True))
    
    else:
        print(name, 'not found')


def findNumber(phonebook, Number):
    for name, numbers in phonebook.items():
        for num in numbers:
            if num == Number:
                return print(name)
                
    print(f'{Number} not found')  

def main(): 
    phonebook = {} 
    
    command = input().split() 
    while (command[0] != 'END'): 
        if command[0] == 'ADD':
            addNumbers(phonebook, command[1], command[2:])
        elif command[0] == 'SHOW':
            showNumbers(phonebook, command[1])
        elif command[0] == 'FIND':
            findNumber(phonebook, command[1])
        
        command = input().split() 


main()