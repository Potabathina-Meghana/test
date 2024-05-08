#using + operator
list1=[1,'f','p',5]
list2=[0,3,4,'o',8]
list_joined=list1+list2
print(list_joined)

#using iterable unpacking operator
list1=[1,2,3,'m']
list2=range(1,11)
list_joined=[*list1,*list2]
print(list_joined)

#with unique values
list1=[7,9,'g','pinky',0,9]
list2=['dude',7,6,0]
list_joined=list(set(list1+list2))
print(list_joined)


#using extend()
list1=[1,'i',8,'0',6]
list2=['maggi','n',9,2,0]
list2.extend(list1)
print(list2)