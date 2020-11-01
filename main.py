def gettime():
    import datetime
    return datetime.datetime.now()


def lock(n):
    if (n == 1):
        k = int(input("enter 1 for exercise\nenter 2 for food\n"))
        if (k == 1):
            with open("garvit-exe.txt", "a")as ge:
                String = input("TYPE HERE\n")
                ge.write(str(gettime()) + " : " + String)
                print("SUCCESSFULLY WRITTEN")
        elif (k == 2):
            with open("garvit-food.txt", "a")as gf:
                String = input("TYPE HERE\n")
                gf.write(str(gettime()) + " : " + String)
                print("SUCCESSFULLY WRITTEN")
    if (n == 2):
        k = int(input("enter 1 for exercise\nenter 2 for food\n"))
        if (k == 1):
            with open("john-exe.txt", "a")as je:
                String = input("TYPE HERE\n")
                je.write(str(gettime()) + " : " + String)
                print("SUCCESSFULLY WRITTEN")
        elif (k == 2):
            with open("john-food.txt", "a")as jf:
                String = input("TYPE HERE\n")
                jf.write(str(gettime()) + " : " + String)
                print("SUCCESSFULLY WRITTEN")
    if (n == 3):
        k = int(input("enter 1 for exercise\nenter 2 for food\n"))
        if (k == 1):
            with open("roman-exe.txt", "a")as re:
                String = input("TYPE HERE\n")
                re.write(str(gettime()) + " : " + String)
                print("SUCCESSFULLY WRITTEN")
        elif (k == 2):
            with open("john-food.txt", "a")as rf:
                String = input("TYPE HERE\n")
                rf.write(str(gettime()) + " : " + String)
                print("SUCCESSFULLY WRITTEN")


def retrieve(n):
    if (n == 1):
        k = int(input("enter 1 for exercise\nenter 2 for food\n"))
        if (k == 1):
            with open("garvit-exe.txt", "rt")as ge:
                for i in ge:
                    print(i, end="")
        elif (k == 2):
            with open("garvit-food.txt", "rt")as gf:
                for i in gf:
                    print(i, end="")
    if (n == 2):
        k = int(input("enter 1 for exercise\nenter 2 for food\n"))
        if (k == 1):
            with open("john-exe.txt", "rt")as je:
                for i in je:
                    print(i, end="")
        elif (k == 2):
            with open("john-food.txt", "rt")as jf:
                for i in jf:
                    print(i, end="")
    if (n == 3):
        k = int(input("enter 1 for exercise\nenter 2 for food\n"))
        if (k == 1):
            with open("roman-exe.txt", "rt")as re:
                for i in re:
                    print(i, end="")
        elif (k == 2):
            with open("john-food.txt", "rt")as rf:
                for i in rf:
                    print(i, end="")

print("what you want to do")
print("1.log\n2.retrieve")
a = int(input())
if (a == 1):
    print("press 1 for garvit\npress 2 for john\npress 3 for roman")
    b = int(input())
    lock(b)
else:
    print("press 1 for garvit\npress 2 for john\npress 3 for roman")
    b = int(input())
    retrieve(b)
