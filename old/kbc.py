# from termcolor import colored
# print("          ....................................KAUN BANEGA CARORPATI................................\n")
# # first question..........................................................................
# print("FIRST QUESTIONFOR 10000\n")
# print(colored("QUESTION NO 1:-\nMS-Word is an example of ____\n""a) An operating system \t  b) A processing device \n  c) Application software \t  d) An input device \t", 'green'))
# answer = (input("enter answer->"))
# if (answer == 'a'):
#     print(colored("correct answer \n congrats you won 10000", 'blue'))
# else:
#     print(colored("wrong answer \n you loss", 'red'))
#     exit()
#     # second question..........................................................................
# print("SECOND QUESTIONFOR 20000\n")
# print(colored("QUESTION NO -2:-\nCtrl, Shift and Alt are called .......... keys\n a)modifier \tb)function \n c)alphanumeric\t  d)adjustment \n", 'green'))
# answer = (input("enter answer->"))
# if (answer == 'a'):
#     print(colored("correct answer \n congrats you won 20000", 'blue'))
# else:
#     print(colored("wrong answer \n you loss", 'red'))
#     exit()
#     # Third question..........................................................................
# print("THIRD QUESTIONFOR 100000\n")
# print(colored("QUESTION NO -3:-\nA computer cannot ""boot"" if it does not have the _____ \na)Compiler  \tb)Loader  \nc)Operating system  \td)Assembler\n", 'green'))
# answer = (input("enter answer->"))
# if (answer == 'c'):
#     print(colored("correct answer \n congrats you won 100000", 'blue'))
# else:
#     print(colored("wrong answer \n you loss", 'red'))
#     exit()
#     # Forth question..........................................................................
# print("FORTH QUESTIONFOR 200000\n")
# print(colored("QUESTION NO 4:-Microsoft Office is an example of a\n a)Closed source software \tb)Open source softwar  \nc)Horizontal market software  \td)vertical market software", 'green'))
# answer = (input("enter answer->"))
# if (answer == 'c'):
#     print(colored("correct answer \n congrats you won 200000", 'blue'))
# else:
#     print(colored("wrong answer \n you loss", 'red'))
#     exit()
# print("GREAT YOU WON \3\3\3\3\3\3\3\3")


st = int(input("enter how mwny question you want to put in numbers ->\n"))

for a in range(1, st+1):
    print("question no", a)
    c = (input("question->\n"))
    b = (input("A="))
    b = (input("B="))
    b = (input("C="))
    b = (input("D="))
    d = (input("enter answer in a,b,c,d \n"))

    print(c)
    print(b, "\n")
    qq = (input("enter answer"))
    if (qq == d):
        print("correct")
    else:
        print("in correct")
