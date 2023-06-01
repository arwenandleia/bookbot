
def main():
    book_path="books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #words= text.split()
    #print(len(words))
    char_freq= get_str_frequency(text)
    dspl_char_freq(char_freq)

def dspl_char_freq(char_freq):
    new_list = list(char_freq.items())
    new_list.sort(key=lambda x:x[1],reverse=True,)
    for item in new_list:
        if item[0].isalpha():
            print(f"The {item[0]} Character was found {item[1]} times")
    


    

def get_str_frequency(input_text):
    lowered_text=input_text.lower()
    chars = {}
    for c in lowered_text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars



    

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()



