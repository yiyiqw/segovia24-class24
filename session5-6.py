name = input("What is your name?")
age = input("How old are you?")
age = int(age)
birth_year = 2023 - age

print(f"OMG {name}, you are {age} years old so you were born in {birth_year}")
print("OMG", name, ", you are", age, "years old so you were born in ", birth_year)


age = int(input("What is your age?"))

age = input("How old are you?")
age = int(age)

print(f"Your age is {age}")


try:
    age =  int(input("What is your age?"))
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    print("Your age is", age)

try:
    age1 = int(input("What is your age player 1?"))
    age2 = int(input("What is your age player 2?"))
    res = age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("I am sorry, but you cannot divide by zero")
else:
    print("Player 1 is older than player 2 by a factor of", res)


import random
drinks = ("beer", "wine", "whiskey", "campari", "tequila", "rum", "gin tonic", "cakia")
try:
    age = int(input ("How old are you? "))
    country = input ("Where do you live? ")
except ValueError:\
    print("I am sorry, but that is not a valid number")
else:
    # Do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative, or greater than 130")
    elif age < 18:
        print ("I am sorry, too young to play this drinking game anywhere in the world")
    elif age < 21 and country == "US":
        print("I am sorry, too young to play this drinking game in the US")
    else:
        drink = random. choice(drinks)

