def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = count_letters(text)
    print("------Book Report of the Classic Frankenstein------\n")
    print(f"{num_words} words found in the document\n")
    for key, value in num_char.items():
        print(f'The letter {key} was found {value} times')


def get_num_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    test_lower = text.lower()
    characters = [char for char in test_lower]
    letters = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        'e': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    for c in characters:
        for v in letters:
            if c == v:
                letters[v] += 1
    return letters


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
