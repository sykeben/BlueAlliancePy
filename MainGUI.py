import easygui as eg
import BlueAlliancePyLib as bapl
import requests as req

quitCall = False
null = None
bapl.api_key = "GJouaQ0y5drrhoMYJVZ42pbZGFGXtrMZPmAqaZBHBJblsKRsfM3Vf0q7raTnsXOl"

def ti(value):
    return str(bapl.teaminfo(teamNumber, value))

teamValid = False
while not teamValid:
    try:
        teamNumber = str(eg.integerbox("Enter a team number:", "BlueAlliancePyGUI - Startup Configuration", None, 1, 9999))
        if bapl.checkteam(teamNumber):
            teamValid = True
        else:
            if eg.indexbox("Invalid team number, team does not exist.", "BlueAlliancePyGUI - Error", choices=["OK", "Quit"]) == 1:
                quitCall = True
                quit(404)
    except req.ConnectionError:
        if eg.indexbox("Connection error.", "BlueAlliancePyGUI - Error", choices=["OK", "Quit"]) == 1:
            quitCall = True
            quit(520)

while not quitCall:
    mainChoice = eg.indexbox("Current team: "+teamNumber+"\nSelect an action . . .", "BlueAlliancePyGUI - Main Menu", choices=["Quit", "Select Team", "Get Data"])
    if mainChoice == 0:
        quitCall = True
    elif mainChoice == 1:
        teamValid = False
        while not teamValid:
            try:
                teamNumber = str(eg.integerbox("Enter a team number . . .", "BlueAlliancePyGUI - Startup Configuration", None, 1, 9999))
                if bapl.checkteam(teamNumber):
                    teamValid = True
                else:
                    if eg.indexbox("Invalid team number, team does not exist.", "BlueAlliancePyGUI - Error", choices=["OK", "Quit"]) == 1:
                        quitCall = True
                        quit(404)
            except req.ConnectionError:
                if eg.indexbox("Connection error.", "BlueAlliancePyGUI - Error", choices=["OK", "Quit"]) == 1:
                    quitCall = True
                    quit(520)
    elif mainChoice == 2:
        secondaryChoice = eg.indexbox("Get data for . . .", "BlueAlliancePyGUI - Get Data", choices=["Back", "General Info", "Contact Info"])
        if secondaryChoice == 1:
            eg.msgbox("This may take a while, please wait.", "BlueAlliancePyGUI - Get Data - Warning")
            infoString = "Team Number: {0}\nName: {1}\nNickname: {2}\nCity: {3}\nState/Providence: {4}\nCountry: {5}\nMotto: {6}".format(teamNumber, ti("name"), ti("nickname"), ti("city"), ti("state_prov"), ti("country"), ti("motto"))
            eg.msgbox(infoString, "BlueAlliancePyGUI - Get Data - General Info")
        elif secondaryChoice == 2:
            eg.msgbox("This may take a while, please wait.", "BlueAlliancePyGUI - Get Data - Warning")
            infoString = "Address: {0}\nLocation Name: {1}\nPostal Code: {2}\nWebsite: {3}".format(ti("address"), ti("location_name"), ti("postal_code"), ti("website"))
            eg.msgbox(infoString, "BlueAlliancePyGUI - Get Data - Contact Info")