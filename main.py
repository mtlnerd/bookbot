import sys

from stats import character_count, count_total_words, sort_characters


def get_book_text(file):
    with open(file) as f:
        contents = f.read()

    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_total_words(text)
    num_characters = character_count(text)
    character_counts = sort_characters(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in character_counts:
        if character["character"].isalpha():
            print(f"{character['character']}: {character['num']}")
    print("============= END ===============")


main()
