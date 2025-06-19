def get_num_words(file):
    num_words = file.split()
    return len(num_words)

def count_chars(words):
    counted_characters = {}
    for bukwa in words:
        bukwa2 = bukwa.lower()
        if bukwa2.isalpha():
            if (bukwa2 in counted_characters) == False:
                counted_characters[bukwa2] = 1
            else:
                counted_characters[bukwa2] += 1
    return counted_characters

def list_chars(dict):
    bukwa_list = []
    for bukwa in dict:
        count = dict[bukwa]
        dict2 = {}
        dict2["letter"] = bukwa
        dict2["count"] = count
        bukwa_list.append(dict2)
    return bukwa_list

def sort_chars(dict):
    return dict["count"]

