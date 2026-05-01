import requests

def getslime(slime):
    response = requests.get(f"https://slime-rancher.vercel.app/api/slime")
    if response.status_code != 200:
        return None
    data = response.json()
    


slimer = getslime("pink")
print(slimer)

