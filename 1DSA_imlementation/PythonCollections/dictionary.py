thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 200

}
# Access Items in dictionary
x = thisdict["brand"]
print(x)
y = thisdict.get("model")
print(y)

dict_keys = thisdict.keys()
dict_values = thisdict.values()
print(dict_keys)
print(dict_values)

thisdict["color"] = "white"
print(dict_keys)
print(dict_values)