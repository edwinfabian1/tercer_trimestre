#clave - valor
d={}
dict={"gato":"cat",
      "perro":"dog",
      "vaca":"cow",
      "caballo":"horse",
}
print(dict)
print(sorted(dict.values()))

print(dict.get("perro"))

print(dict["vaca"])

del dict["perro"]
print(dict)

dict["raton"]="mouse"
print(dict)

dict.update(["perro","dog"])
print(dict)

dict.popitem()
print(dict)

for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)

for k,v in dict.item():
    print(k,"->",v)

for item in dict.items():
    print(item)