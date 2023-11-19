def costSlab1(matrix):
    slab1_cost = sum(unit * 10 for unit in matrix[0] if unit <= 100)
    print(f"Total bill for slab 1: Rs. {slab1_cost}")

def costSlab2(matrix):
    slab2_cost = sum(unit * 15 for unit in matrix[1] if 100 < unit <= 200)
    print(f"Total bill for slab 2: Rs. {slab2_cost}")

def costSlab3(matrix):
    slab3_cost = sum(unit * 20 for unit in matrix[2] if 200 < unit <= 300)
    print(f"Total bill for slab 3: Rs. {slab3_cost}")

def display_menu(matrix, student_id):
    print(f"Student ID: {student_id}")
    print("1. Display bill of slab 1 and slab 2")
    print("2. Display bill of slab 3")
    print("Press any other key to exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            costSlab1(matrix)
            costSlab2(matrix)
        elif choice == '2':
            costSlab3(matrix)
        else:
            print("Exiting the program...")
            break

# Source data - 2D list
source_data = [
    [55, 65, 75],
    [120, 150, 170],
    [210, 230, 240]
]

student_id = "21MDBCS126"  # Replace this with the actual student ID

# Display menu and process choices
display_menu(source_data, student_id)
