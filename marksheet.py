name=input("enter your name:")
p=input("enter physcis marks:")
c=input("enter chemistry marks:")
m=input("enter maths marks:")

marksheet='''Name:<|name|>
   Marksheet
------------------
physics | <|p|>
chemistry | <|c|>
maths | <|m|>
'''
marksheet=marksheet.replace("<|p>",p)
marksheet=marksheet.replace("<|c>",c)
marksheet=marksheet.replace("<|m>",m)
marksheet=marksheet.replace("<|name>",name)
print(marksheet)
print("Total   |",int(p),int(c),int(m))