def main():
    path_to_book = "books/frankenstein.txt"
    print(f'---Starting report of {path_to_book}-----')
    book_text = get_text_from_book(path_to_book)
    no_of_words = count_words(book_text)
    #print(no_of_words)
    print(f'The Number of words is {no_of_words}')
    
    char_hist_dict = count_characters(book_text)
    display_character_freq(char_hist_dict)



def display_character_freq(char_dict):
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item:item[1], reverse=True))
    for indiv_char in sorted_char_dict:
        print(f'The {indiv_char} character was found {sorted_char_dict[indiv_char]} times')




def count_characters(input_text):
    character_histogram = {}
    lowered_input_text = input_text.lower()
    for indiv_char in lowered_input_text:

        if indiv_char in character_histogram:
            character_histogram[indiv_char] +=1
        elif indiv_char.isalpha():
            character_histogram[indiv_char] = 1
    return character_histogram



def get_text_from_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents


def count_words(input_text):
    words = input_text.split()
    return len(words)


if __name__ == "__main__":
    main()
