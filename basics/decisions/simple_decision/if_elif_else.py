print("Which direction should I move the paint brush?")
direction=str(input())

if (direction == "up"):
 print("I am painting in the upward direction")
elif (direction == "down"):
 print("I am painting in the downward direction")
elif (direction == "left"):
 print("I am painting in the left direction")
elif (direction == "right"):
 print("I am painting in the right direction")
else:
 print("I don't recognise that direction. I'll just chill here for a bit")
