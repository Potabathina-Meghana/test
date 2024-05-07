list_1=[1,6,8,4,3,9,8,0,4]
print(list(set(list_1)))


list_1=[3,0,4,8,3,9,8,9]
list_2=[1,0,2,6,3,8,3,9] #intersection
print(list(set(list_1)^(set(list_2))))

#first occurance
count=0
my_string="Meghana"
my_char="a"
for i in my_string:
    if i == my_char:
        count+=1
print(count)