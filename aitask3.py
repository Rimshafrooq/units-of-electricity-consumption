# -*- coding: utf-8 -*-
"""aitask3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PmlK-Rf-Nuiq5vt5Ds9CyOROgz7tYy4o
"""

# Define the source matrix
electricity_matrix = [
    [80, 150, 250],
    [120, 180, 280],
    [200, 250, 350]
]

# Function to calculate and display cost for slab 1
def costSlab1():
    units_consumed = electricity_matrix[0][0]
    unit_cost = 10
    total_cost = units_consumed * unit_cost
    print(f"Bill for Slab 1: Rs. {total_cost}")

# Function to calculate and display cost for slab 2
def costSlab2():
    units_consumed = electricity_matrix[1][0]
    unit_cost = 15
    total_cost = units_consumed * unit_cost
    print(f"Bill for Slab 2: Rs. {total_cost}")

# Function to calculate and display cost for slab 3
def costSlab3():
    units_consumed = electricity_matrix[2][0]
    unit_cost = 20
    total_cost = units_consumed * unit_cost
    print(f"Bill for Slab 3: Rs. {total_cost}")

# Main menu loop
while True:
    student_id = input("Enter your student ID: ")
    print(f"Student ID: {student_id}")

    print("1. Display the bill of slab 1 and slab 2")
    print("2. Display the bill of slab 3")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        costSlab1()
        costSlab2()
    elif choice == '2':
        costSlab3()
    else:
        print("Exiting the program.")
        break

