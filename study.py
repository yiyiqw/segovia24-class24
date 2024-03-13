# Session 3-4

print("hello world again!")

print(5/5)

a = 5
b = 5
print(a, b, id(a), id(b))
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a, b, id(a), id(b))
print(a is b)

a.append(4)
print(a, b, id(a), id(b))
print(a is b)
print(a == b)

# SIEVE OF ERATOSTHENES
# Create a list of the first n numbers.
n = 100
x = list(range(2, n+1))

for i in x:
    j = 2
    while (i * j <= x[-1]):
        if (i * j in x):
            x.remove(i*j)
        j += 1

print("The list of prime numbers is:", x)

# EXERCISE 1
print(type(2))
print(type(2.3))
print((type(False)))
print(type(None))
print(type(4*2))
print(type(4/2))
print(type(3.0*1.0))
print(type(~3))
print(type(3|2))
print(type(3|2))
print(type("xx"))

# EXERCISE 2
print(5 + 2 - 9)
print(2 + 3 * 5)
print(--5)
print(None + 7)
print(not None)
print(4/2)
print(3.0*1.0)
print(2 ** 3 + 1)
print(2 ** (3 + 1.0))
print(2 < 3 < 1)
print(3 > 0 ** 0 * 4)
print(2 > 1 and 5)

# EXERCISE 3
a = 6
print(a + 2.0)
a /= 2
print(a)
b = 3
print(a**b)
b -= a
print(b + 2)
c = a > b
print(c and a)
print(a + b + c)

# Sessions 5-6
try:
    age1 = int(input("What is your age player 1? "))
    age2 = int(input("What is your age player 2? "))
    res = age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("I am sorry, but you cannot divide by 0")
except:
    print("I am sorry, but something went wrong")
else:
    print('Player 1 is older than player 2 by a factor of ', res)
finally:
    print("Thank you for playing")


# I want to print the multiplication table from 1 to 10.
for i in range(1, 11):
    for j in range(i, 11):
        print(i, "x", j, "=", i*j)
print()


import random
drinks = ["beer", "wine", "whiskey", "campari", "rum", "gin tonic", "rakia", "vodka", "martini", "sangria"]
try:
    age = int(input("How old are you? "))
    country = input("Where do you live? ")
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    # Do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative or greater than 130")
    elif age < 18:
        print("I am sorry, but you are too young to play this drinking game anywhere in the world.")
    elif age < 21 and country == "US":
        print("I am sorry, but you are too young to play this drinking game in the US.")
    else:
        drink = random.choice(drinks)
        print("Drink some", drink, ". Thank you for playing, you are", age, "years old so you can play this game in", country)

import random
lives = 3

while lives:
    print("You have", lives, "lives left")
    dice_roll = random.randint(1,6)
    if dice_roll == 6:
        print("You rolled a 6, you win!")
        break

    print("You rolled a", dice_roll, "try again")
    lives -= 1

else:
    print("You lost all your lives, game over.")


result = 0
for i in range(0,10):
    result += i
print("The sum of the first 9 numbers is", result)

result = 0
text = "1234567890"
for i in text:
    result += int(i)
print("The sum of the first 9 numbers is", result)

print(list(range(10)))
print(list(range(1, 11)))
print(list(range(0, 30, 5)))
print(list(range(0, 10, 3)))
print(list(range(0, -10, -1)))
print(list(range(0)))
print(list(range(1, 0)))


try:
    num = input("Give me a number:")
    num = int(num)
    print("The square of the number read is:", num*num)
except:
    print("Please give me a proper number.")

# Try/Except Syntax and Functionality
try:
    num = input("Give me a number:")
    num = int(num)
    num2 = input("Give me another number:")
    num2 = int(num2)
    result = num/num2

except ValueError:
    print("Please give me a proper number.")
except ZeroDivisionError:
    print("The second number cannot be zero.")
except:
    print("Some other exception I did not see coming.")
else:
    print("The division result is", result)


n = 1
result = 0

while n < 10:
    result += n
    n += 1
print("The sum of the first 9 numbers is", result)

# Infinite While Statements
while True:
    num = input("Give me a number (type quit to exit):")
    num2 = input("Give me another number(type quit to exit):")
    if num == "quit" or num2 == "quit":
        break
    num = int(num)
    num2 = int(num2)
    if num2 == 0:
        print("Cannot divide by zero")
        continue
    print("The division result of", num, "and", num2, "is", num/num2)


# Session 7-8
# Iterate over a string backward using while
text = "abcdefghijkl"
i = 0
while i < len(text):
    print(text[len(text)-1-i])
i += 1


def to_lowercase(input):
    return input.lower()

name = "Yiyi Qiu"
print(f"{to_lowercase(name)} thinks she's funny.")

template = "Today is %s"
print(template % "Tuesday")

# Tuple
template = "%s I have seen %d %s."
print(template % ("Today", 3, "dogs"))
print(template % ("On Monday", 7, "cats"))

base = "abcdefghijklmnopqrstuvwxyz"

print("here are some slices")
print(base[0:3])
print(base[0:5])
print(base[10:]) # From position 10 to the end.
print(base[:10]) # From the beginning to position 10 (excluding 10).
print(base[:]) # The whole string -> not really a slice.
print(base[::2]) # Every other letter.
print(base[5:15:3]) # Every third letter from the 5th to 15th.
print(base[::-1]) # The whole string backwards.


hi = "Hello world!"

# List Methods
print(dir(hi))

# Get a short description of a method.
print(help(hi.lower))

# Some more useful methods.
s = "hello world my name is John"
print(s.capitalize())
print(s.center(40))
print(s.count(" "))
print(s.replace(" ", "!!"))
print(s.split())

#CLASS EXAMPLE
text = "abcdefg"
print(dir(text))
help(text.isidentifier)
print(text.isidentifier()) # Is abcdefg a valid identifier?
print("1234".isidentifier()) # Is 1234 a valid identifier?
print("anananananananana".count("ana"))
print("anananananananana".replace("ana", "banana"))
print("anananananananana".find("ana", 1))
print("bbbabbbbbabbbbbabbabb".split("a"))
print("this is a sentence and i want the words".split(" "))
sentence = "Hello, kind-sir; how may! I be of service today?"
punctuation = ",-;?!"

# Sanitize the sentence.
for p in punctuation:
    sentence = sentence.replace(p, " ") # Replace the punctuation with nothing.
print(sentence)
sentence = sentence.replace("  ", " ") # Replace double spaces with single spaces.

# Split the sentence into words.
words = sentence.split(" ")
print(words)

text = "cat"
print(text.upper())
print(text)

name = "John"
second_name = "Bob"
print(f"Hi, {name} how are you? My name is {second_name}")
name = "Jane"
second_name = "Mary"
print(f"Hi, {name} how are you? My name is {second_name}")

# Indexing
hi = "Hello"
print(hi[1])
print(hi[-1])

# Addition
bye = "Bye"
print(hi+bye)
print(hi + " " + bye)

# Multiplication
print(3 * "abc")
bye = hi * 4
print(bye)

#Length
hi = "Hello!"
print(len(hi))

# For
str = "Hello world!"
print(str[1:3])
print(str[:4])
print(str[4:])
print(str[::3])
print(str[::-1])

# Comparison
hi = "banana"
print(hi == "banana")
print(hi == "Banana")
print(hi < "Banana")
print(hi > "bana")

# In
print("ba" in hi)
print("baN" in hi)


# Session 9-10

f = open("x-files.txt", "a")
while True:
    line = input("give me some text to put into the file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

# we need to close the file at the end
f.close()

f = open("x-files.txt", "a")
while True:
    line = input("give me some text to put into the file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

# we need to close the file at the end
f.close()


def sum_and_multiply(t1, t2, m):
    # addition number1
    # addition number2
    # multiplicator
    # prints (t1+t2)*m
    print((t1 + t2) * m)

sum_and_multiply(1, 2, 3)

def sum_and_multiply_different_params(t1, t2, m):
    print((t1 + t2) * m)

sum_and_multiply_different_params(t2=1, m=2, t1=3)


# Functions that return a value
def sum_and_multiply(t1, t2, m):
    # addition number1
    # addition number2
    # multiplicator
    # prints (t1+t2)*m
    return (t1 + t2) * m

result = sum_and_multiply(1, 2, 3)
print("(1+2)*3-4=", result - 4)

# Final words about functions
def introduce(name):
    # a regular string
    print("The name is:", name)

def bond(first_name="james", last_name="bond"):
    """
    Cool function
    :param first_name: first name, default "james"
    :param last_name: last name, default "bond"
    :return: returns the cool introduction
    """
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return last_name + "," + " " + first_name + " " + last_name

introduce(bond())

def greet():
    """
    This is a basic function used for teaching.
    It just prints 2 lines of text.
    :return: 7
    """
    print("Hello, World!")
    print("Bye World!")
    return 7


def operation_3_numbers(a, b, c=0):
    """
    This function sums 3 numbers.
    This is another explanation line.
    :param a: The first number.
    :param b: The second number.
    :param c: The third number.
    :return: The sum of these 3 numbers.
    """
    return a + b + c

def read_3_numbers():
    """
    This function reads 3 numbers from the user.
    :return: The 3 numbers.
    """
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    return a, b, c


# Another code:
# print("Now i will greet you!")
# a = greet()
# print("The function returned:", a)
# print("Done greeting")

# Another code:
# a = operation_3_numbers(10, 20, 40+3) # parameters taken by position.
# print(a)
# a = operation_3_numbers(c=10, a=20, b=43)
# print(a)
# a, b, c = read_3_numbers()
# print(operation_3_numbers(a, b, c))

print(operation_3_numbers(10, 20))

# To add elements to the list
t = ['a', 'b', 'c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

t = t.sort()
print(t)

# To delete elements from the list
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

t = ['a', 'b', 'c']
t.remove('b')
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

# Addition
a = [1, 2,3]
b = [4, 5, 6]
c = a + b
print(c)

# Multiplication
print([0]*4)
print([1, 2, 3]*3)

# Length
a = [1, 3, 5]*3
print(len(a))

# Iterate
for n in a:
    print(n)


# What is a list?
a = []
print(a)

a = [1, 3, 5, 2, 54]
print(a)

a = ["me", "myself", "eye"]
print(a)

a = ["me", 2+3, "hey"+"you", -4.2, None]
print(a)

# Lists are mutable.
lst = [1, 3, 5, 7, 9]
print(lst[1])
lst[1] = 11
print(lst)
lst[1] = lst[2]
print(lst)

# Lists can be sliced
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1:3])
print(list[:4])
print(list[4:])
print(list[::3])
print(list[::-1])

# min(), max(), len()
print(max('Hello world'))
print(min('Hello world'))
print(len('Hello world'))

# Conversion Functions: int(), float(), str()
print(int(3.2))
print(float(7))
print(str(3 + 6))

# Math Functions
import math
print(math.sin(30/360*2*math.pi))
print(math.sin(45/360*2*math.pi))
print(math.sqrt(2)/2)
print(help(math.sinh))
print(dir(math))

# Random Values
import random

for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))

ppl = ["Jon", "Ana", "Maria", "Jim", "Florence", "George", "James"]
print(random.choice(ppl))



