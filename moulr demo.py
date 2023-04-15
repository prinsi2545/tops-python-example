import UDF

while True:
    print("*"*50)
    print("1.oddeven")
    print("2.maxoftwo")
    print("3.maxof three")
    print("4.prime")
    print("5.fibonacci")
    print("6.exit")
    print("*"*50)
    choice=int(input("enter your choice:"))
    print("*"*50)
    if choice==1:
        n1=int(input("enter value:"))
        UDF.oddeven(n1)
        print("*"*50)
        
    elif choice==2:
        n1=int(input("enter value:"))
        n2=int(input("enter value:"))
        UDF.maxoftwo(n1,n2)
        print("*"*50)

    elif choice==3:
        n1=int(input("enter value:"))
        n2=int(input("enter value:"))
        n3=int(input("enter value:"))
        UDF.maxofthree(n1,n2,n3)
        print("*"*50)

    elif choice==4:
        n2=int(input("enter value:"))
        UDF.prime(n2)
        print("*"*50)

    elif choice==5:
        n2=int(input("enter value:"))
        UDF.fibonacci(n2)
        print("*"*50)
    else:
        print("good bye")
        break
    
        
        
    
