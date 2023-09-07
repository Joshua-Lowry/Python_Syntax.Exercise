def word_print(list):
    """
    This function takes a list of words as the paremeter
    """
    for word in list:
        """
        This loops through the list of words
        """
        print(word.upper())
        """
        As each word is looped through in the list, it then prints them as fully uppercased.
        """

def e_word_print(list):
    for word in list:
        if word.startswith('h' or 'y'):
            print(word.upper())

