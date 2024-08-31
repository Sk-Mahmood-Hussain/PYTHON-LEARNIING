
# """


from termcolor import colored
print("hello")
print(7*8)
print("hello\nworld")
"""
"""
a = "hussain"
b = complex(8, 6)
c = False
d = None
print(c + b)
print("the type of data is=", type(b))
print("the type of data is=", type(a))
print("the type of data is=", type(c))
print("the type of data is=", type(d))
print(22+3)
print(22-5)
print(3*4)
print(2**3)
"""
"""
print(" ........hear is your clculator.......\n")
an = float(input("an="))
az = float(input("az="))
print("enter 1 for addition\n enter 2 for substraction \n enter 3 for multiplication\n enter 4 for division")
enter_no = int(input("choose a digit from 1, 2 , 3, 4 , d\n"))
if enter_no == 1:
    print("the addition valu is: ",   az,  an+az)
elif enter_no == 2:
    print("the substraction valu is: ", an-az)
elif enter_no == 3:
    print("the multiplication valu is: ", an*az)
elif enter_no == 4:
    print("the division valu is: ", an/az)
else:
    print(" invaild input")

# print("the valu of ", an, "-", az, "=", an-az)
# print("the valu of ", an, "/", az, "=", an/az)
#  print("the valu of ", an, "*", az, "=", an*az)
"""

# day 1 learning string

"""
a = "!!!i am hussain!!!!!!!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip("!"))
print(a.replace("i am", "you are"))
print(a.split())
b = "i am eram"
print(b.capitalize())
c = "total words 12"
print(len(c))
print(len(c.center(19)))
print(c.center(19))
print(a.count('!'))
print(a.endswith('!'))
print(a.endswith('am', 4, 7))
print(a.startswith('am', 4, 7))
print(a.find('hussain'))
print(a.swapcase())
print(a.title())
"""
# DAY 2............ if else conditional ststement
# if else statement
"""
a = int(input("enter your age:-"))                          # if else
print("your age is:- ", a)                                  # if else elif
if (a >= 18):                                               # nested if else elif
    print("you are able to drive")
else:
    print("you are not able to drive")
    print("nikal pehle bada hoo ja")
"""
# if else elif
"""
num = int(input("enter the number"))
if (num < 0):
    print("the enter number is negative")
elif (num == 0):
    print("the number is zero")
elif (num == 999):
    print("it is a special numbar")
else:
    print("the number is positive")
"""
# nested if else elif
"""
value = int(input("enter the number"))
if (value < 20):
    print("the number is < than 20")
elif (value > 20):
    if (value > 22 and value < 29):
        print("the value is in between 22 to 29")
    else:
        print("the number is not in between 22 to 29")
else:
    print("the enter number is invalid")
"""
# DAY 3......... for loop
"""
for i in range(1, 11):
    for j in range(1, 11):
        num = i*j
        print(i, "*", j, "=", num)
        if (j == 10):
            print("\n")
            continue
"""
"""
a = input("enter your name")
for _ in range(10):
    print(a)
"""
"""
for a in range(1, 11):
    for b in range(1, 16):
        print(a, "*", b, "=", a*b)
        if (b == 10):
            print("\n")
            print("imp multiplication")
            continue
        if (b == 15):
            print("imp multiplication end")
            print("\n")
        continue
"""
"""
while (1):
    a = int(input("a="))
    if (a >= 90):
        print("gread A")
    else:
        if (a >= 80):
            print("gread B")
        else:
            if (a >= 70):
                print("gread C")
            else:
                if (a >= 60):
                    print("jus pass gread D")
                else:
                    print("try next time... FAIL")

# prg string................................................
while (1):
    a = (input("enter your pragrapg or line here ->\n"))
    count = (input("enter what youwant to know->\n "))
    print(a.count(count))


# MY PROJECT       ....................................KAUN BANEGA CARORPATI................................

print("          ....................................KAUN BANEGA CARORPATI................................\n")
# first question..........................................................................
print("FIRST QUESTIONFOR 10000\n")
print(colored("QUESTION NO 1:-\nMS-Word is an example of ____\n""a) An operating system \t  b) A processing device \n  c) Application software \t  d) An input device \t", 'green'))
answer = (input("enter answer->"))
if (answer == 'a'):
    print(colored("correct answer \n congrats you won 10000", 'blue'))
else:
    print(colored("wrong answer \n you loss", 'red'))
    exit()
    # second question..........................................................................
print("SECOND QUESTIONFOR 20000\n")
print(colored("QUESTION NO -2:-\nCtrl, Shift and Alt are called .......... keys\n a)modifier \tb)function \n c)alphanumeric\t  d)adjustment \n", 'green'))
answer = (input("enter answer->"))
if (answer == 'a'):
    print(colored("correct answer \n congrats you won 20000", 'blue'))
else:
    print(colored("wrong answer \n you loss", 'red'))
    exit()
    # Third question..........................................................................
print("THIRD QUESTIONFOR 100000\n")
print(colored("QUESTION NO -3:-\nA computer cannot ""boot"" if it does not have the _____ \na)Compiler  \tb)Loader  \nc)Operating system  \td)Assembler\n", 'green'))
answer = (input("enter answer->"))
if (answer == 'c'):
    print(colored("correct answer \n congrats you won 100000", 'blue'))
else:
    print(colored("wrong answer \n you loss", 'red'))
    exit()
    # Forth question..........................................................................
print("FORTH QUESTIONFOR 200000\n")
print(colored("QUESTION NO 4:-Microsoft Office is an example of a\n a)Closed source software \tb)Open source softwar  \nc)Horizontal market software  \td)vertical market software", 'green'))
answer = (input("enter answer->"))
if (answer == 'c'):
    print(colored("correct answer \n congrats you won 200000", 'blue'))
else:
    print(colored("wrong answer \n you loss", 'red'))
    exit()
print("GREAT YOU WON \3\3\3\3\3\3\3\3")
"""
# clloge program .......................................................................
# program NO 1..........................................................
"""
# WRITE A MENU DRIVEN PROGRAM TO CONVERT THE GIVEN TEMPREATURE FROM FHARENHEIT TO CELSIUS AND VICE VERSA DEPENDING UPON CHOICE
"""
"""
while 1:
    print("tempreature conversion menu")
    print("1. FHARENHIT TO CELSIUS")
    print("2. CELSIUS TO FHARENHIT")
    print("3. QUITE")
    answer = int(input("enter what you want 1, 2, 3...."))
    if answer == 1:
        farr = float(input("enter fharenhit--->"))
        rr = (farr - 32) * 5/9
        print(rr)
    elif answer == 2:
        calc = float(input("enter celsius.... "))
        zz = (calc * 9/5) + 35
        print(zz)
    else:
        exit()
"""
# PROGRAM NO 2...............................................................
"""
# WRITE A PROGRAM TO CALCULATE TOTAL MARKS ,PERCENTAGE AND GREAD OF A STUDENT .MARKS OBTAIN IN EACH OF THE THREE SUBJECTS ARE TO BE INPUT
# BY THE USER .ASSIGN GRADES ACCORDING
# TO THE FOLLOWING CRITERIA:
# GRADE A : PERCENTAGE >=80
# GRADE B : PERCENTAGE >=70AND <80
# GRADE C : PERCENTAGE >=60AND <70
# GRADE D : PERCENTAGE >=40AND <60
# GRADE E : PERCENTAGE <40
"""
"""
while 1:
    print("total marks ,%,and gread ........->")
    subject1 = float(input("enter the marks of subject 1->"))
    subject2 = float(input("enter the marks of subject 2->"))
    subject3 = float(input("enter the marks of subject 3->"))
    total_marks = subject1 + subject2 + subject3
    percentage = (total_marks / 300) * 100
    if percentage >= 80:
        grade = "A"
    elif 70 <= percentage < 80:
        grade = "B"
    elif 60 <= percentage < 70:
        grade = "C"
    elif 40 <= percentage < 60:
        grade = "D"
    else:
        grade = "E"

    print(f"grade {grade}")
    print(f"total marks {total_marks}")
    print(f"percenage {percentage: .2f}%")

# FSTRING..............................................................................................
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


def square(n):
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
print(square.__doc__)

# .....DAY 7.........................EXCEPTION.......HANDALING.................................................
print("here the new program")
name = input("enter the number")
try:
    for i in range(1, 11):
        print(f" {int (name) } * {int (i) } =  { int (name * i) } ")
except:
    print("sorry")
print("my name is hussain ")
print("hello")
