import requests

base_url = "https://rickandmortyapi.com/api"

def get_info(type):
    url = f"{base_url}/{type}"
    response = requests.get(url)
    print(response)
    if response.status_code ==200:
        print("Data successfully retrieved")
        raw = response.json()
        char_data = raw["results"]
        return char_data
    else:
        print(f"Date retrieve failed - status code{response.status_code}")

res = "character"
char_info = get_info(res)
if char_info:
    for character in char_info:
        print(f"Name: {character["name"]}, Gender: {character["gender"]}, Status: {character["status"]}, Species: {character["species"]}")
