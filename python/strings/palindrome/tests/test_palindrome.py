import unittest
from src.palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):

    def test_edgecases(self):
        self.assertTrue(is_palindrome(""))

        self.assertFalse(is_palindrome(5))

    def test_lowercase(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("aa"))
        self.assertTrue(is_palindrome("aba"))
        self.assertTrue(is_palindrome("abba"))
        self.assertTrue(is_palindrome("abcba"))

        self.assertFalse(is_palindrome("ab"))
        self.assertFalse(is_palindrome("abc"))
        self.assertFalse(is_palindrome("abb"))

    def test_uppercase(self):
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome("AA"))
        self.assertTrue(is_palindrome("ABA"))
        self.assertTrue(is_palindrome("ABBA"))
        self.assertTrue(is_palindrome("ABCBA"))

        self.assertFalse(is_palindrome("AB"))
        self.assertFalse(is_palindrome("ABC"))
        self.assertFalse(is_palindrome("ABB"))

    def test_mixcase(self):
        self.assertTrue(is_palindrome("aA"))
        self.assertTrue(is_palindrome("aBa"))
        self.assertTrue(is_palindrome("aBA"))
        self.assertTrue(is_palindrome("aBcBa"))
        self.assertTrue(is_palindrome("aBCBa"))
        self.assertTrue(is_palindrome("aBCBA"))
        self.assertTrue(is_palindrome("aBCbA"))


if __name__ == "__main__":
    unittest.main()
