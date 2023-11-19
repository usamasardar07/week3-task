# Creating 2 dimensional Matrix
matrix = [[55, 65, 75], [120, 150, 170], [210, 230, 240]]


def CostSlab1():
    s1bill = 10
    mul1 = s1bill * matrix[0][0]
    mul2 = s1bill * matrix[0][1]
    mul3 = s1bill * matrix[0][2]
    print("\nSlab 1 Bill is as follows;")
    print(str(mul1) + "\t" + str(mul2) + "\t" + str(mul3) + "\n")


def CostSlab2():
    s2bill = 15
    mul1 = s2bill * matrix[1][0]
    mul2 = s2bill * matrix[1][1]
    mul3 = s2bill * matrix[1][2]
    print("Slab 2 Bill is as follows;")
    print(str(mul1) + "\t" + str(mul2) + "\t" + str(mul3) + "\n")


def CostSlab3():
    s3bill = 20
    mul1 = s3bill * matrix[2][0]
    mul2 = s3bill * matrix[2][1]
    mul3 = s3bill * matrix[2][2]
    print("\nSlab 3 Bill is as follows;")
    print(str(mul1) + "\t" + str(mul2) + "\t" + str(mul3) + "\n")


def display():
    print("My Student ID is ABC101")
    print("Press 1 to display Slab 1 & 2 Bills")
    print("Press 2 to display Slab 3 Bills")
    print("Press any other key to Exit")
    choice = input("\nEnter your Choice : ")
    if choice == '1':
        CostSlab1()
        CostSlab2()
    elif choice == '2':
        CostSlab3()
    else:
        print("Wrong input key, Program terminated!")


display()
