# Midterm exam
import random
import datetime

# Question 1
print(2*3+5*6)

# Question 2
print(3+10**2/2)

# Question 3
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])  # Check if both scheme and netloc are present
    except ValueError:
        return False  # If there's a ValueError, the URL is not valid

# Example usage:
s = "http://google.com"
urls = s.split()

for url in urls:
    print(f"{url}: {is_valid_url(url)}")

# Question 4
import random

random_numbers = []

for _ in range(10):
    random_numbers.append(random.randint(1, 100))

# Replace numbers greater than 80 with their corresponding numbers
random_numbers = [num if num <= 80 else -90 for num in random_numbers]

# Print the final list
print(random_numbers)

# Question 5
import datetime

today = datetime.date.today()
start_of_year = datetime.date(today.year, 1, 1)
day_of_year = (today - start_of_year).days + 1

sun = 0
for i in range(day_of_year//10):
    sun += random.randint(1, day_of_year//7)

print(sun)

max_random_value = day_of_year // 7  # Maximum random value
max_value = max_random_value * (day_of_year // 10)  # Maximum sum of random values

# It prints the sum of the random values.
# The maximum possible value depends on consistently getting the maximum random value in each iteration,
# but the actual output may vary due to the randomness of the random.randint function.

# Question 6
def compare(first, second):
    if first == second:
        print(f"{first} = {second}")
    elif first > second:
        print(f"{first} is greater than {second}")
    elif first < second:
        print(f"{first} is smaller than {second}")

first = int(input("Input first number:"))
second = int(input("Input second number:"))
compare(first, second)

# Question 7
a = 6
a = a - 2
print(a*2)
a = a*2
print(a+1)
a = a//3

print(a)

# Question 8
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

numbers = [34567899838, 548729249578, 43829101003884, 478929889422]

for number in numbers:
    if palindrome(str(number)):
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")


# Question 9
# Strings are immutable. This means that you cannot change them. Trying to change will result in an error ('TypeError')
# A list is mutable because you can change the items inside the list after it was created
# This is because

# Lists are mutable
my_list = [1, 2, 3]
print("Original List:", my_list)

# Modifying the list
my_list[0] = 10
print("Modified List:", my_list)

# Original List: [1, 2, 3]
# Modified List: [10, 2, 3]

# Strings are immutable
my_string = "hello"
print("Original String:", my_string)

# Attempting to modify the string (will raise an error)
try:
    my_string[0] = 'H'
except TypeError as e:
    print(f"Error: {e}")

# Original String: hello
# Error: 'str' object does not support item assignment

# Question 10
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)  # Use string repetition to create "abcabcabcabc"
print(d)