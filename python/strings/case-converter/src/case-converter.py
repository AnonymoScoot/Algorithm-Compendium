
from assertpy import *


def lowercase(string: str) -> str | None:

    if type(string) is not str:
        return None

    lowercase_string = []

    for char in string:
        match char:
            case "A":
                lowercase_string.append("a")
            case "B":
                lowercase_string.append("b")
            case "C":
                lowercase_string.append("c")
            case "D":
                lowercase_string.append("d")
            case "E":
                lowercase_string.append("e")
            case "F":
                lowercase_string.append("f")
            case "G":
                lowercase_string.append("g")
            case "H":
                lowercase_string.append("h")
            case "I":
                lowercase_string.append("i")
            case "J":
                lowercase_string.append("j")
            case "K":
                lowercase_string.append("k")
            case "L":
                lowercase_string.append("l")
            case "M":
                lowercase_string.append("m")
            case "N":
                lowercase_string.append("n")
            case "O":
                lowercase_string.append("o")
            case "P":
                lowercase_string.append("p")
            case "Q":
                lowercase_string.append("q")
            case "R":
                lowercase_string.append("r")
            case "S":
                lowercase_string.append("s")
            case "T":
                lowercase_string.append("t")
            case "U":
                lowercase_string.append("u")
            case "V":
                lowercase_string.append("v")
            case "W":
                lowercase_string.append("w")
            case "X":
                lowercase_string.append("x")
            case "Y":
                lowercase_string.append("y")
            case "Z":
                lowercase_string.append("z")
            case _:
                lowercase_string.append(char)

    return "".join(lowercase_string)


def uppercase(string: str) -> str | None:

    if type(string) is not str:
        return None

    uppercase_string = []

    for char in string:
        match char:
            case "a":
                uppercase_string.append("A")
            case "b":
                uppercase_string.append("B")
            case "c":
                uppercase_string.append("C")
            case "d":
                uppercase_string.append("D")
            case "e":
                uppercase_string.append("E")
            case "f":
                uppercase_string.append("F")
            case "g":
                uppercase_string.append("G")
            case "h":
                uppercase_string.append("H")
            case "i":
                uppercase_string.append("I")
            case "j":
                uppercase_string.append("J")
            case "k":
                uppercase_string.append("K")
            case "l":
                uppercase_string.append("L")
            case "m":
                uppercase_string.append("M")
            case "n":
                uppercase_string.append("N")
            case "o":
                uppercase_string.append("O")
            case "p":
                uppercase_string.append("P")
            case "q":
                uppercase_string.append("Q")
            case "r":
                uppercase_string.append("R")
            case "s":
                uppercase_string.append("S")
            case "t":
                uppercase_string.append("T")
            case "u":
                uppercase_string.append("U")
            case "v":
                uppercase_string.append("V")
            case "w":
                uppercase_string.append("W")
            case "x":
                uppercase_string.append("X")
            case "y":
                uppercase_string.append("Y")
            case "z":
                uppercase_string.append("Z")
            case _:
                uppercase_string.append(char)

    return "".join(uppercase_string)


def sentencecase(string: str) -> str | None:

    if type(string) is not str:
        return None

    return uppercase(string[0]) + lowercase(string[1:])


def inversecase(string: str) -> str | None:

    if type(string) is not str:
        return None

    inverted_string = []

    for char in string:
        match char:
            case char if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                inverted_string.append(lowercase(char))
            case char if char in "abcdefghijklmnopqrstuvwxyz":
                inverted_string.append(uppercase(char))
            case _:
                inverted_string.append(char)

    return "".join(inverted_string)


def capitalizedcase(string: str) -> str | None:

    if type(string) is not str:
        return None

    capitalized_string = [sentencecase(word) for word in string.split()]

    return " ".join(capitalized_string)


def alternatingcase(word: str, even_capitalization: bool) -> str | None:

    if type(word) is not str:
        return None

    alternate_string = []

    for word in word.split():
        if even_capitalization:
            alternate_string.append("".join([uppercase(char) if index % 2 == 0 else lowercase(
                char) for index, char in enumerate(word)]))
        else:
            alternate_string.append("".join([lowercase(char) if index % 2 == 0 else uppercase(
                char) for index, char in enumerate(word)]))

    return " ".join(alternate_string)



if __name__ == "__main__":
    assert_that(lowercase("A")).is_type_of(str)
    assert_that(lowercase("A")).is_equal_to("a")
    assert_that(lowercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                ).is_equal_to("abcdefghijklmnopqrstuvwxyz")

    assert_that(uppercase("a")).is_type_of(str)
    assert_that(uppercase("a")).is_equal_to("A")
    assert_that(uppercase("abcdefghijklmnopqrstuvwxyz")
                ).is_equal_to("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    assert_that(sentencecase("abcd")).is_type_of(str)
    assert_that(sentencecase("abcd")).is_equal_to("Abcd")

    assert_that(inversecase("Aa")).is_type_of(str)
    assert_that(inversecase("Aa")).is_equal_to("aA")
    assert_that(inversecase("AbCd")).is_equal_to("aBcD")
    assert_that(inversecase("")).is_equal_to("")

    assert_that(capitalizedcase("abcd efgh")).is_type_of(str)
    assert_that(capitalizedcase("abcd efgh")).is_equal_to("Abcd Efgh")

    assert_that(alternatingcase("abcd efgh", True)
                ).is_type_of(str)
    assert_that(alternatingcase("abcd efgh", True)
                ).is_equal_to("AbCd EfGh")
    assert_that(alternatingcase("abcd efgh", False)
                ).is_equal_to("aBcD eFgH")
