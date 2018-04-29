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


def checkteam(team_number):
    team_number = str(team_number)
    data_code = requests.get(base_url + "/team/frc" + team_number + "?X-TBA-Auth-Key=" + api_key).status_code
    if data_code == 200:
        return True
    elif data_code == 304:
        return True
    elif data_code == 404:
        return False


def checkserveronline():
    try:
        if requests.get("https://www.thebluealliance.com").status_code != 404:
            return True
        else:
            return False
    except ConnectionError:
        return False
    except requests.ConnectionError:
        return False
