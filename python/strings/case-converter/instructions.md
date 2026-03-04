# Case Converter

Create a program that contains a set of functions for converting strings to different cases.

The program should have the following functions:

* `uppercase(string)`: Converts a string to uppercase
* `lowercase(string)`: Converts a string to lowercase
* `sentencecase(string)`: Converts a string to sentence case
* `alternatingcase(string, even_capitalization)`: Converts a string to alternating case
* `capitalizedcase(string)`: Converts a string to capitalized case
* `inversecase(string)`: Converts a string to inverse case

## Requirements

* Handle empty input gracefully
* Work correctly with both short and long strings
* Provide clear output messages
* Avoid using built-in case-converting utilities if your language provides them

## Suggested Approach

* Start by reading the input string
* Normalize the string by making it consistent for comparison
* Compare the frequency of each character in the strings
* Use a loop or recursive logic to perform the comparison
* Store the result of the check in a variable before printing output

## Testing

Try your program with the following examples:

* "Hello World"
* "This is a test"
* "Python is awesome"
* "AbCd EfGh"
* "aBcD eFgH"

## Extension Challenges

* Allow the program to ignore punctuation marks
* Support multiple lines of input
* Create a version that checks case conversion using recursion
