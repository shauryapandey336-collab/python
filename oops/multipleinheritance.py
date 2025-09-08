class Employee: #papa ki car
    car="pninfosys"
    ecode=120
class Freelancer: #chacha ki car
    car="google"
    level=0

    def upgradelevel(self):
        self.level=self.level+1

class Programmer(Freelancer,Employee):
    name="vikas"  
    # car="321" apni khud ke car

p=Programmer()
print(p.car) # pahle khud ke liye check krega ,chacah ki pass check krega mili wrna papa ki pass check krega
p.upgradelevel()              