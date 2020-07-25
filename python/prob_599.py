"""
UNFINISHED

Problem 599: Ghost

Ghost is a two-person word game where players alternate appending letters
to a word. The first person who spells out a word, or creates a prefix
for which there is no possible continuation, loses. Here is a sample game:

(player 1 loses, starts with 'G', 'H', 'O', 'S', 'T' (loss))

Given a dictionary of words, determine the letters the first player should
start with, such that with optimal play they cannot lose.

For example, if the dictionary is:
    ["cat", "calf", "dog", "bear"]
the only winning start letter would be 'b'.

NOTES:
    Okay no guarantees I can figure this one out. I guess these rules
    stipulate that the only valid 'words' are those that are found in the
    dictionary.
"""

TEST_CASES = [
    ["cat", "calf", "dog", "bear"],
]

if __name__ == "__main__":
    for word