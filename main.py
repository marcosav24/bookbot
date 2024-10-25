def main():
    book_path = "frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"Word count: {word_count}")
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

main()
