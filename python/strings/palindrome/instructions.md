# Palindrome

A palindrome is a sequence of characters that reads the same forward and backward, ignoring differences in case and sometimes ignoring spaces and punctuation depending on the specification.

## Problem Description

Create a program that asks the user to enter a text string and determines whether the input is a palindrome.

Your program should:

* Accept a single line of text from the user
* Normalize the text by making it consistent for comparison

  * You may convert letters to the same case
  * You may ignore spaces if the exercise specification requires it
* Compare the sequence of characters from both ends
* Display a message indicating whether the input is a palindrome

## Requirements

* Handle empty input gracefully
* Work correctly with both short and long strings
* Provide clear output messages
* Avoid using built-in palindrome-checking utilities if your language provides them

## Suggested Approach

* Start by reading the input string
* Prepare the string for comparison by applying normalization rules
* Compare characters symmetrically from the start and end of the string
* Use a loop or recursive logic to perform the comparison
* Store the result of the check in a variable before printing output

## Testing

Try your program with the following examples:

* Level
* Radar
* Hello
* A man a plan a canal Panama (depending on normalization rules)

## Extension Challenges

* Allow the program to ignore punctuation marks
* Support multiple lines of input
* Create a version that checks palindromes using recursion
* Measure and display the time complexity of your solution