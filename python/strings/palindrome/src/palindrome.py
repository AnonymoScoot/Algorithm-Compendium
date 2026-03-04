from assertpy import *


def is_palindrome(word: str):

    if type(word) is not str:
        return False

    word = word.lower()

    reversed = word[::-1]

    if word == reversed:
        return True
    return False


if __name__ == "__main__":
    assert_that(is_palindrome("a")).is_true()
    assert_that(is_palindrome("aa")).is_true()
    assert_that(is_palindrome("aba")).is_true()
    assert_that(is_palindrome("abba")).is_true()
    assert_that(is_palindrome("abcba")).is_true()
    assert_that(is_palindrome("ab")).is_false()
    assert_that(is_palindrome("abc")).is_false()
    assert_that(is_palindrome("abb")).is_false()
    assert_that(is_palindrome("A")).is_true()
    assert_that(is_palindrome("AA")).is_true()
    assert_that(is_palindrome("ABA")).is_true()
    assert_that(is_palindrome("ABBA")).is_true()
    assert_that(is_palindrome("ABCBA")).is_true()
    assert_that(is_palindrome("AB")).is_false()
    assert_that(is_palindrome("ABC")).is_false()
    assert_that(is_palindrome("ABB")).is_false()
    assert_that(is_palindrome("aA")).is_true()
    assert_that(is_palindrome("aBa")).is_true()
    assert_that(is_palindrome("aBA")).is_true()
    assert_that(is_palindrome("aBcBa")).is_true()
    assert_that(is_palindrome("aBCBa")).is_true()
    assert_that(is_palindrome("aBCBA")).is_true()
    assert_that(is_palindrome("aBCbA")).is_true()
