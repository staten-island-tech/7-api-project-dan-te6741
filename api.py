import requests 
date = input("input a date here (YYYYMMDD)")
ans = requests.get(f"https://isdayoff.ru/{date}") 

if ans.text == 0:
    print("Workday")
elif ans.text == 1:
    print ("Day off")
elif ans.text == 2:
    print("Shortened day")



