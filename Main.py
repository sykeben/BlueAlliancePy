##############################
# BLUEALLIANCEPY MAIN SCRIPT #
##############################

# <<< INTRO >>>
print("BlueAlliancePy Console")
print("(C)2018 - Ben Sykes")
print("")

# <<< SET VARIABLES >>>
print("Setting variables . . . ", end='')
importsuccess = True
keyvalid = True
null = None
print("Done.")
print("")

# <<< FORMAT HTML HEADER >>>
print("Starting HTML . . . ", end='')
html = ["<html>",
        "<head>",
        "<title>BlueAlliancePy Results</title>",
        "<style>",
        "body {",
        "font-family: \"Lucida Sans Unicode\", \"Lucida Grande\", sans-serif;",
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
teamnumber = input("Team # ......... ")
if not(keyvalid):
    apikey = input("API Key ........ ")
print("")

# <<< GET ALL TEAM INFO >>>
print("Gathering all team information . . . ", end='')
teaminforequest = requests.get(baseurl+"/team/frc"+teamnumber+urlparameters)
if teaminforequest.status_code == 200:
    print("Successful.")
elif teaminforequest.status_code == 300:
    print("Successful, but nothing has been modified since.")
elif teaminforequest.status_code == 401:
    print("Unsuccessful, the API key is invalid.")
    quit(401)
elif teaminforequest.status_code == 404:
    print("Unsuccessful, The server cannot be found.")
    quit(404)
else:
    print("Recieved a weird code: "+str(teaminforequest.status_code))
print("")
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
    os.remove("results.html")
except OSError:
    pass
try:
    htmlfile = open("results.html", "w")
    for item in html:
        htmlfile.write("%s\n" % item)
    print("Done.")
    # <<< OPEN HTML FILE IN BROWSER >>>
    print("Opening HTML file in browser . . . ", end='')
    try:
        webbrowser.open("results.html")
        print("Done.")
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

# <<< QUIT >>>
quit(0)