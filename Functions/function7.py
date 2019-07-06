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

number = int(input("Enter Number:"))
UniqueNumberCheck(number)
