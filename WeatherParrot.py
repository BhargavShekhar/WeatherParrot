import requests     # to search from the API
import json         # to convert api from string to dictionary
import pyttsx3      # to add text to speech

city = input("Enter City name:\n")
url = f"https://api.weatherapi.com/v1/current.json?key=54eaea5a5bf742c98f3155022240402&q={city}"
responce = requests.get(url)

weatherDict = json.loads(responce.text)

speak = pyttsx3.init()

speak.setProperty('rate', 145)
speak.setProperty('volume', 0.9)

if responce.status_code == 200:
    # print(responce.text)
    print(f"Temperature: {weatherDict["current"]["temp_c"]}")
    speak.say(f"{city} has {weatherDict["current"]["temp_c"]} degree celcius")
    speak.runAndWait()
    print(f"Weather Type: {weatherDict["current"]["condition"]["text"]}")
    speak.say(f"Weather type is {weatherDict["current"]["condition"]["text"]}")
    speak.runAndWait()
    print(f"Wind: {weatherDict["current"]["wind_kph"]}kph")
    speak.say(f"Wind is {weatherDict["current"]["wind_kph"]} kilometer per hour")
    speak.runAndWait()

else:
    print("Request failed")