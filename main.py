from stats import get_word_count
from stats import count_characters
from stats import sort_most_frequent
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main(book):
    text = get_book_text(book)
    count = get_word_count(text)
    character_counts = count_characters(text)
    sorted_char_list = sort_most_frequent(character_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char in sorted_char_list:
        print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")
    pass

book = ""
try:
    book = sys.argv[1]
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(book)