# class iphone16:
#     x=5
# # ek method banaya 
# def user(self,a):
#     print("hello user",a)
# p1=iphone16() #object  
# print(p1.x)
# p1.user(2) #yaha se 2 value class me jaenge to class method ko call krega par agar method me koi argument nhi hoga to argument hume deni padegi      

class pninfosys:
    company="pninfosys"
    age=12
    college="itm"

    def itm(self,a):
        # self is used to call variable globally 
        print(f"hello itm {self.company} is {self.age} is {self.college}\n{a}")
        print("hello",a)

data=pninfosys() #this is object
print(data.company)
data.itm(2)
       