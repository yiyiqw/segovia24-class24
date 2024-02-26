a = 2
b = 3
c = "abc"
print(a, b, c)
print(a, b, c, sep=",")
a += 2
a == 5
print(a)
print(c*(a-b))
d = c.find("b")
print(d)
print(d and b)
print(d == True)
e = str(a) + str(b) + str(c) + str(d)
print(e)
print(e[1::2])
print(e+e[::-1])


def print_b_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()

            b_words = [word for word in words if len(word) == 3 and word[0].lower() == 'b']

            if b_words:
                print("3-letter words starting with 'b':")
                for word in b_words:
                    print(word)
            else:
                print("No 3-letter words starting with 'b' found in the file.")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_name = 'example.txt'  # Replace with the actual file name
print_b_words(file_name)


def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# Example usage:
result_1 = find_divisors(47)
result_2 = find_divisors(28)

print(f"Divisors of 47: {result_1}")
print(f"Divisors of 28: {result_2}")

def get_multiple_of_six():
    while True:
        try:
            number = int(input("Please enter a multiple of 6: "))
            if number % 6 == 0:
                return number
            else:
                print("Invalid input! Please enter a multiple of 6.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Example usage:
result = get_multiple_of_six()
print(f"You entered: {result}")


def calculate_net_salary(gross, children):
    try:
        gross = float(gross)
        children = int(children)

        if gross < 1000:
            tax_rate = 0.10
        elif gross < 2000:
            tax_rate = 0.12
        elif gross < 4000:
            tax_rate = 0.14
        else:
            tax_rate = 0.18

        if gross < 2000:
            tax_cut_per_child = 0.01
        else:
            tax_cut_per_child = 0.005

        income_tax = gross * tax_rate
        tax_cut = children * tax_cut_per_child * gross

        net_salary = gross - income_tax + tax_cut

        return net_salary

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")

# Example usage:
try:
    gross_salary = input("Enter gross salary: ")
    num_children = input("Enter the number of children: ")

    net_salary = calculate_net_salary(gross_salary, num_children)

    print(f"Net Salary: {net_salary:.2f}")

except KeyboardInterrupt:
    print("\nOperation aborted by the user.")
except Exception as e:
    print(f"An error occurred: {e}")

divisor = 3
for num in range(0, 12, 3):
    print(num/divisor)

for letter in 'Ahola':
    print(letter)

num = 0
while num <= 5:
    print(num)
    num += 2
print("Out")
print(num)

num = 0
count = 0
while num <= 19:
    if num % 3 == 0:
        count += 1
    num + 1

print("Numbers divisible by 3", count)


dir(hi)

from urllib.parse import urlparse

def is_valid_url(url):
    """
    Checks if the passed parameter is a valid URL by parsing it and verifying if it has a scheme and netloc.

    Args:
    - url (str): The string to be checked as a valid URL.

    Returns:
    - bool: True if the passed string is a valid URL, False otherwise.
    """
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme) and bool(parsed_url.netloc)


from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])  # Check if both scheme and netloc are present
    except ValueError:
        return False  # If there's a ValueError, the URL is not valid

# Example usage:
s = "http://google.com and then there could be http://yahoo.com"
urls = s.split()

for url in urls:
    print(f"{url}: {is_valid_url(url)}")
