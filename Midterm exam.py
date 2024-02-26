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
