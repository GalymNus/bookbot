import sys
from stats import get_book_text, get_words_num, count_unique_characters, sort_results


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        characters = count_unique_characters(book)
        sorted_characters = sort_results(characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {len(get_words_num(book))} total words")
        print("--------- Character Count -------")
        for char in sorted_characters:
            print(f"{char}: {sorted_characters[char]}")
        print("============= END ===============")


main()
