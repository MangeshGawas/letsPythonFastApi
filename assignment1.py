''' 
 - write a python code that can do the following:
 - you have 50Rs
 - you buy an ithem is 15Rs , that has a 3% tax 
 - using the print() Print how much moneyyou have left, after purchasing the item
'''

money = 50
item = 15
tax = 0.3

money_left = money- item-(item*tax)
print(money_left)