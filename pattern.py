#Pattern 1:

for i in range(5):  # Iterates over rows, i.e., 0, 1, 2, 3,4
    for j in range(5):  # Iterates over columns, i.e., 0, 1, 2, 3,4
        print("#", end=" ")  # Prints '#' without moving to a new line
    print()  # Moves to the next line after printing each row

#Pattern 2:

num=int(input())
# run for rows
for i in range(1, num+1):
    #run for columns
    for j in range(i):
        print("#", end =" ")
    #after printing row to go to next row
    print()

for i in range(1, 10):
    pass # to avoid syntax error

for i in range(1,11):
    if i == 6:
        continue # skipping the value
    print(i)

for i in range(1,11):
    if i == 7:
        break #stopping
    print(i)

i=0
while i<=10:
      if i==5:
          break
      print(i)
      i +=1
      
       