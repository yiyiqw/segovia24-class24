# question 1
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a)

# question 2
print(2+3*6/2)

# question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

# question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

numbers = [7489617719749244646336564429479177169847, 5485839837501070045005400701057389385845, 8025833559061079503003059701609553385208, 6593036601359343374664733439531066303956]

for number in numbers:
    if palindrome(str(number)):
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")

# question 5
def find_pattern_occurrences(text):
    """
    Finds all occurrences of a pattern that starts with 'C', has any number of letters, and ends with 'jeb'.

    Args:
    - text (str): The text to search the pattern in.

    Returns:
    - int: The number of matches found in the text.
    """
    # Split the text into words
    words = text.split()
    # Initialize the count of matches
    count = 0
    # Iterate over each word in the text
    for word in words:
        # Check if the word starts with 'C' and ends with 'jeb'
        if word.startswith('C') and word.endswith('jeb'):
            count += 1
    return count


# Example usage:
text_to_search = "Conejeb is a pattern, Ctwojeb is another, but not Cjebend or startCjeb."
number_of_matches = find_pattern_occurrences(text_to_search)
print(f"Number of matches: {number_of_matches}")


# question 6
# Strings are immutable. This means that you cannot change them. Trying to change will result in an error ('TypeError')
# A list is mutable because you can change the items inside the list after it was created

# Lists are mutable
my_list = [1, 2, 3]
print("Original List:", my_list)

# Modifying the list
my_list[0] = 10
print("Modified List:", my_list)

# Original List: [1, 2, 3]
# Modified List: [10, 2, 3]

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Modify the second element
numbers[1] = 20  # This changes the second element from 2 to 20

# Add a new element
numbers.append(6)  # This adds a new element to the end of the list

# Remove an element
numbers.remove(3)  # This removes the number 3 from the list

# After the above operations, the list has been changed:
print(numbers)  # Output: [1, 20, 4, 5, 6]

# from this we can see how lists can be changed, which shows they are mutable

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

# Define a string
greeting = "Hello, world!"

# Try to change the first character
try:
    greeting[0] = "J"  # This will raise an error, as strings are immutable
except TypeError as e:
    print(e)  # Output: 'str' object does not support item assignment

# To change the string, you have to create a new one
greeting = "J" + greeting[1:]

# Now greeting is a new string object:
print(greeting)  # Output: "Jello, world!"



# question 7
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

modified_numbers = []
for number in random_numbers:
    if number % 2 == 0:
        modified_numbers.append(number * 2)

print(modified_numbers)

# question 8

def is_valid_url(url):
    """
    Checks if the passed parameter is a simplified valid URL.
    A valid URL starts with "http://" and does not contain spaces.

    Args:
    - url (str): The string to be checked as a valid URL.

    Returns:
    - bool: True if the passed string is a valid URL, False otherwise.
    """
    # Check if the URL starts with "http://"
    if not url.startswith("http://"):
        return False

    # Check if the URL contains any spaces
    if " " in url:
        return False

    return True

# Example URLs to check
url_to_check = "http://google.com"

# Call the function with the URL
if is_valid_url(url_to_check):
    print(f"The URL '{url_to_check}' is valid.")
else:
    print(f"The URL '{url_to_check}' is not valid.")


# question 9
def days_since_birthday():
    # Prompt the user to input their birthday in "DD-MM-YYYY" format
    birthday = input("Enter your birthday (DD-MM-YYYY): ")

    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))

    # Placeholder for the current year, assuming we can't dynamically fetch it
    current_year = 2024

    # Calculate the number of full years since the birth year
    full_years = current_year - year - 1

    # Initialize the count of leap years
    leap_years = 0

    # Count how many leap years in the range from the year after the birth year to last year
    for y in range(year + 1, current_year):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            leap_years += 1

    # Calculate the number of days: leap years have 366 days, others have 365
    total_days = leap_years * 366 + (full_years - leap_years) * 365

    return total_days

print(days_since_birthday())


def days_since_birthday(birthday):
    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))

    # Get the current year (we'll use a placeholder since we're not importing anything)
    # In practice, you would get the current year dynamically
    current_year = 2024  # Placeholder for the current year

    # Calculate the number of full years since the birth year
    full_years = current_year - year - 1

    # Initialize the count of leap years
    leap_years = 0

    # Count how many leap years in the range from the year after the birth year to last year
    for y in range(year + 1, current_year):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            leap_years += 1

    # Calculate the number of days: leap years have 366 days, others have 365
    total_days = leap_years * 366 + (full_years - leap_years) * 365

    return total_days


# Example usage
birthday = "01-01-2000"
print(days_since_birthday(birthday))
