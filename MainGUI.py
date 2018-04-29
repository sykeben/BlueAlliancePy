print("BlueAlliancePyGUI Console")
print("")


def logmsg(text):
    print("[MESSAGE] {0}".format(text))


def logerr(text):
    print("[~ERROR~] {0}".format(text))


def logwarn(text):
    print("[WARNING] {0}".format(text))


def lognewln():
    print("")


logmsg("Loading libraries . . .")
import easygui as eg
import BlueAlliancePyLib as bapl
import requests as req
import os
import webbrowser

logmsg("Setting variables . . .")
quitCall = False
null = None
checkOK = False
bapl.api_key = "GJouaQ0y5drrhoMYJVZ42pbZGFGXtrMZPmAqaZBHBJblsKRsfM3Vf0q7raTnsXOl"


while not checkOK:
    logmsg("Checking for server connectivity . . .")
    if bapl.checkserveronline():
        logmsg("SUCCESS!")
        checkOK = True
    else:
        logerr("FAILURE!")
        if eg.indexbox("Server check failed.", "BlueAlliancePyGUI - Error", choices=["Try again", "Quit"]) == 1:
            logwarn("Quitting!")
            quit(4040404)


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
    mainChoice = eg.indexbox("Current team: "+teamNumber+"\nSelect an action . . .", "BlueAlliancePyGUI - Main Menu", choices=["Quit", "Select Team", "Get Data", "Generate HTML"])
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
            try:
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
            except:
                logerr("Could not parse name, invalid format.")
                eg.msgbox("Could not parse name, invalid format.", "BlueAllianceGUI - Get Data - Error")
    elif mainChoice == 3:
        logmsg("Getting data . . .")
        eg.msgbox("This may take a while, please wait.", "BlueAlliancePyGUI - Get Data - Warning")
        parsedteaminfo = bapl.readjsondata("/team/frc{0}".format(teamNumber))
        logmsg("Generating HTML results . . .")
        logmsg("HTML Generating: Header . . .")
        html = ["<html>",
        "<head>",
        "<title>BlueAlliancePy Results</title>",
        "<link href=\"https://fonts.googleapis.com/css?family=Roboto\" rel=\"stylesheet\">",
        "<style>",
        "* {",
        "font-family: \'Roboto\', sans-serif;",
        "}",
        "</style>",
        "</head><body>",
        "<h1>BlueAlliancePy Results</h1>",
        "<p>These are the results generated by BlueAlliancePy.</p>"]
        logmsg("HTML Generating: Body . . .")
        html.append("<h2>General Information</h2>")
        html.append("<ul>")
        html.append("<li><b>Name:</b> "+str(parsedteaminfo["name"])+"</li>")
        html.append("<li><b>Nickname:</b> "+str(parsedteaminfo["nickname"])+"</li>")
        html.append("<li><b>Number:</b> "+str(parsedteaminfo["team_number"])+"</li>")
        html.append("<li><b>Rookie Year:</b> "+str(parsedteaminfo["rookie_year"])+"</li>")
        html.append("<li><b>Motto:</b> "+str(parsedteaminfo["motto"])+"</li>")
        html.append("<li><b>City:</b> "+str(parsedteaminfo["city"])+"</li>")
        html.append("<li><b>State/Providence:</b> "+str(parsedteaminfo["state_prov"])+"</li>")
        html.append("<li><b>Country:</b> "+str(parsedteaminfo["country"])+"</li>")
        html.append("</ul>")
        html.append("<h2>Contact Information</h2>")
        html.append("<ul>")
        html.append("<li><b>Website:</b> <a href=\""+str(parsedteaminfo["website"])+"\">"+str(parsedteaminfo["website"])+"</a></li>")
        html.append("<li><b>Address:</b> <a href=\""+str(parsedteaminfo["gmaps_url"])+"\">"+str(parsedteaminfo["address"])+"</a></li>")
        html.append("</ul>")
        logmsg("HTML Generating: Footer . . .")
        html.append("</body>")
        html.append("</html>")
        try:
            os.remove("results.html")
        except OSError:
            pass
        try:
            htmlfile = open("results.html", "w")
            for item in html:
                htmlfile.write("%s\n" % item)
            logmsg("Opening HTML file in browser . . . ")
            try:
                webbrowser.open("results.html")
            except webbrowser.Error:
                logerr("Encountered a browser control error.")
            except:
                logerr("Encountered some error.")
        except:
            logerr("An error occurred, now printing HTML data instead of viewing it from a file within your browser:")
            lognewln()
            logmsg("##### START OF HTML DATA #####")
            for item in html:
                logmsg(str(item))
            logmsg("##### END OF HTML DATA #####")
            lognewln()
        

logwarn("Quitting!")
