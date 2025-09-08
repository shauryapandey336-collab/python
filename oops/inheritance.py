class papa:
    
    bike="007"

    def showDetails(self):
        print("This is an employee")
class son(papa):
  
    bike="008"
    language="python"
    def getLanguage(self):
        print(f"The language is {self.language}")   
    def showDetails(self):
        print("This is an programmer")    
p=son()
print(p.language)
p.showDetails()
print(p.bike)   


# pahle son bale me check krega agar usme mila gaya to theek hai wrna papa bali class se call krdega 