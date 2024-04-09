"""
Even numbers: 
"""
count=0
for number in range(2,100): # Here it will print upto 98
    if number%2==0:
        count+=1
        print(number)
print(f"We have {count} even numbers")

n=int(input("Enter the n:"))
for i in range(2,n+1): #Here it will print upto last value as we have given n+1
    print(i)