"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""
def myFunction(firstname, lastname, age):
    my_dic = {
        "firstname":firstname,
        "lastname":lastname,
        "age":age
    }
    print(my_dic)

myFunction(firstname="Mangesh", lastname="Gawas", age=26)