from assertpy import *


def anagram(word1, word2):

    if type(word1) is not str or type(word2) is not str:
        return False

    return sorted(word1) == sorted(word2)


if __name__ == "__main__":

    assert_that(anagram("listen", "silent")).is_true()
    assert_that(anagram("abcd", "dcba")).is_true()
    assert_that(anagram(5, 5)).is_false()
