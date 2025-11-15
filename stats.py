def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents 
    
def get_num_words(book):
    b = get_book_text(book)
    word_count = b.split()
    return len(word_count)

def get_character_count(book):
    s = get_book_text(book).lower()
    ret_dict = dict()
    for c in s:
        if c in ret_dict:
            ret_dict[c] += 1
        else:
            ret_dict[c] = 1
    return(ret_dict)
