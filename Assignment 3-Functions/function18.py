# Take as input a character ch. Write a function that returns ‘U’, if it is uppercase
# ‘L’ if it is lowercase and ‘I’ otherwise. Print the value returned

def CaseCheck(ch):
    if ch.isupper():
        print('U')
    elif ch.islower():
        print('L')
    else:
        print('I')
    
if __name__ == '__main__':
    ch = input("Enter Character")
    CaseCheck(ch)
