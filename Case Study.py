print("===================CASE STUDY (TELEPHONE)===================")
print("1. American | 2. Asian | 3. African | 4. European")
destination = int(input("\nSelect your Region Call Destination: "))
day = input("\nType |X| for Weekdays and |Y| for Weekends: ")
setday = input("\nIf you are calling in Day type |A| if Night type |B|: ")
time = int(input("\nHow many Minutes do you want to call?: "))

match destination:
    case 1:
        reg = "American Region"
        if day == "X" or day == "x":
            d = "Weekdays"
            if setday == "A" or setday == "a":
                st = "Day Time"
                cost = 50
                rate = 3
            elif setday == "B" or setday == "b":
                st = "Night Time"
                cost = 45
                rate = 3
            else:
                print("Wrong Time")
                exit()
        
        elif day == "Y" or day == "y":
            d = "Weekends"
            if setday == "A" or setday == "a":
                st = "Day Time"
                cost = 40
                rate = 3
            elif setday == "B" or setday == "b":
                st = "Night Time"
                cost = 38
                rate = 3
            else:
                print("Wrong Time")
                exit()
        
        else:
            print("Wrong Day")
            exit()
    case 2:
        reg = "Asian Region"
        if day == "X" or day == "x":
            d = "Weekdays"
            if setday == "A" or setday == "a":
                st = "Day Time"
                cost = 30
                rate = 2
            elif setday == "B" or setday == "b":
                st = "Night Time"
                cost = 27
                rate = 2
            else:
                print("Wrong Time")
                exit()
        
        elif day == "Y" or day == "y":
            d = "Weekends"
            if setday == "A" or setday == "a":
                st = "Day Time"
                cost = 25
                rate = 2
            elif setday == "B" or setday == "b":
                st = "Night Time"
                cost = 15
                rate = 2
            else:
                print("Wrong Time")
                exit()
        
        else:
            print("Wrong Day")
            exit()
    case 3:
        reg = "African Region"
        if day == "X" or day == "x":
            d = "Weekdays"
            if setday == "A" or setday == "a":
                st = "Day Time"
                cost = 40
                rate = 3
            elif setday == "B" or setday == "b":
                st = "Night Time"
                cost = 36
                rate = 3
            else:
                print("Wrong Time")
                exit()
        
        elif day == "Y" or day == "y":
            d = "Weekends"
            if setday == "A" or setday == "a":
                st = "Day Time"
                cost = 35
                rate = 3
            elif setday == "B" or setday == "b":
                st = "Night Time"
                cost = 22
                rate = 3
            else:
                print("Wrong Time")
                exit()
        
        else:
            print("Wrong Day")
            exit()
    case 4:
        reg = "European Region"
        if day == "X" or day == "x":
            d = "Weekdays"
            if setday == "A" or setday == "a":
                st = "Day Time"
                cost = 35
                rate = 2
            elif setday == "B" or setday == "b":
                st = "Night Time"
                cost = 30
                rate = 2
            else:
                print("Wrong Time")
                exit()
        
        elif day == "Y" or day == "y":
            d = "Weekends"
            if setday == "A" or setday == "a":
                st = "Day Time"
                cost = 20
                rate = 2
            elif setday == "B" or setday == "b":
                st = "Night Time"
                cost = 19
                rate = 2
            else:
                print("Wrong Time")
                exit()
        
        else:
            print("Wrong Day")
            exit()

    case default:
        print("Invalid Input!")
        exit()

pen = (time/rate) * cost
tot = "{:.2f}".format(pen)
print("============================================================")
print("Region Code:",reg)
print("Call Dated:",d)
print("Call Time:",st)
print("Call Duration:",time,"minutes")
print("Call Total Cost:",tot,"pesos")
print("\n==================S U B M I T T E D  B Y====================")
print("==========L O P E Z, C H R I S T I A N   J O H N============")
print("========D E L O S  S A N T O S, M A R K  R O N I L==========")
