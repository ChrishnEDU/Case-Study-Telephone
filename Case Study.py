print("===================CASE STUDY (TELEPHONE)===================")
print("1. American | 2. Asian | 3. African | 4. European")
destination = int(input("\nSelect your Region Call Destination: "))
print("============================================================")
setday = input("\nIf you are calling in Day type |A| if Night type |B|: ")
print("============================================================")
day = input("\nType |X| for Weekdays and |Y| for Weekends: ")
print("============================================================")
time = int(input("\nHow many Minutes do you want to call?: "))

if day == "X" or "x":
    if setday == "A" or "a":
        if destination == 1:
            cost = time / 3 * 50
        elif destination == 2:
            cost = time / 2 * 30
        elif destination == 3:
            cost = time / 3 * 40
        elif destination == 4:
            cost = time / 2 * 35

    elif setday == "B" or "b":
        if destination == 1:
            cost = time / 3 * 45
        elif destination == 2:
            cost = time / 2 * 27
        elif destination == 3:
            cost = time / 3 * 36
        elif destination == 4:
            cost = time / 2 * 30

elif day == "Y" or "y":
    if setday == "A" or "a":
        if destination == 1:
            cost = (time/3) * 40
        elif destination == 2:
            cost = (time/2) * 25
        elif destination == 3:
            cost = (time/3) * 35
        elif destination == 4:
            cost = (time/2) * 20
        
    elif setday == "B" or "b":
        if destination == 1:
            cost = (time/3) * 38
        elif destination == 2:
            cost = (time/2) * 15
        elif destination == 3:
            cost = (time/3) * 22
        elif destination == 4:
            cost = (time/2) * 19

tot = "{:.2f}".format(cost)
print("Call Duration:",time,"minutes")
print("Call Total Cost:",tot,"pesos")
print("\n==================S U B M I T T E D  B Y====================")
print("==========L O P E Z, C H R I S T I A N   J O H N============")
print("========D E L O S  S A N T O S, M A R K  R O N I L==========")
