"""
Given a string, return whether it represents a number.

Here are the different kinds of numbers:

    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation

And here are examples of non-numbers:

    "a"
    "x 1"
    "a -2"
    "-"


NOTE: Unfinished...
"""

import re
from typing import Any, Dict, List, Set
import contextlib

TEST_CASES: List[Dict[Any]] = [
    {'input_string': "10", 'output': "positive integer"},
    {'input_string': "-10", 'output': "negative integer"},
    {'input_string': "10.1", 'output': "positive real number"},
    {'input_string': "-10.1", 'output': "negative real number"},
    {'input_string': "1e5", 'output': "number in scientific notation"},
    {'input_string': "a", 'output': "non-number"},
    {'input_string': "x 1", 'output': "non-number"},
    {'input_string': "a -2", 'output': "non-number"},
    {'input_string': "-", 'output': "non-number"},
]

OUTCOMES = [
    "positive integer", "negative integer", "positive real number",
    "negative real number", "number in scientific notation",
    "non-number",
]
VALID_CHAR_REGEX = r'[\de]'


def return_type(inp_str):
    MyNum = NumObj(inp_str)

    MyNum = _check_first_char(MyNum)
    if MyNum.ready_to_return:
        return MyNum.ready_to_return

    while not MyNum.ready_to_return:
        MyNum = _check_subsequent_chars(MyNum)
    
    return MyNum.ready_to_return


def _check_subsequent_chars()
    char = MyNum.pop()
    if char is None:
        return MyNum
    elif char == '.' and not 


def _check_first_char(MyNum):
    first_char = MyNum.pop()
    if first_char is None:
        MyNum.set_only_possible('non-number')
        return MyNum
    if first_char == '-':
        MyNum.set_impossible(['positive integer', 'positive real number'])
    elif re.match(VALID_CHAR_REGEX, first_char):
        MyNum.set_impossible(['negative integer', 'negative_real_number'])
    else:
        MyNum.set_only_possible('non-number')
    return MyNum


class NumObj():

    def __init__(self, inp_str):
        self.all_chars = list(inp_str)
        self.chars = list(inp_str)
        self.possible_outcomes: Set[str] = {key for key in OUTCOMES}
        self.decimal_flag = False

    def pop(self):
        try:
            return self.chars.pop()
        except Exception:
            return None

    def set_impossible(self, outcomes):
        if isinstance(outcomes, str):
            outcomes = [outcomes]
        for outcome in outcomes:
            try:
                self.possible_outcomes[outcome] = False
            except KeyError:
                print(f'outcome: {outcome} isn\'t in possible_outcomes')

    def set_only_possible(self, outcomes):
        if isinstance(outcomes, str):
            outcomes = [outcomes]
        self.set_impossible([oc for oc in OUTCOMES if oc not in outcomes])

    @property
    def ready_to_return(self):
        if len(self.possible_outcomes) != 1:
            return False
        elif len(self.possible_outcomes) == 1:
            return self.possible_outcomes[0]
        else:
            raise RuntimeError('something has gone wrong')


if __name__ == "__main__":
    for test_case in TEST_CASES:
        print(f'input of {test_case["input_string"]}')
        result = return_type(test_case['input_string'])
        print(result)
        if result == test_case['output']
            print('nice')
        else:
            print('bad')
