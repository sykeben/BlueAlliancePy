print("BlueAlliancePyGUI Console")
print("")


def logmsg(text):
    print("[MESSAGE] {0}".format(text))


def logerr(text):
    print("[~ERROR~] {0}".format(text))


def logwarn(text):
    print("[WARNING] {0}".format(text))

logmsg("Loading libraries . . .")
import easygui as eg
import BlueAlliancePyLib as bapl
import requests as req

logmsg("Setting variables . . .")
quitCall = False
null = None
bapl.api_key = "GJouaQ0y5drrhoMYJVZ42pbZGFGXtrMZPmAqaZBHBJblsKRsfM3Vf0q7raTnsXOl"


def ti(value):
    logmsg("Team info called for: {0} . . .".format(value))
    return str(bapl.teaminfo(teamNumber, value))


logmsg("Starting main loop . . .")
teamValid = False
while not teamValid:
    try:
        logmsg("Getting team number . . .")
        teamNumber = str(eg.integerbox("Enter a team number:", "BlueAlliancePyGUI - Startup Configuration", None, 1, 9999))
        logmsg("Checking team number . . .")
        if bapl.checkteam(teamNumber):
            logmsg("Team number OK.")
            teamValid = True
        else:
            logerr("Team number invalid.")
            if eg.indexbox("Invalid team number, team does not exist.", "BlueAlliancePyGUI - Error", choices=["OK", "Quit"]) == 1:
                quitCall = True
                quit(404)
    except req.ConnectionError:
        logerr("Connection error!")
        if eg.indexbox("Connection error.", "BlueAlliancePyGUI - Error", choices=["OK", "Quit"]) == 1:
            quitCall = True
            quit(520)

while not quitCall:
    logmsg("Getting main choice . . .")
    mainChoice = eg.indexbox("Current team: "+teamNumber+"\nSelect an action . . .", "BlueAlliancePyGUI - Main Menu", choices=["Quit", "Select Team", "Get Data"])
    if mainChoice == 0:
        quitCall = True
    elif mainChoice == 1:
        teamValid = False
        while not teamValid:
            try:
                logmsg("Getting team number . . .")
                teamNumber = str(eg.integerbox("Enter a team number . . .", "BlueAlliancePyGUI - Startup Configuration", None, 1, 9999))
                logmsg("Checking team number . . .")
                if bapl.checkteam(teamNumber):
                    logmsg("Team number OK.")
                    teamValid = True
                else:
                    if eg.indexbox("Invalid team number, team does not exist.", "BlueAlliancePyGUI - Error", choices=["OK", "Quit"]) == 1:
                        quitCall = True
                        quit(404)
            except req.ConnectionError:
                logerr("Connection error!")
                if eg.indexbox("Connection error.", "BlueAlliancePyGUI - Error", choices=["OK", "Quit"]) == 1:
                    quitCall = True
                    quit(520)
    elif mainChoice == 2:
        logmsg("Getting secondary choice . . .")
        secondaryChoice = eg.indexbox("Get data for . . .", "BlueAlliancePyGUI - Get Data", choices=["Back", "General Info", "Contact Info", "Parsed Name"])
        if secondaryChoice == 1:
            logmsg("Getting team data for: General Info . . .")
            eg.msgbox("This may take a while, please wait.", "BlueAlliancePyGUI - Get Data - Warning")
            infoString = "Team Number: {0}\nName: {1}\nNickname: {2}\nCity: {3}\nState/Providence: {4}\nCountry: {5}\nMotto: {6}".format(teamNumber, ti("name"), ti("nickname"), ti("city"), ti("state_prov"), ti("country"), ti("motto"))
            eg.msgbox(infoString, "BlueAlliancePyGUI - Get Data - General Info")
        elif secondaryChoice == 2:
            logmsg("Getting team data for: Contact Info . . .")
            eg.msgbox("This may take a while, please wait.", "BlueAlliancePyGUI - Get Data - Warning")
            infoString = "Address: {0}\nLocation Name: {1}\nPostal Code: {2}\nWebsite: {3}".format(ti("address"), ti("location_name"), ti("postal_code"), ti("website"))
            eg.msgbox(infoString, "BlueAlliancePyGUI - Get Data - Contact Info")
        elif secondaryChoice == 3:
            logmsg("Getting team data for: Parsed Name . . .")
            eg.msgbox("This may take a while, please wait.", "BlueAlliancePyGUI - Get Data - Warning")
            rawString = ti("name")
            logmsg("Parsing team data for: Parsed Name . . .")
            firstSplit = rawString.split("&")
            secondSplit = firstSplit[0].split("/")
            infoString = "TEAM " + teamNumber + ", " + firstSplit[1].upper() + ", Sponsered by:\n"
            n = -1
            for item in secondSplit:
                infoString = infoString + "- " + item
                n += 1
                if n < len(secondSplit):
                    infoString = infoString + "\n"
            eg.msgbox(infoString, "BlueAlliancePyGUI - Get Data - Parsed Name")

logwarn("Quitting!")