dicty = set()  # declare global variable dictionary


def read_dict():
    global dicty  # refrence global dict
    if dicty:
        return  # return if there are words in dicty

    with open("words.txt", "r") as f:  # open words.txt and set mode to read
        contents = f.read()  # move words in words.txt to contents

    dicty = set(
        word.lower()  # convert to lower case
        # converts the list of words into a python list containing the words
        for word in contents.splitlines()
    )  # hashes the contents


def is_this_spelled_right(word):
    # Return True if spelled correctly otherwise return false

    word = word.lower()  # converting word to lower case
    read_dict()
    return word in dicty
