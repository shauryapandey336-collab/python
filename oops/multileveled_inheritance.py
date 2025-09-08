class Person:
    country="india"

    def takeBreath(self):
        print("gwalior")

class Employee(Person):
    company="honda"

    def getSalary(self):
        print("salary 10000")
    def takeBreath(self):
         super().takeBreath()   
         print("pninfosys")

class Programmer(Employee):
    company="fiverr"

    def getSalary(self):
         super().getSalary()  #tu bhi aaa 
         print(f"no slaary to programmers")
    def takeBreath(self):
        super().takeBreath() 
        print("i am a programmer so i am luckily breathing")

p=Programmer()
p.takeBreath()

# super key word is used to call all method with the help of super keyword 
                           