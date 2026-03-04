# Anagram

Create a program that checks if two strings are anagrams of each other.

A string is an anagram of another string if the characters in the first string can be rearranged to spell the second string.

For example, "listen" and "silent" are anagrams of each other because they contain exactly the same characters.

## Requirements

* Handle empty input gracefully
* Work correctly with both short and long strings
* Provide clear output messages
* Avoid using built-in anagram-checking utilities if your language provides them

## Suggested Approach

* Start by reading the two input strings
* Normalize the strings by making them consistent for comparison
* Compare the frequency of each character in the strings
* Use a loop or recursive logic to perform the comparison
* Store the result of the check in a variable before printing output

## Testing

Try your program with the following examples:

* Listen and Silent
* Acts and Cats
* Weird and Wired (depending on normalization rules)

## Extension Challenges

* Allow the program to ignore punctuation marks
* Support multiple lines of input
