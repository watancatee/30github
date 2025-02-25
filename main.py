print("Write a number")
a = int(input())
print("Is " + str(a) + " your number")
answer = input().lower()
if answer == "yes":
    print("Great!")
else:
    exit()
if a > 0:
    print("Your number is greater than 0! Congrats")