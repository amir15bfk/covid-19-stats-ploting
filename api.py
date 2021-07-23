import requests

url = "https://coronavirus-smartable.p.rapidapi.com/stats/v1/DZ/"

headers = {
    'x-rapidapi-key': "175bb7317amshc592db3b123e5e6p1a5a83jsne007e2ab754f",
    'x-rapidapi-host': "coronavirus-smartable.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



def get_new_deaths():
    r =[]
    for i,item in enumerate(response["stats"]["history"]):
        r.append(item['deaths']-response["stats"]["history"][i-1]['deaths'])
    r[0]=0
    return r

def get_new_cases():
    r =[]
    for i,item in enumerate(response["stats"]["history"]):
        r.append(item['confirmed']-response["stats"]["history"][i-1]['confirmed'])
    r[0]=0
    return r

def get_new_recovered_cases():
    r =[]
    for i,item in enumerate(response["stats"]["history"]):
        r.append(item['recovered']-response["stats"]["history"][i-1]['recovered'])
    r[0]=0
    return r

def get_total_recovered_cases():
    r =[]
    for item in response["stats"]["history"]:
        r.append(item['recovered'])
    return r

def get_total_cases():
    r =[]
    for item in response["stats"]["history"]:
        r.append(item['confirmed'])
    return r
    
def get_total_deaths():
    r =[]
    for item in response["stats"]["history"]:
        r.append(item['deaths'])
    return r

