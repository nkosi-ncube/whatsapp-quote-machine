import requests
from .categories import categories
from dotenv import load_dotenv
import os

def getQoute(category):   
    load_dotenv()
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': os.environ.get("API_KEY")})
    if response.status_code == requests.codes.ok:
        if response.json() ==[]:           
            return f"These are the available categories : {categories()}"
        else:
            qoute = response.json()     
                
            return qoute
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    category = input("Category: ")    
    print(getQoute(category))


