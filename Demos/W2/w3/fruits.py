#Define an empty list
fruits = []

#Define a list with items

vegetables=["Carrot", "Peas"]

print(vegetables)

#add items to the list
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Tomatoe")
fruits.append("Banana")

print(fruits)

#remove an item from a list at the END of the list
fruits.remove("Banana")
print(fruits)


#remove item by index
del fruits[1]
print (fruits)

#insert a value NOT at the end
fruits.insert(1,"Pineapple")
print (fruits)

#access single element
print (fruits[0])