# FSTRING..............................................................................................
from termcolor import colored
letter = "hii my name is{} and my country name is {} good bye"
name = "Hussain"
country = "INDIA"
print(letter.format(name, country))
print(f"hii my nme is{name} and my country name is {country} good bye")
a = "a.modifier"
b = "b.function"
c = "c.alphanumeric"
d = "d.adjustment"
print(
    f"QUESTION NO -2:-\nCtrl, Shift and Alt are called ...\n {a}\t{b}\n{c}\t{d}")
answer = (input("enter answer->"))
if (answer == 'a'):
    print(colored("correct answer \n congrats you won 20000", 'blue'))
else:
    print(colored("wrong answer \n you loss", 'red'))
    # DOCSTRING.....................................................................................

    """
# def square(n):
    # from termcolor import colored
# letter = "hii my name is{} and my country name is {} good bye"
# name = "Hussain"
# country = "INDIA"
# print(letter.format(name, country))
# print(f"hii my nme is{name} and my country name is {country} good bye")
# a = "a.modifier"
# b = "b.function"
# c = "c.alphanumeric"
# d = "d.adjustment"
# print(
#     f"QUESTION NO -2:-\nCtrl, Shift and Alt are called ...\n {a}\t{b}\n{c}\t{d}")
# answer = (input("enter answer->"))
# if (answer == 'a'):
#     print(colored("correct answer \n congrats you won 20000", 'blue'))
# else:
#     print(colored("wrong answer \n you loss", 'red'))



print(square.__doc__)
"""
