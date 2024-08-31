print("\npython calculator :\npress q to exit \n")
while (1):
    exp = input(">>>")
    if (exp == "q"):
        exit(0)
    print(eval(exp))
