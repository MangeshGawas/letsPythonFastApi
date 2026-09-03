my_set = {1,23,5,2,13,2,44,5,2,17,8,5}
print(my_set)
print(len(my_set))

for i in my_set:
    print(i)

my_set.discard(3)
print(my_set)