def print_b_words(file_name):
    try:
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Split the content into words
            words = content.split()

            # Filter and print 3-letter words starting with 'b'
            b_words = [word for word in words if len(word) == 3 and word.lower().startswith('b')]
            for b_word in b_words:
                print(b_word)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
file_name = 'your_text_file.txt'
print_b_words(file_name)


def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# Example usage:
num = 12  # Replace 12 with the integer for which you want to find divisors
result = find_divisors(num)
print(f"The divisors of {num} are: {result}")


def get_multiple_of_six():
    while True:
        try:
            user_input = int(input("Enter a multiple of 6: "))
            if user_input % 6 == 0:
                return user_input
            else:
                print("Invalid input. Please enter a multiple of 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example usage:
result = get_multiple_of_six()
print(f"You entered a multiple of 6: {result}")

