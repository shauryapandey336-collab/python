a={
    "name":"pninfosys",
    "college":"RJIT",
    "mark":[1,2,3,4],
    "education":{'ram':'mca'},
    1:2,

}
# print(a["college78"]) ye error h
print(a.get("college1")) #get lagake null show kewga na ki error
print(a.keys())
print(type(a.keys()))
print(list(a.keys()))
print(a.values())
print(a.items())

updatedict={
    "branch":"it",
    "phone":98378736,
    "salary":4000,
    "name":"rohit"
}
a.update(updatedict)
print(a)