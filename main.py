from stats import get_nums_words, charater_count, sorted_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    with open(file) as f:
        contents = f.read()
        print("----------- Word Count ----------")
        num_words = get_nums_words(contents)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        counter = charater_count(contents)
        stats = sorted_counts(counter)
        for stat in stats:
            char = stat["char"]
            count = stat["num"]
            print(f"{char}: {count}")
        
        print("============= END ===============")



main()