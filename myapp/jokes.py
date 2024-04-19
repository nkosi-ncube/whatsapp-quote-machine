import requests

def getJokes():
    api_url = 'https://api.api-ninjas.com/v1/jokes'
    response = requests.get(api_url, headers={'X-Api-Key': 'H6odIiPP40xwvWhH3xoYBQ==kZLWBhas1FD5YEkv'})
    if response.status_code == requests.codes.ok:
        if response.json() ==[]:           
            return f"No joke found"
        else:
            qoute = response.json()     
                
            return qoute
    else:
        print("Error:", response.status_code, response.text)

print("JOKE:" ,getJokes()[0].get("joke"))