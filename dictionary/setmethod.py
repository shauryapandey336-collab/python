a=set()
a.add(4)
a.add(5)
# a.add(4,5) not allowed 
a.add("pn")
# a.add([5,7,8]) set ki aandar list ko ad nahi kar skte 
a.add((5,7,8)) #tupple ko add kar skte hai
# a.add({5:7}) set ke aandar dict nhi aaegi 
print(len(a))
a.remove(5)
print(a)

#clear()
a.clear()
print(a)
