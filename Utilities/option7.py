def driverReport():
    # Import libraries
    import datetime
    import Utilities.FormatValues as FV

    # Constants/defaults/calculations
    currDate = datetime.datetime.now()
    begDate = "2023-05-01"
    begDateDSP = datetime.datetime.strptime(begDate, "%Y-%m-%d")

    # Print headings
    print()
    print("HAB TAXI SERVICES")
    print()
    print("DRIVER FINANCIAL LISTING")
    print(f"From {FV.FDateM(begDateDSP)} to {FV.FDateM(currDate)}")
    print()
    print("DRIVER  TRANSACTION", " " *31, "TRANSACTION")
    print("ID      NUMBER       DATE          DESCRIPTION      AMOUNT        HST          TOTAL")
    print("=" * 86)

    # Initialize counters/accumulators
    totTransAcc = 0
    HSTAcc = 0
    totAcc = 0
    totTransCtr = 0
    totMonthCtr = 0
    totWeekCtr = 0
    totDailyCtr = 0

    # Open file
    f = open("DataFiles/RevenueRecords.dat", "r")

    # Loop to process from data from file
    for revenueRecordsline in f:
        revenueLine = revenueRecordsline.split(",")

        # Read files
        driverID = revenueLine[3].strip()
        transNum = revenueLine[0].strip()
        transDate = revenueLine[1].strip()
        transDate = datetime.datetime.strptime(transDate, "%d-%m-%Y")
        transDescrpt = revenueLine[2].strip()
        transAmount = float(revenueLine[4].strip())
        HST = float(revenueLine[5].strip())
        transTotal = float(revenueLine[6].strip())

        # Calculations for variables, counters and accumulators
        totTransAcc += transAmount
        HSTAcc += HST
        totAcc += transTotal
        totTransCtr += 1

        if transAmount == 300.00:
            totWeekCtr += 1
        elif transAmount == 175.00:
            totMonthCtr += 1
        else:
            totDailyCtr += 1

        # Print detail lines
        print(f"{driverID:<4s}    {transNum:<5s}     {FV.FDateS(transDate):<10s}   {transDescrpt:<17s}  {FV.FDollar2(transAmount):>9s}       {FV.FDollar2(HST):>7s}    {FV.FDollar2(transTotal):>9s}")

    # Close file
    f.close()

    # Print summary details and counters/accumulators
    print("=" * 86)
    print(" " * 48, f"{FV.FDollar2(totTransAcc):>10s}     {FV.FDollar2(HSTAcc):>9s}   {FV.FDollar2(totAcc):>10s}")
    print("=" * 86)
    print("Data Analytics:")
    print()
    print(f"Total transactions:        {totTransCtr:>3d}")
    print(f"Total Weekly Rentals:      {totWeekCtr:>3d}")
    print(f"Total Daily Rentals:       {totDailyCtr:>3d}")
    print(f"Total Monthly Stand Fees:  {totMonthCtr:>3d}")
    print()
    print()
    input("Press the Enter Key to Continue...")