def reverse_words(text):
    for i in text.split():
        print(f"'{i[::-1]}'", end=' ')

