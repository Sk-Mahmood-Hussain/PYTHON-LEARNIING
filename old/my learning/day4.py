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

# FUNCTION
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
                    """


def musk(a, b):
    ans = a+b*a-b
    print(ans)
    a = 30
    b = 40
    musk(a, b)
    if (a > b):
        print("A is greatest")
    else:
        print("B  is greatest ")
    c = 60
    d = 50
    musk(c, d)
    if (c > d):
        print("Cis greatest")
    else:
        print("d is greatest ")
