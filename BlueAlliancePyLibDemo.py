print("<<<<< BlueAlliancePyLib Demo >>>>>")
print("")

print("Importing the library . . . ", end='')
import BlueAlliancePyLib as bapl
print("Done.")

print("Setting variables . . . ", end='')
null = None
current = "main"
print("Done.")

print("Setting API key . . . ", end='')
bapl.api_key = "GJouaQ0y5drrhoMYJVZ42pbZGFGXtrMZPmAqaZBHBJblsKRsfM3Vf0q7raTnsXOl"
print("Done.")

while current != "quit":

    while current == "main":
        print("")
        print("----- Main Menu -----")
        print("[0] Quit")
        print("[1] Team Info Prompt")
        print("[2] Get Server Status")
        print("---------------------")
        choice = input("(0-2)>>> ")
        if choice == "0":
            current = "quit"
        elif choice == "1":
            current = "teaminfoprompt"
        elif choice == "2":
            current = "getserverstatus"
        else:
            print("Invalid choice, try again . . . ")

    if current == "teaminfoprompt":
        print("")
        print("----- TEAM INFO PROMPT -----")
        print("Run \"quit\" to go back.")
        print("Run \"help\" for a list of commands")
        print("----------------------------")
        goback = False
        teamnumber = "/NONE"
        while not (goback):
            if teamnumber == "/NONE":
                prompt = "(Team:NONE)>>> "
            else:
                prompt = "(Team:"+teamnumber+")>>> "
            command = input(prompt).lower()
            if command == "quit":
                goback = True
            elif command == "help":
                print(" COMMANDS:")
                print("  help -> Prints this list.")
                print("  teamnumber -> Sets the current team number.")
                print("  getinfo -> Gets a value, if the value is")
                print("             \"help\", it will print available")
                print("             values.")
            elif command == "teamnumber":
                choice = input(" Number? ")
                try:
                    teamnumber = str(int(choice))
                except TypeError:
                    print("Invalid team number.")
            elif command == "getinfo":
                choice = input(" Value? ")
                if choice == "help":
                    print("  VALUES:")
                    print("   name; nickname; city; state/prov;")
                    print("   country; address; website; motto;")
                    print("   rookie year; location name; [help]")
                elif choice == "name":
                    print("  "+str(bapl.teaminfo(teamnumber, "name")))
                elif choice == "nickname":
                    print("  "+str(bapl.teaminfo(teamnumber, "nickname")))
                elif choice == "city":
                    print("  "+str(bapl.teaminfo(teamnumber, "city")))
                elif choice == "state/prov":
                    print("  "+str(bapl.teaminfo(teamnumber, "state_prov")))
                elif choice == "country":
                    print("  "+str(bapl.teaminfo(teamnumber, "country")))
                elif choice == "address":
                    print("  "+str(bapl.teaminfo(teamnumber, "address")))
                elif choice == "website":
                    print("  "+str(bapl.teaminfo(teamnumber, "website")))
                elif choice == "motto":
                    print("  "+str(bapl.teaminfo(teamnumber, "motto")))
                elif choice == "rookie year":
                    print("  "+str(bapl.teaminfo(teamnumber, "rookie_year")))
                elif choice == "location name":
                    print("  "+str(bapl.teaminfo(teamnumber, "location_name")))
                else:
                    print("  Invalid value.")
            else:
                print(" Invalid command.")
        print("----------------------------")
        current = "main"

    if current == "getserverstatus":
        print("")
        print("----- SERVER STATUS GETTER -----")
        print("Current Season ..... "+str(bapl.getstatus("current_season")))
        print("Max Season ......... "+str(bapl.getstatus("max_season")))
        if bapl.getstatus("is_datafeed_down"):
            temp = "Down"
        else:
            temp = "Up"
        print("Datafeed Status .... "+temp)
        print("--------------------------------")
        input("Press [ENTER] to continue . . . ")
        print("--------------------------------")
        current = "main"

print("")
print("Exiting . . . ")