#%%
contents = "ID|Name|Position|Salary|\n" 
contentslist = []
with open("Data.txt") as f:
        for line in f:
            contentslist = contentslist + line.rstrip().split("|")            
            contents = contents + line.rstrip() + "\n"
print (contents)
contentsdict = {}
x = 0
try:
    for item in contentslist:
        z = {contentslist[x+1]:[contentslist[x],contentslist[x+2],contentslist[x+3]]}
        contentsdict.update(z)
        x += 5
except(IndexError):
    pass

while True:
    Menu = input("1. New Staff\n2. Delete Staff\n3. View Summary Data\n4. Save and Exit\nInput Choice: ")        
    if Menu == "1":
        IDtemp = input("Input Staff ID: ")
        try:
            int(IDtemp[1:])
            if (IDtemp[0] != "S") or (len(IDtemp) != 5):
                print("Invalid ID")
                continue
            elif IDtemp in contentslist:
                print("Person already in list")
                continue
            else:
                ID = IDtemp
                nametemp = input("Input Staff Name: ")
            if len(nametemp) > 20:
                print("Name length too long.\nName must be below 20 characters.")
                continue
            else:
                name = nametemp
                positiontemp = input("Input Staff Position: ")
            if positiontemp.capitalize() == "Manager" or positiontemp.capitalize() == "Staff" or positiontemp.capitalize() == "Officer":
                position = positiontemp.capitalize()
                salarytemp = input("Input Staff Salary: ")
            else:
                print("Invalid position.\nPosition must either be Staff, Officer or Manager.")
                continue
            try:
                if position == "Staff" and (int(salarytemp) < 3500000 or int(salarytemp) > 7000000):
                            print("Invalid salary.\nStaff salary must be between 3500000 and 7000000.")
                            continue
                elif position == "Officer" and (int(salarytemp) < 7000001 or int(salarytemp) > 10000000):
                            print("Invalid salary.\nOfficer salary must be between 7000001 and 10000000.")
                            continue
                elif position == "Manager" and int(salarytemp) < 10000000:
                            print("Invalid salary.\nManager salary must be 10000000 or higher.")
                            continue
                else:
                    salary = salarytemp
                    newstaff = {name: [ID, position, salary]}
                    contentslist += [ID, name, position, salary, ""]
                    contentsdict.update(newstaff)
            except(ValueError):
                print("Salary must be a number without comas.")
                continue
                
        except(ValueError):
            print("Invalid ID")
            continue

    elif Menu == "2":
        IDtemp = input("Input Staff ID: ")
        try:
            int(IDtemp[1:])
            if (IDtemp[0] != "S") or (len(IDtemp) != 5):
                print("Invalid ID")
                continue
            elif IDtemp not in contentslist:
                print("ID not found.")
                continue
            else:
                contentslist.pop(contentslist.index(IDtemp)+1)
                contentslist.pop(contentslist.index(IDtemp)+1)
                contentslist.pop(contentslist.index(IDtemp)+1)
                contentslist.pop(contentslist.index(IDtemp)+1)
                contentslist.pop(contentslist.index(IDtemp))
                for key, List in contentsdict.items():
                    for value in List:
                        if value == IDtemp:
                            del contentsdict[key]
                print("Staff has been removed.")
        except(ValueError):
            print("Invalid ID")
            continue
    elif Menu == "3":
        numlistS = []
        numlistO = []
        numlistM = []
        templist = contentslist
        for value in templist:
            if value == "Staff":
                numlistS += [int(templist[templist.index(value)+1])]
                templist.pop(templist.index(value))
            elif value == "Officer":
                numlistO += [int(templist[templist.index(value)+1])]
                templist.pop(templist.index(value))
            elif value == "Manager":
                numlistM += [int(templist[templist.index(value)+1])]
                templist.pop(templist.index(value))
        print("\n1. Staff\nMinimum Salary: ", min(numlistS), "\nMaximum Salary: ", max(numlistS), "\nAverage Salary: ", int(sum(numlistS)/len(numlistS)))
        print("\n2. Officer\nMinimum Salary: ", min(numlistO), "\nMaximum Salary: ", max(numlistO), "\nAverage Salary: ", int(sum(numlistO)/len(numlistO)))
        print("\n3. Manager\nMinimum Salary: ", min(numlistM), "\nMaximum Salary: ", max(numlistM), "\nAverage Salary: ", int(sum(numlistM)/len(numlistM)))
    elif Menu == "4":
       newData = ""
       for key, List in sorted(contentsdict.items()):
           for content in List:
               try:
                   int(content[1:])
                   if content[0] == "S":
                       newData = newData + content + "|" + key + "|"
                   else:
                       newData = newData + content + "|\n"
               except(ValueError):
                   newData = newData + content + "|"
       with open("Data.txt", "w") as f:
            f.write(newData)
            break
    else:
        continue