"""
You are given a set of synonyms, such as:

    (big, large), (eat, consume), ...
    
Using this set, determine if two sentences with the
same number of words are equivalent.

For example, the following two sentences are equivalent:

"He wants to eat food."
"He wants to consume food."
"""

TEST_CASES = [
    {
        'synonyms': (("big", "large", "chonky"), ("eat", "consume", "pizza")),
        'sentences': (
            "They want to eat big food.",
            "They want to consume large food.",
        )
    },
    {
        'synonyms': (("big", "large", "chonky"), ("eat", "consume", "pizza")),
        'sentences': (
            "They want to eat big food.",
            "They want to pizza chonky food.",
        )
    },
]


def are_equivalant(sents, syns):
    sentlist0, sentlist1 = sents[0].split(), sents[1].split()
    for word_idx in range(len(sentlist0)):
        if sentlist0[word_idx] != sentlist1[word_idx]:
            if not are_synonyms(sentlist0[word_idx], sentlist1[word_idx], syns):
                return False
    return True


def are_synonyms(word0, word1, syns):
    for tup in syns:
        for syn_word_idx in range(len(tup)):
            if tup[syn_word_idx] in [word0, word1]:
                syns_to_check = list(tup)
                syns_to_check.pop(syn_word_idx)
                check_word = [w for w in [word0, word1] if w != tup[syn_word_idx]][0]
                for check_syn in syns_to_check:
                    if check_syn == check_word:
                        return True
    return False


if __name__ == "__main__":
    for test_args in TEST_CASES:
        result = are_equivalant(test_args['sentences'], test_args['synonyms'])
        print(
            f"It is {result} that the sentences:\n\"{test_args['sentences'][0]}\"\n"
            f"and\n\"{test_args['sentences'][1]}\"\nare the same.\n"
        )
