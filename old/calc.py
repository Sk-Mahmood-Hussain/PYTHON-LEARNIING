print(" ........hear is your clculator.......\n")
an = int(input("an="))
az = int(input("az="))
print("enter 1 for addition\n enter 2 for substraction \n enter 3 for multiplication\n enter 4 for division")
enter_no = int(input("choos 1 charecter among 2 , 3, 4 , d\n"))
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
