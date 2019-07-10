def Input(list):
    n = int(input("Enter Size of Array:"))
    for i in range(n):
        num = input("Enter {}st element of array:".format(i+1))
        list.append(num)

if __name__ == '___main__':
        list = []
        Input(list)

