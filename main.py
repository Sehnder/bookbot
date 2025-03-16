from stats import get_num_words, get_chars_dict, add_count_as_value
import sys





def main():
    ####Check for errors first
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    
    book_path = str(sys.argv[1])
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Pass chars_dict, not text
    sorted_chars = add_count_as_value(chars_dict)
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()