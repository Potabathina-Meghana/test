def name():
    return "Pinky","Sony"
#print the tuple with the returned values
print(name())
#print the individual terms
name_1,name_2=name()
print(name_1,name_2)

#using a dictionary
def name():
    n1="Maggi"
    n2="Teju"
    return{1:n1,2:n2}
names=name()
print(names)