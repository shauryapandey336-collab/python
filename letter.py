letter = '''Dear <|NAME|>,
You are selected!
Have a great day
thanks and regard,
pninfosys <|NAME|>

Date : <|DATE|>
'''
name = input("Enter your name")
date = input("Enter date")

letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)