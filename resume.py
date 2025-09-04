Name=input("Enter your name: ")
Age=(input("Enter your age: "))
D=input("Enter your qualification: ")
University=input("enter your university/collge name: ")
Hobby=input("enter your hobbies: ")
gender=input("enter your gender")
exp=input("enter your experince")


resume=''' 
               My Resume
-------------            ---------------------
Name =is |<Name>|,
Age=|<Age>| 
Qualification= |<D>|,
Institute name= |<University>|,
Gender=|<Gender>|
Hobbies=|<Hobby>|
Experince=|<Exp>|

'''


resume=resume.replace("|<Name>|",Name)
resume=resume.replace("|<Age>|",Age)
resume=resume.replace("|<D>|",D)
resume=resume.replace("|<University>|",University)
resume=resume.replace("|<Hobby>|",Hobby)
resume=resume.replace("|<Gender>|",gender)
resume=resume.replace("|<Exp>|",exp)
print(resume)