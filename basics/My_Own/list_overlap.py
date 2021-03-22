#write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates).
a = [12, 12, 3, 5, 8, 90, 11, 44, 66, 8, 9, 34, 56,79,88]
b = [12, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,79]
c = []
for item in a and b:
    if item in c:
        pass
    else:
        c.append(item)
c.sort()
print("These are the numbers found in BOTH a AND b:", c)
