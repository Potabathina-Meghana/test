index=[1,2,3]
languages=['java','python','c']
dictionary=dict(zip(index,languages))
print(dictionary)

#using list comprehension
index=[0,1,2]
languages=['Python','C++','C#']
dictionary={k:v for k, v in zip(index,languages)}
print(dictionary)