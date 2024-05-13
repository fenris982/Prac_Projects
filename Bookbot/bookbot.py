


def main():
    book_content = ''
    with open('G:\DOWNLOADS\python_projects\Bookbot\Frankenstein') as f:
        book_content = f.read()
    return book_content
        
def count_words(book):
    words = book.split()
    return len(words)

def char_count(words):
    lower_string = words.lower()
    char_dict = {}
    for char in lower_string:
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def sort_dict(char_dict):
    sorted_char_list = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_char_dicts = [{'char': char, 'count': count} for char, count in sorted_char_list if char.isalpha()]
    return sorted_char_dicts 
    

# book_content = main()
# # print("Number of words in Frankenstein book: ", count_words(book_content))
# # print("Number of each char in Frankenstein", char_count(book_content))
# print("The list of alphabetical characters in Frankenstein is: ", sort_dict(char_count))  


book_content = main()
word_count = count_words(book_content)
char_counts = char_count(book_content)
sorted_char_dicts = sort_dict(char_counts)

# print("Number of words in Frankenstein book:", word_count)
# print("Character counts in Frankenstein book:", sorted_char_dicts)

print("--- Begin report of books/frankenstein.txt ---")
print("{} words found in the document\n".format(word_count))

for char_info in sorted_char_dicts:
    print("The '{}' character was found {} times\n".format(char_info['char'], char_info['count']))
    