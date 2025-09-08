# no argument no retun 
def add():
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))
    c=a+b
    print("sum= ",c)
add() 
# with argument no return 
def add(a,b):
    c=a+b
    print("Addition=",c)
add(3,5)  

# no argument with return 
def add():
    a=int(input("enter 1st No:"))
    b=int(input("enter 2nd no:"))
    c=a+b
    return c
d=add()
print("Addition =",d)

# with argument with return 
def add(a,b):
    c=a+b
    return c
a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
x=add(a,b)
print("Addition=",x)