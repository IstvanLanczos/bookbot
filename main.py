
with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    words = file_contents.split()
    total_words = len(words)
    print(f'{total_words} words found in the document')

    char_count = {
    }
    for letter in file_contents:
        if letter.isalpha():
            if letter.lower() in char_count:
                char_count[letter.lower()] += 1
            else:
                char_count[letter.lower()] = 1
    order = []
    for char in char_count:

        if len(order) == 0:
            order.append(char)
        else:
            i = 0

            while i < len(order):
                if char_count[order[i]] > char_count[char]:
                    i += 1
                else:
                    order.insert(i, char)
                    break
                if i == len(order):
                    order.insert(i, char)
                    break

    for char in order:
        print(f"The '{char}' character was found {char_count[char]} times")
    print('--- End report ---')

