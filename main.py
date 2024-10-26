def main():
    book_path = "frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    charac_count = count_characters(text)
    filtrar = filtro(text)
    print(f"Word count: {word_count}")
    print(f"Character counts: {charac_count}")
    print(f"alphabet word counts: {filtrar}")
    #print(text)
    

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

def filtro(text):
    char_alfa = {}
    for c in text.lower():
        if c not in char_alfa and c.isalpha():
            char_alfa[c] = 1
        elif c.isalpha():
            char_alfa[c] = char_alfa[c] + 1

    return char_alfa

main()
