import sys
from stats import get_num_words
from stats import count_chars
from stats import sort_chars
from stats import list_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents    

def print_report(book_path, word_count, letter_list):
    print(" ")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in letter_list:
        print(f"{letter["letter"]}: {letter["count"]}")
    print("============= END ===============")
    print(" ")

def main():
    err = "Usage: python3 main.py <path_to_book>"
    try:
        if sys.argv[1] == None:
            trigger = None
    except IndexError:
        print(err)
        sys.exit(1)
    try:
        if sys.argv[2] != None:
            print(err)
            sys.exit(1) 
    except IndexError:
        trigger = None
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    counted_chars = count_chars(text)
    listed_chars = list_chars(counted_chars)
    listed_chars.sort(reverse = True, key = sort_chars)
    print_report(book_path, word_count, listed_chars)

main()