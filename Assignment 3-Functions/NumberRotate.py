def LNumberRotate(n,d):
    a=str(n)
    Lstart = a[0:d]
    Lend = a[d:]
    Lcomplete = Lend+Lstart
    return int(Lcomplete)

def RNumberRotate(n, d):
    a = str(n)
    Rstart = a[0:len(a)-d]
    Rend = a[len(a)-d:]
    Rcomplete = Rend+Rstart
    return Rcomplete

if __name__ == '__main__':
    n = int(input("Enter Number:"))
    d = int(input("Enter Number of rotations:"))
    # print(LNumberRotate(n,d))
    # print(RNumberRotate(n,d))
