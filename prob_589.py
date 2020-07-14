"""Q 589:
    Alice wants to join her school's Probability Student Club.
    Membership dues are computed via one of two simple probabilistic games.

    The first game: roll a die repeatedly.
    Stop rolling once you get a five followed by a six.
    Your number of rolls is the amount you pay, in dollars.

    The second game: same, except that
    the stopping condition is a five followed by a five.

    Which of the two games should Alice elect to play?
    Does it even matter?
    Write a program to simulate the two games
    and calculate their expected value.

Assumptions:
    A roll of the die is a distinct probabilistic event, I.E.
        a single roll has no influence on other rolls
    The probabilities of the distinct outcomes of a dice roll
        are equal. prob(1) == prob(2) == ... == prob(6).
    random.random() is sufficiently random
    int(float) always rounds down
"""

import random
from typing import List, Tuple

N_SAMPLES = 100000


def roll_die(n_faces: int = 6):
    """return a single die roll of an n_faces die."""
    return int(random.random() * n_faces) + 1


def calculate_probabilities(
    sequences_of_note: Tuple[List[int]],
    n_samples: int
):
    """Given sequences to count and samples to try,
    return probabilities of simuated outcomes."""
    seq_len = len(sequences_of_note[0])
    if not all([
        len(seq) == seq_len for seq in sequences_of_note
    ]):
        raise RuntimeError(
            'sequences_of_note must all be the same length'
        )

    def handle_buffer(new_val, buffer, seq_len):
        buffer.pop(0)
        buffer.append(new_val)
        return buffer

    def get_key_name(seq_list):
        return ', '.join([str(x) for x in seq_list])

    def initialize_active_variables(sequences_of_note, seq_len):
        buffer = []
        for i in range(seq_len):
            buffer.append(roll_die())

        counts = {get_key_name(key): 0 for key in sequences_of_note}
        counts['the_rest'] = 0

        return buffer, counts

    buffer, counts = initialize_active_variables(sequences_of_note, seq_len)

    for i in range(seq_len, n_samples+1):
        buffer = handle_buffer(roll_die(), buffer, seq_len)
        if buffer in sequences_of_note:
            counts[get_key_name(buffer)] += 1
        else:
            counts['the_rest'] += 1

    return {key: (counts[key] / n_samples) for key in counts}


if __name__ == "__main__":
    print(calculate_probabilities(
        ([5, 5], [5, 6]),
        N_SAMPLES
    ))
