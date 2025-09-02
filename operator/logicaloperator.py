a=10
b=12
c=10
d=True
if(a==b and a==c):
    print("hello")
else:
    print("world")    
if(b==a or b==c):
    print("hi") 
else:
    print("bye")    
print(not d) 

# another example 
b=12
x=5
print(b>3 and b<100)
print(b>3 or b<4)
print(not(x>3 and x<10))

username="ram"
password=12345
if(not(username=="ram" and password=='12345')):
    print("login")
else:
    print("username or password not match")    