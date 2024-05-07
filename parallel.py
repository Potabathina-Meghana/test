list_1=[1,2,3,4,5]
list_2=['a','b','c','d','e']
for i,j in zip(list_1,list_2):
    print(i,j)

#using itertools
import itertools
list_1=[1,2,3,4]
#for short stopping
list_2=['a','b','c']
for i,j in zip(list_1,list_2):
    print(i,j)
print("\n")
#for long stopping

for i ,j in itertools.zip_longest(list_1,list_2):
    print(i,j)

    