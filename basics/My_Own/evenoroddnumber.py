#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides
# evenly into num, tell that to the user. If not, print a different appropriate message.
### the following code returns an error for some reason
#num = input("Enter a number: ")
#mod = num % 2
#if mod > 0:
#    print("You picked an odd number.")
#else:
#    print("You picked an even number.")

num=int(input("Give me a number to check:"))
check=int(input("Give me a number to divide by:"))

if num%4==0:
    print(num, "is a multiple of 4")
elif num%2==0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
if num%check==0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)