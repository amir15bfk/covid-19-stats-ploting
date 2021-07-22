import requests

url = "https://coronavirus-smartable.p.rapidapi.com/stats/v1/DZ/"

headers = {
    'x-rapidapi-key': "175bb7317amshc592db3b123e5e6p1a5a83jsne007e2ab754f",
    'x-rapidapi-host': "coronavirus-smartable.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



def get_new_deaths():
    return response["stats"]["newDeaths"]

def get_new_Cases():
    return response["stats"]["newlyConfirmedCases"]

def get_total_Cases():
    return response["stats"]["totalConfirmedCases"]

def get_tota_lDeaths():
    return response["stats"]["totalDeaths"]


print(get_new_deaths())