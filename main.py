from stats import get_num_words, get_char_count, sort_char_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found " + str(get_num_words(text)) + " total words")
    print("--------- Character Count -------")
    char_count = get_char_count(text)
    sorted_char_count = sort_char_dict(char_count)
    for letter in sorted_char_count:
        print(letter["letter"] + ": " + str(letter["num"]))
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()