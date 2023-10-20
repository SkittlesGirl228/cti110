# Checking if I have enough expenses covered for my trip
# 09/07/2023
# CTI-110 P1HW2 - Travel Expense
# Your Name
#
########### pseudocode ###########
########### pseudocode ###########
########### pseudocode ###########
########### pseudocode ###########
########### pseudocode ###########
########### pseudocode ###########
########### pseudocode ###########
########### pseudocode ###########
########### pseudocode ###########
########### pseudocode ###########
########### pseudocode ###########
#

# Information
print("This tool will help calculate and displays travel expenses")
budget = float(input("Enter Budget:  "))
print()

destination = input("Enter your travel destination:  ")
print()

gas = float(input("How much do you think you will spend on gas?  "))
print()

hotel = float(input("Approximately, how much will you need for accomodation/hotel:  "))
print()

food = float(input("Last, how much do you need for food?  "))

# Summary of Expenses
expenses = gas + hotel + food
balance = budget - expenses

#Display results
print("n--------Travel Expenses---------n")
print("Location:", destination)
print("Initial Budget:", budget)
print("\nFuel:",gas)
print("Accomodation:",hotel)
print("Food:",food)
print("\nRemaining Balance:",balance)

print("\nTotal expenses:",expenses)
