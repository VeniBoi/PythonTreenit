import requests
import json
import time
import datetime

#Kysytään käyttäjän syöte, eli miltä viikolta ja päivältä ruoka
# lista halutaan
print("Valitse minkä viikon, sekä päivän ruokalistan haluat, jos vaihtoehtoisesti haluat suoraan tämän päivän ruokalistan,\n"
      "jätä kenttä tyhjäksi ja paina enter...\n")
viikko = input("Viikko: ")

if viikko == '':
    #Haetaan tämän päivän tiedot
    date = datetime.date.today()  # if date is 01/01/2018
    year, week_num, day_of_week = date.isocalendar()

    viikko = str(week_num)
    paiva = str(day_of_week)
    print("Ei syötettä, haetaan tämän päivän ruokalista...")
else:
    paiva = input("Päivä (numeroina): ")

print("\nHaetaan...")
#d-kirjain on tuossa vaan siks ku se JSON filu on hassun mallinen
response = requests.get('https://www.juvenes.fi/DesktopModules/Talents.LunchMenu/LunchMenuServices.asmx/GetMenuByWeekday?KitchenId=46&MenuTypeId=60&Week=' + viikko + '&Weekday=' + paiva + '&lang=%27fi%27&format=json')
respDict = json.loads(response.json()["d"])
print("Valmis!\n")
time.sleep(0.5)

if respDict['MealOptions'][0]['Name'] == "[CLOSED]":
    print("Nyt kävi jokin virhe, tai vaihtoehtoisesti tälle päivälle ei ole ruokalistaa (esim. viikonloppu).")
else:
    print("Skene tarjoilee: \n")

    for x in respDict['MealOptions']:
        for y in x['MenuItems']:
            print(y['Name'])







