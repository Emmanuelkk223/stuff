myList = ['mango', 5, 'banana', 8, 'pawpaw', 'water melon', 23, 5, 9, 'cashew', True, False]
myList.insert(2, 'apple')

price = []
fruit = []
Boolean = []

for i  in myList:
    if type(i) == int or type(i) == float:
        price.append(i)
    elif type(i) == bool:
        Boolean.append(i)
    else:
        fruit.append(i)

        
print(price)
print(fruit)
print(Boolean)
