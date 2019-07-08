# Take as input a number. Assume that for a number of n digits, the value of each
# digit is from 1 to n and is unique. E.g. 32145 is a valid input number.
def UniqueNumberCheck(number):
    number = str(number)
    flag = False
    for i in range(len(number)-1):
        for j in range(i+1,len(number),1):
            if number[i]==number[j]:
                print("This is not a valid input number")
                flag = True
    if flag == False:
        print("This is a valid input number")
if __name__ == '__main__':
    number = int(input("Enter Number:"))
    UniqueNumberCheck(number)
