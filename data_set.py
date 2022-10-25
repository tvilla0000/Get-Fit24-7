from asyncio.windows_events import NULL
from numpy import empty
from retry import retry
import pandas as pd

filepath_DLs = r'C:\Users\Get Fit 24 7\Desktop\ALL CLUB FILES\DL LIST.xlsx'
sheets = []

@retry((ValueError, TypeError, IndexError), tries=3, delay=0)
def addSheet():
    new_sheet = input("How many sheets are we working with in 'DL LIST'? \n")
    if new_sheet == '':
        print(f"Invalid input. You entered '{new_sheet}'. The program can not analyze the data if there is no data referenced. Please Enter the Number of Sheets To Analyze.")
        addSheet()
    elif int(new_sheet) < 1:
        print("Invalid Input. Need at Least One Sheet to analyze data. \n")
        addSheet()
    elif int(new_sheet) == 1:
        new_sheet = str(input("What Sheet are we working with in 'DL LIST'? \n"))
        sheets.append(new_sheet)
    elif int(new_sheet) > 1:
        while True:
            new_sheet = str(input("Enter Sheet name We are Working With. When You're Done enter 'done'  \n"))
            if new_sheet.lower() == 'done':
                break
            sheets.append(new_sheet)

    else:
        print("Invalid Input. Data Can Not be Analyzed. Please Enter the Number of Sheets to Analyze From 'DL LIST'.")
        addSheet()
   

def getDls():
    for s in sheets:
        data = pd.read_excel(filepath_DLs, sheet_name=s)
        df = pd.DataFrame(data, columns=["STATUS", "NAME", "AMOUNT", "PHONE NUMBER"])
        print(f' \n {s} \n \n {df}\n')
 

def getPending():
    for s in sheets:
        data = pd.read_excel(filepath_DLs, sheet_name=s)
        df = pd.DataFrame(data, columns=["STATUS", "NAME", "AMOUNT", "PHONE NUMBER"])
        df = df[df['STATUS'] == 'PENDING']
        print(f' \n {s} \n \n {df} \n')

def getCollections():
     for s in sheets:
        data = pd.read_excel(filepath_DLs, sheet_name=s)
        df = pd.DataFrame(data, columns=["STATUS", "NAME", "AMOUNT", "PHONE NUMBER"])
        df = df[df['STATUS'] == 'COLLECTIONS']
        print(f' \n {s} \n \n {df} \n')



def main():
    tasks = ['get dls', 'get collections', 'get pending']
    task = ''
    count = 0
    while task != 'quit':
        count += 1
        if count == 1:
            task = str(input("What Are You Working On Today? If You've Changed Your Mind enter 'quit' to cancel out! \n")).lower()
        elif count > 1:
            task = str(input("Anything Else You Need to Work On? If You're all wrapped up enter 'quit' to cancel out! \n")).lower()
        if task == 'quit':
            print("Have a Nice Day!")
            break
        if task in tasks:
            addSheet()
            if task == 'get dls':
                getDls()
                task = input(f"Here are the results for all DLs from sheets {sheets}. Would you like to do something else with the DLs? If you're all wrapped up enter 'quit'! \n").lower()
                if task == 'quit':
                    print("Have a Nice day!")
                    return
                elif task in tasks and task != 'get dls':
                    if task == 'get collections':
                        print(f"Here Are Your Results For Collections in sheet(s) {sheets} \n")
                        getCollections()
                        continue
                        
                    elif task == 'get pending':
                        print(f"Here Are Your Results For Pending Payments in sheet(s) {sheets}")
                        getPending()
                        continue

                    else:
                        print("Invalid input. Options are 'get collections', and 'get pending'. \n")
            elif task == 'get collections': 
                getCollections()
                print(f"Here Are Your Results For Collections in sheet(s) {sheets} \n")
                continue
            elif task == 'get pending':
                getPending()
                print(f"Here Are Your Results For Pending Payments in sheet(s) {sheets}")
        else:
            print("invalid input. Options are 'get dls', 'get collections', and 'get collections' or 'quit' to cancel out. \n")
            count -=1
            continue

main()
