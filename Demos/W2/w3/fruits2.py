def get_fruits():
  fruits=[]
  print("How many fruits would you like to enter?")
  n=int(input())
  for i in range(n):
    print("Type in the next fruit:")
    fruits.append(input())
    #print all items
  print("Your fruits are {}".format(fruits))
#print only few items by SLICING
print(f"Sliced list:{fruits[0:5:2]}")
get_fruits()
#print only few items by using negative index
print (f"Negative index: {fruits[-1]})
get_fruits()

