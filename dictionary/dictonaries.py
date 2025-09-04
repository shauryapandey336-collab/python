a={
    "name": "pninfosys rohit",
    "collage":"itm",
    # "collage":"itm", duplicate keys are not aalowed
    2:[1,2,3,4,1,1,(2,4,5.5)],
    4:("ram","mohit"),
    "education":{'ram':'MCA'},
    "city":"gwalior",
}
print(a)
print(type(a))
print(a["name"])
print(a[2]) #this is not induxing this is the name of key
# print(a[0]) not availablle error 
print(a[2][6])
print(type(a[2][6]))
print(type(a[4]))
print(a["education"]["ram"])
print(a[2][6][1])
print(a["education"]["ram"][1])
print(a["city"][1])
print(type(a["city"]))
print(a["city"])

a[4]=(40,50,60,59,5.6)
a["name"]="raj"
print(a)