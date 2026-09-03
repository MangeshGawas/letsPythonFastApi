'''
String Assignment 
Ask the user how many days until their birthday
and print an approx number of weeks until their birthday

week is = 7days

decimals within the return is allowed
'''

days = input("how many days until your birthday")
print(type(days))

days = int(days)
print(round(days/7) ," week remaining")