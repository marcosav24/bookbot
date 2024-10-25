def main():
    book_path = "frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    charac_count = count_characters(text)
    print(f"Word count: {word_count}")
    print(f"Character counts: {charac_count}")
    print(text)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for i in text.lower():
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] = char_count[i] + 1
        
    return char_count
    
main()
