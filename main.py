# Import helper functions from stats.py
import sys
from stats import get_num_words
from stats import counting_characters
from stats import sorted_characters

# Function to open a file and return its contents as a string
def get_book_text(path_to_file):
    # "with open" ensures the file is properly closed after reading
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()  # Read the entire file into a string

def main():
    # check if user provided a book path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # exit with error code 1
    
    # STEP 1: Read the book text from file
    # sys.argv[1] is the path to the book
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    
    # STEP 2: Count the number of words
    num_words = get_num_words(text)

    # STEP 3: Count characters (returns a dictionary like {'a': 100, 'b': 50, ...})
    characters = counting_characters(text)

    # STEP 4: Sort the characters by frequency (returns a list of dicts)
    # Example: [{'char': 'e', 'num': 44538}, {'char': 't', 'num': 29493}, ...]
    sorted_chars = sorted_characters(characters)

    # STEP 5: Print a formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Loop through sorted characters and print each one
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============ END ============")

# This ensures main() only runs if this file is executed directly
if __name__ == "__main__":
    main()
