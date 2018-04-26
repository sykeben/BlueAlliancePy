import requests
import json

base_url = "https://www.thebluealliance.com/api/v3"
api_key = ""


def readjsondata(path):
    raw_data = requests.get(base_url + path + "?X-TBA-Auth-Key=" + api_key)
    parsed_data = json.loads(raw_data.text)
    return parsed_data


def teaminfo(team_number, value_name):
    data = readjsondata("/team/frc" + str(team_number))
    if value_name == "/~ALL":
        out = data
    else:
        out = data[value_name]
    return out


def getstatus(value_name):
    data = readjsondata("/status")
    if value_name == "/~ALL":
        out = data
    else:
        out = data[value_name]
    return out