import re


class Character:
    """Support Character
    0123456789abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    def __init__(self):
        self.word = input("Enter your word: ")
        self.total_word = []
        if len(self.word) != 0:
            self.prepare_character()
        else:
            print("Your word is EMPTY!!!")

    def prepare_character(self):
        self.set_word = list(sorted(set(self.word.lower())))
        for char in self.set_word:
            self.total_word.append(self.convert_special_character(char))
        self.total_word = sorted(self.total_word)
        self.count_character()

    def count_character(self):
        for char in self.total_word:
            print("Letter '{letter}' in word is {count}.".format(letter=char,
                                                                 count=len(re.findall(char, self.word.lower()))))

    def convert_special_character(self, text):
        replacements = {
            "\\": "\\\\",
            "`": "\`",
            "*": "\*",
            "_": "\_",
            "{": "\{",
            "}": "\}",
            "[": "\[",
            "]": "\]",
            "(": "\(",
            ")": "\)",
            "+": "\+",
            "?": "\?",
            "|": "\|",
        }
        text = "".join([replacements.get(c, c) for c in text])
        return text


count_word = Character()
