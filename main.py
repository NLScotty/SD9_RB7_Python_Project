# Program written for HAB Taxi Services by SD9 - Robot Group 7
# Written on : Aug 7 2023 - Aug

import math
import datetime
import Utilities.option8 as option8
import Utilities.option1 as option1
import Utilities.option7 as option7

# Main program.

exitFlag = False
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
    print("8. Generate Expense Invoice by Expense ID")
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
                if Choice == 1:
                    option1.enterEmpl()
                elif Choice == 7:
                    option7.driverReport()
                elif Choice == 8:
                    option8.run()
                elif Choice == 9:
                    exitFlag=True
                break
                
    if exitFlag == True:
        break