# Program written for HAB Taxi Services by SD9 - Robot Group 7
# Written on : Aug 7 2023 - Aug

import math
import datetime

# Main program.
while True:
    print()
    print("        HAB Taxi Services")
    print("        Company Services System")
    print()
    print()
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Your report –add description here")
    print("9. Quit Program. ")

    while True:
        try:
            Choice = int(input("       Enter choice (1-9): "))
        except:
            print("Error - choice is not a valid entry.")
        else:
            if Choice < 1 or Choice > 9:
                print("Error - Choice must be between 1 and 9.")
            else:
                break
                


