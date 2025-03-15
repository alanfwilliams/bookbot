def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    text = text.lower()
    text_list = text.split()
    letter_dict = {}
    for word in text_list:
        for letter in word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    return dict["num"]

def sort_char_dict(char_dict):
    dict_list = []
    for item in char_dict:
        dict_list.append({"letter": item, "num": char_dict[item]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list