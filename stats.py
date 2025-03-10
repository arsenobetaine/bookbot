def get_book_text(filepath):
    with open(filepath, 'r') as f:
        book_text = f.read()
    return book_text

def get_num_words(filepath):
    book_text = get_book_text(filepath)
    num_words = len(book_text.split())
    return num_words

def get_num_chars(filepath):
    book_text = get_book_text(filepath).lower()
    book_text = ''.join(char for char in book_text if char.isalpha())
    num_chars = {}
    for char in book_text:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    num_chars = dict(sorted(num_chars.items(), key=lambda item: item[1],reverse=True))
    return num_chars

