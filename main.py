def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letters = characters(text)
    dict_list = list_convert(letters)
    report = output(dict_list, word_count)
 



def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def characters(text):
    characters = {}
    for character in text.lower():
        if character in characters:
            characters[character] += 1
        else: 
            characters[character] = 1
    return characters

def sort_on(dict_list):
    return dict_list["count"]

def list_convert(characters):
    dict_list = []
    for letter, count in characters.items():
        characters_dict ={'letter': letter, 'count': count}
        dict_list.append(characters_dict)
    return dict_list

def output(dict_list, word_count):
    dict_list.sort(reverse=True, key=sort_on)
    print(dict_list)
    print(f"{word_count} words found in the document")
    for item in dict_list:
        letter = item['letter']
        count = item['count']
        line = (f"The {letter} character was found {count} times")
        print(line)
    

main()