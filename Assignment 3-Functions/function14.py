def Log(n,x):
    counter=1
    base=n
    
    while(True):
        base=base*n
        counter=counter+1
        
        if(base==x):
            return counter
        
if __name__=='__main__':
    n=int(input("Enter Base:"))        
    x=int(input("Enter Number:"))
    print(Log(n,x))        
        
        
        
        