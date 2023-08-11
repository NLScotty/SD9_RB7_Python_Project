def expenseByID():
    # We take the user input
    invNum = input("Please enter the ID of the expense you would like a report on: ") 
    # Information retreived by reading Expense Records
    driverNum = ''
    invDate = ''
    itemID = []
    numItem = []
    totItemCost = []
    subTotal = []
    hst = []
    invTotal = []

    # Information retreived by looking up itemId on Pats Inventory
    itemDesc = []

    # We open the Expense Records, save all relevant date, then close it
    expenseFile = open("../DataFiles/ExpenseRecords.dat", 'r')
    for line in expenseFile:
        record = line.split(",")
        # print(record[0]+" "+invNum)
        if record[0] == invNum:
            driverNum = record[1].strip()
            itemID.append(record[2].strip())
            invDate = record[3].strip()
            numItem.append(record[4].strip())
            totItemCost.append(float(record[5]))
            subTotal.append(float(record[6]))
            hst.append(float(record[7]))
            invTotal.append(float(record[8]))
    expenseFile.close()
    # if no record found, end execution
    if(driverNum == ''):
        print("No Invoice with ID of "+ invNum +" can be found.")
        return
    # else, we continue
    else:
        print(driverNum, itemID, numItem)



expenseByID()