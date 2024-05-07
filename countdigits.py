num=345256
count=0
while num!=0:
    num//=10
    count+=1
print("Number of digits:",str(count))

#inbuilt
num=123445677
print(len(str(num)))