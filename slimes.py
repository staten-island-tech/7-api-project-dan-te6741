import requests

def getslime(slime):
    response = requests.get(f"https://github.com/apriltaoyvr/slime-rancher-api/{slime.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
    }

slimer = getslime("Pink Slime")
print(slimer)