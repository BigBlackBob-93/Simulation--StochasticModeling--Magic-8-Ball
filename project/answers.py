from random import shuffle
from constants import answers


def get_answers() -> list:
    shuffle(answers)
    return answers
