#function with no arguement & no return value

def printLine():
    print("*"*50)
printLine()
print("Welcome To user defined function in python")
printLine()

#function with argument & no return value.

def add(a,b):
    print("Addition:",a+b)
printLine()
x=int(input("Enter value : "))
y=int(input("Enter value : "))
add(x,y)
printLine()


#function with argument&retuen value

def sub(a,b):
    return a-b
printLine()
x=int(input("Enter value : "))
y=int(input("Enter value : "))
#ans=sub(x,y)
print("substraction : ",sub(x,y))
printLine()

    
