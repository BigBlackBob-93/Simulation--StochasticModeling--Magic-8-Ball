from random import randint
from objects import (
    answer_btn,
    result_l,
    question_le
)
from answers import get_answers


def reset():
    result_l.hide()


def start():
    if len(question_le.text()) > 0:
        answers = get_answers()
        alpha = randint(0, len(answers) - 1)
        result_l.setText(answers[alpha])
        result_l.show()


answer_btn.clicked.connect(start)
question_le.textChanged.connect(reset)
