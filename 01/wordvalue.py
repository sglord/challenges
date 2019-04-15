from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    d = open(DICTIONARY, 'r')
    word_list = d.read().splitlines()
    return word_list
    pass


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for letter in word:
        l = letter.upper()
        value += LETTER_SCORES.get(l, 0)
    return value
    pass


def max_word_value(lst=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if lst == None:g
        lst = load_words()
    high_val = 0
    high_word = ''
    for word in lst:
        val = calc_word_value(word)
        if(val > high_val):
            high_val = val
            high_word = word
        else:
            continue
    return high_word
    pass


if __name__ == "__main__":
    pass  # run unittests to validates
TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
# max_word_value()
