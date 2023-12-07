def main():
    book_path = "books/frankenstein.txt"

    get_report(book_path)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_count(text):
    text = text.lower()
    text = text.replace(" ", "")
    char_count = {}

    for letter in text:
        if letter.isalpha():
            if letter not in char_count:
                char_count[letter] = 1
            else:
                char_count[letter] += 1
    return dict(sorted(char_count.items()))

def get_report(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)

    print(f"\n--- Report for {book_path} ---\n")
    print(f"{num_words} words found in the document \n")

    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times.")

    print(f"\n--- End ---\n")

main()