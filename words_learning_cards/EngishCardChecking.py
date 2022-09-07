# using random.choice()
import random
import sys

VERSION = 'The current version is 2022042701'
HELP_INSTRUCTION = 'The redundant message is removed if z is selected'


def version_help():
    for x in sys.argv:
        if x == '-v' or x == '--version':
            print(VERSION)
        elif x == '-h' or x == '--help':
            print(HELP_INSTRACTION)


word_pairs = []
r2e = {}
english_words = []
russian_words = []
MAXIMAL_NUMBER = 2
valid_selection = True


def input_validating(checked_words, translation_words):
    while True:
        selected_number = 0
        try:
            row_input = input('Input Your selection here: ')
            if row_input == 'z':
                return row_input
            selected_number = int(row_input)
            print('Your choice: {}'.format(translation_words[selected_number]))
            selected_word = checked_words[selected_number]
        except (ValueError, ArithmeticError, IndexError):
            print('''
            It is not correct number.'
            Reenter please
            or type z for quit
            ''')
        else:
            break
    return selected_number


def sort_list_randomly(a, b):
    c = list(zip(a, b))
    random.shuffle(c)
    a, b = zip(*c)
    return a, b


def validating_selection(source, translation):
    c = 0
    random_source = ''
    selected_word = ''
    initial_selection = ''
    while random_source == selected_word:
        source_list, translation_list = sort_list_randomly(source, translation)
        if c > 0:
            print('Correct! \nTry the next one:')
            print('The previous selection is {}'.format(initial_selection))
        # select random word that is not equal to previous
        while True:
            random_source = random.choice(source_list)
            if random_source != initial_selection:
                break
        initial_selection = random_source
        c = c + 1
        # print('The previous selection is {}'.format(initial_selection)
        print('''
Select number that corresponds to
the correct translation of
{}
from list below or select z to quit
'''.format(random_source))
        for r in translation_list:
            print('{}: {}'.format(translation_list.index(r), r.rstrip("\n")))
        # checking input till it is valid
        selected_number = input_validating(source_list, translation_list)
        if selected_number != 'z':
            selected_word = source_list[selected_number]
        else:
            break
    if selected_number != 'z':
        print('Wrong. Your choice '
              'corresponds to word {}'.format(selected_word))
    return selected_word


def main():
    version_help()
    # print("Open file with Engish words")
    checked_file = open("words.txt", encoding='utf-8', mode='r')
    # create list of lines from file
    lines = checked_file.readlines()
    # closes file and clean the buffer
    checked_file.close()
    # Create list word_pairs
    # like [['english1', 'russian1'], ['english2', 'russian2']]
    for x in lines:
        # print(x.split(':'))
        word_pairs.append(x.split(':'))
    # print(word_pairs)
    # Create dictionary e2r
    e2r = dict(word_pairs)
    for key, value in e2r.items():
        # print('English: {}, is Russian: {}'.format(key, value))
        r2e[value] = key
        english_words.append(key)
        russian_words.append(value)
    ans = True
    while ans:
        print("""
        1.Check engish-russian translation
        2.Check russian-english translation
        3.Exit/Quit
        """)
        ans = input('Input Your choice here: ')
        if ans == "1":
            selection = validating_selection(english_words, russian_words)
        elif ans == "2":
            selection = validating_selection(russian_words, english_words)
        elif ans == "3":
            print("\n Goodbye")
            ans = None
        else:
            print("\n Not Valid Choice Try again")
    exit()


if __name__ == "__main__":
    main()
