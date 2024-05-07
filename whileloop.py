#Print number from 1 to 10 using while loop
#if we keep end in the print statement then it will print in the same line or else it will print in the new line
i=1
while i <= 10:
    print(i, end=" ")
    #update
    i += 1

# print even numbers from 1 to 10
i=0
while i <=10:
    if i % 2 == 0:
        print(i, end=" ")
        #update
    i += 1
# print odd numbers from 1 to 100
i=0
while i<=100:
    if i%2!= 0:
        print(i, end="")
    i +=1
#print sum of numbers
i=0
add=0
while i <= 10:
    add +=i
    #print(add)
    i+=1
print(add)

