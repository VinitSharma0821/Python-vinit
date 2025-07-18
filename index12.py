while True:
    print("1, option 1")
    print("2, option 2")
    print("3, option 3")

    option = int(input("choose your option (1/2/3)"))

    if option == 1:
        print("Option 1 selected")
        for i in range (1,4):
            for j in range (1,i+1):
                print(i, end=" ")
            print()
    elif option == 2:
        print("Option 2 selected")
        for i in range (1,6):
            for j in range (1,i+1):
                print(i, end=" ")
            print()
    elif option == 3:
        print("Option 3 selected")
        for i in range(1,6):
            print(" " * (5-i), end="")
            print("* "*i)

    elif option == 4:
        print("Program exited!")
        break
    else:
        print("invalid number")
        break
