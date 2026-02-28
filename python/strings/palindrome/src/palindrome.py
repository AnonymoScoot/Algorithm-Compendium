
def is_palindrome(word):

    if type(word) is not str:
        return False

    word = word.lower()

    reversed = word[::-1]

    if word == reversed:
        return True
    return False
