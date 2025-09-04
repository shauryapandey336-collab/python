a=140
if(a<3):
    print("the value of a is greater than 3")
elif(a<12):
    print("The value of a is greate than 12")    
elif(a<10):
    print("The value of a is greater than 10")
else:
    print("The value is not greater than 3 and 7")        

# login amin,hr,student 
username="hr"
password=4
# role="student"
# table :role (admin),hr,student 
if(username=="raj" and password==123):
    print("student login")
elif(username=="admin" and password==49):
    print("admin login")  
elif(username=="hr" and password==4):
    print("hr login")  
else:
    print("check username or password")        
