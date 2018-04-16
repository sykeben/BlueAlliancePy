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
print("Done.")
print("")

# <<< IMPORT LIBRARIES AND MODULES >>>
print("Importing libraries and modules:")

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

if not(importsuccess):
    print("Some errors occurred, the application may not work properly.")
print("")

# <<< AUTO CONFIGURATION >>>
print("Auto-configuring what can be auto-configured . . . ", end='')
apikey = "GJouaQ0y5drrhoMYJVZ42pbZGFGXtrMZPmAqaZBHBJblsKRsfM3Vf0q7raTnsXOl"
baseurl = "https://www.thebluealliance.com/api/v3"
print("Done.")
print("")

# <<< USER CONFIGURATION >>>
print("Please input the following information:")
teamnumber = input("Team # ......... ")
print("")

# <<< GET TEAM INFO >>>
print("Gathering team information . . . ", end='')
teaminforequest = requests.get(baseurl+"/team/frc"+teamnumber+"/simple"+"?X-TBA-Auth-Key="+apikey)
print("Returned: "+str(teaminforequest))
print("Parsing team information . . . ", end='')
parsedteaminfo = json.loads(teaminforequest.text)
print("Done.")
print("")

# <<< DISPLAY TEAM INFO >>>
print("City ............... "+parsedteaminfo["city"])
print("Country ............ "+parsedteaminfo["country"])
print("Name ............... "+parsedteaminfo["name"])
print("Nickname ........... "+parsedteaminfo["nickname"])
print("State/Providence ... "+parsedteaminfo["state_prov"])
print("Number ............. "+str(parsedteaminfo["team_number"]))