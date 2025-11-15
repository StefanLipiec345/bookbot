import sys
from stats import get_num_words
from stats import get_character_count


def main(book):
    count = get_num_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words.")
    print("--------- Character Count -------")

    ret_dict = get_character_count(book)
    
    for s in ret_dict:
        print(f"{s}: {ret_dict[s]}")
    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main (sys.argv[1])
