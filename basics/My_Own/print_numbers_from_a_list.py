#write a program that prints out all the elements of the list that are less than ''number''(this will be given by the user.
#Extras:
#Instead of printing the elements one by one, make a new list that has all the elements less than ''number'' from this list
# in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller
# than that number given by the user.
from typing import List, Any, Union

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Give me a number. I will tell you which numbers from the list are smaller than the number you gave me: "))

new_list: list[Union[int, Any]] = []

for i in a:
    if i < num:
        new_list.append(i)

print ("The following numbers from the list are smaller than the number you gave me:", new_list)