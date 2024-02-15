numberlist=[]
for num in range(10):
    numberlist.append(int(input("insert the "+ str(num+1) + " number")))

print(numberlist)

max=numberlist[0]
for numbers in numberlist:
    if numbers>max:
        max=numbers


print("The largest number is: "+ str(max))