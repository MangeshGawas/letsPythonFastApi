my_list = [1,2,3,4,5,6]
for i in range(len(my_list)):
    print(my_list[i])

print("2nd logic")
for i in my_list:
    print(i)

#sum of list no

sum = 0
for i in my_list:
    sum +=i
    # print(sum)

print(sum)


#while loop

i = 0
while i<5:
    i +=1
    if i ==3:
        continue
    print(i)
    if i ==4:
        break
else:
    print("i is now larger or equal to 5")