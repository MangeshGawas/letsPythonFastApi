user_dictionary = {
    "username":'codingwithMangesh',
    'name':"Mangesh",
    'age':26
}

print(user_dictionary)
print(user_dictionary.get("username"))

user_dictionary["married"] = False

for x,y in user_dictionary.items():
    print(x, y)

user_dictionary.pop("age")

print(user_dictionary)

user_dictionary.clear()
print(user_dictionary)


