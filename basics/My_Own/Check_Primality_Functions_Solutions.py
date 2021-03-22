#Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.)
number = int(input("What is your number? "))
print("")

divisors = []

for i in range(1,(number)+1):
    if number % i == 0:
        divisors.append(i)
else:

    print("The divisors are:", divisors)
if len(divisors) < 3:
    print("Your number is prime.")