###############################
# BLUEALLIANCEPY KIOSK SCRIPT #
###############################

# <<< INTRO >>>
print("BlueAlliancePy Kiosk Console")
print("(C)2018 - Ben Sykes")
print("")

# <<< SET VARIABLES >>>
print("Setting variables . . . ", end='')
importsuccess = True
keyvalid = True
null = None
teamvalid = False
print("Done.")
print("")

# <<< FORMAT HTML HEADER >>>
print("Starting HTML . . . ", end='')
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
print("Done.")

# <<< IMPORT LIBRARIES AND MODULES >>>
print("Importing libraries and modules:")

print("- Time . . . ", end='')
try:
    import time
    print("Done.")
except ImportError:
    print("An error occurred.")
    importsuccess = False
except ImportWarning:
    print("Done, but a warning was issued.")

print("- Web Browser . . . ", end='')
try:
    import webbrowser
    print("Done.")
except ImportError:
    print("An error occurred.")
    importsuccess = False
except ImportWarning:
    print("Done, but a warning was issued.")

print("- Requests . . . ", end='')
try:
    import requests
    print("Done.")
except ImportError:
    print("An error occurred.")
    importsuccess = False
except ImportWarning:
    print("Done, but a warning was issued.")

print("- JSON . . . ", end='')
try:
    import json
    print("Done.")
except ImportError:
    print("An error occurred.")
    importsuccess = False
except ImportWarning:
    print("Done, but a warning was issued.")

print("- OS . . . ", end='')
try:
    import os
    print("Done.")
except ImportError:
    print("An error occurred.")
    importsuccess = False
except ImportWarning:
    print("Done, but a warning was issued.")

print("- Random . . . ", end='')
try:
    import random
    print("Done.")
except ImportError:
    print("An error occurred.")
    importsuccess = False
except ImportWarning:
    print("Done, but a warning was issued.")

print("- Sleep (From: Time) . . . ", end='')
try:
    from time import sleep
    print("Done.")
except ImportError:
    print("An error occurred.")
    importsuccess = False
except ImportWarning:
    print("Done, but a warning was issued.")

if not(importsuccess):
    print("Some errors occurred, the application may not work properly.")
print("")

# <<< AUTO CONFIGURATION >>>
print("Auto-configuring what can be auto-configured . . . ", end='')
apikey = "GJouaQ0y5drrhoMYJVZ42pbZGFGXtrMZPmAqaZBHBJblsKRsfM3Vf0q7raTnsXOl"
baseurl = "https://www.thebluealliance.com/api/v3"
urlparameters = "?X-TBA-Auth-Key="+apikey
print("Done.")

# << API KEY TEST >>>
print("Testing API Key . . . ", end='')
testrequest = requests.get(baseurl+"/status"+urlparameters)
if testrequest.status_code == 200:
    print("Successful.")
elif testrequest.status_code == 300:
    print("Successful, but nothing has been modified since.")
elif testrequest.status_code == 401:
    print("Unsuccessful, the key is invalid.")
    keyvalid = False
elif testrequest.status_code == 404:
    print("Unsuccessful, The server cannot be found.")
    quit(404)
else:
    print("Recieved a weird code: "+str(teaminforequest.status_code))
print("")

# <<< USER CONFIGURATION >>>
print("Please input the following information:")
teamnumber = input("Team # (R for random) ......... ")
if not(keyvalid):
    apikey = input("API Key ....................... ")
    keyvalid = True
print("")

# <<< GET ALL TEAM INFO >>>
openedalready = False
if teamnumber.lower() != "r":
    randomteam = False
    while not(teamvalid):
        print("Gathering all team information . . . ", end='')
        teaminforequest = requests.get(baseurl+"/team/frc"+teamnumber+urlparameters)
        if teaminforequest.status_code == 200:
            print("Successful.")
            teamvalid = True
        elif teaminforequest.status_code == 300:
            print("Successful, but nothing has been modified since.")
            teamvalid = True
        elif teaminforequest.status_code == 401:
            print("Unsuccessful, the API key is invalid.")
            print("Quitting . . . ")
            quit(401)
        elif teaminforequest.status_code == 404:
            print("Unsuccessful, The page cannot be found.")
            print("That team may not exist.")
            print("")
            print("Input a different team number ...... ", end='')
            teamnumber = input("")
            print("")
        else:
            print("Received a weird code: "+str(teaminforequest.status_code))
            print("The program may be unstable now.")
    print("")
    print("Parsing team information . . . ", end='')
    parsedteaminfo = json.loads(teaminforequest.text)
    print("Done.")
else:
    randomteam = True

while True:
    # <<< RESET HTML >>>
    print("Resetting HTML data . . . ", end='')
    html = ["<html>",
            "<head>",
            "<title>BlueAlliancePy Results</title>",
            "<meta http-equiv=\"refresh\" content=\"5\" >",
            "<link href=\"https://fonts.googleapis.com/css?family=Roboto\" rel=\"stylesheet\">",
            "<style>",
            "* {",
            "font-family: \'Roboto\', sans-serif;",
            "}",
            "</style>",
            "</head><body>",
            "<h1>BlueAlliancePy Results</h1>",
            "<p>These are the results generated by BlueAlliancePy.</p>"]
    print("Done.")
    # <<< GET AND PARSE DATA >>>
    if randomteam:
        randomteamok = False
        teamnumber = str(random.randint(1, 7000))
        while not(randomteamok):
            print("Gathering all team information . . . ", end='')
            teaminforequest = requests.get(baseurl+"/team/frc"+teamnumber+urlparameters)
            print("Done.")
            if teaminforequest.status_code == 200:
                randomteamok = True
                print("Parsing team information for team " + teamnumber + " . . . ", end='')
                parsedteaminfo = json.loads(teaminforequest.text)
                print("Done.")
            else:
                print("Invalid random number, trying again . . .")
                sleep(0.1)
    else:
        print("Gathering all team information . . . ", end='')
        teaminforequest = requests.get(baseurl + "/team/frc" + teamnumber + urlparameters)
        print("Done.")
        print("Parsing team information . . . ", end='')
        parsedteaminfo = json.loads(teaminforequest.text)
        print("Done.")

    # <<< ADD GENERAL TEAM INFO >>>
    print("Adding general team info . . . ", end='')
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
    print("Done.")

    # << ADD TEAM CONTACT INFO >>>
    print("Adding team contact info . . . ", end='')
    html.append("<h2>Contact Information</h2>")
    html.append("<ul>")
    html.append("<li><b>Website:</b> <a href=\""+str(parsedteaminfo["website"])+"\">"+str(parsedteaminfo["website"])+"</a></li>")
    html.append("<li><b>Address:</b> <a href=\""+str(parsedteaminfo["gmaps_url"])+"\">"+str(parsedteaminfo["address"])+"</a></li>")
    html.append("</ul>")
    print("Done.")

    # <<< WRITE HTML TO FILE >>>
    print("Writing HTML file . . . ", end='')
    html.append("</body>")
    html.append("</html>")
    try:
        os.remove("kiosk_results.html")
    except OSError:
        pass
    sleep(0.5)
    htmlfile = open("kiosk_results.html", "w")
    for item in html:
        htmlfile.write("%s\n" % item)
    print("Done.")
    sleep(0.5)
    if not(openedalready):
        try:
            # <<< OPEN HTML FILE IN BROWSER >>>
            print("Opening HTML file in browser . . . ", end='')
            try:
                webbrowser.open("kiosk_results.html")
                print("Done.")
                openedalready = True
            except webbrowser.Error:
                print("Encountered a browser control error.")
            except:
                print("Encountered some error.")
        except:
            print("An error occurred, now printing HTML data instead of viewing it from a file within your browser:")
            print("")
            print("##### START OF HTML DATA #####")
            for item in html:
                print(str(item))
            print("##### END OF HTML DATA #####")

    # <<< HOLD UP >>>
    sleep(5)

# <<< QUIT >>>
quit(0)