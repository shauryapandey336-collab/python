Name=input("Enter your name")
Age=(input("Enter your age"))
Degree=input("Enter your degree name")
University=input("enter your university/collge name")
Hobby=input("enter your hobbies")



resume=''' 
               My Resume
-------------            ---------------------
My name is |<Name>|,
i am |<Age>| years old,
I currently persuing my <|D|>,
From |<University>|,
i want to be an software an engineer,
My hobbies are |<Hobby>|
'''


resume=resume.replace("|<Name>|",Name)
resume=resume.replace("|<Age>|",Age)
resume=resume.replace("|<D>|",Degree)
resume=resume.replace("|<University>|",University)
resume=resume.replace("|<Hobby>|",Hobby)
print(resume)