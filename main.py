import sys
import stats

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book = sys.argv[1]

    num_words = stats.get_num_words(book)
    num_chars = stats.get_num_chars(book)
    print(
          '============ BOOKBOT ============',
          f'Analyzing book found at {book}...',
          '----------- Word Count ----------',
          f'Found {num_words} total words',
          '--------- Character Count -------',
          sep='\n'
         )

    for key, value in num_chars.items():
        print(f"{key}: {value}")

    print(
          '============= END ==============='
         )

if __name__ == "__main__":
    main()
