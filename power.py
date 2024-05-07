base=3
exponent=4
result=1
while exponent!=0:
     result*=base
     exponent-=1
print("Answer="+str(result))

#using the for loop
base=4
exponent=5
result=1
for exponent in range(exponent,0,-1):
     result*=base
    
print("Answer="+str(result))

#pow():Here we use this for calculating negative values.
base=3
exponent=-4
result=pow(base, exponent)
print("Answer="+str(result))