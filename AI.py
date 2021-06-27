""" IMPORT LIBRARIES """
import os
import pyttsx3
import platform
import psutil
import speech_recognition as sr
import datetime
import time
import wikipedia
import wolframalpha
import subprocess
import webbrowser
import requests
import json
import pyjokes
import socket
import random
from PIL import ImageGrab
from plyer import notification
# To do list ;)
''' TO DO IN FUTURE 
1) Control tello drone using voice (CHARLIE)
2) Put as many notifiers as possible
3) Make this AI as interactive as possible (basically Add a ChatBot ;)) 
4) Increase functionalities
5)  
'''

""" ENGINE INITIALIZATION """
engine = pyttsx3.init('sapi5')
time_now = datetime.datetime.now()
today = datetime.date.today()
""" LISTS AND DICTIONARIES """
links = {
    'Circuits class': r'https://classroom.google.com/c/Mjk3NTg1NzcwMDUw',
    'Circuits meet': '',
    'Fabrication class': r'https://classroom.google.com/u/0/c/Mjk4NTkxNjE1OTc3',
    'Vector class': r'https://classroom.google.com/u/0/c/MzE2NjA2NzQyMDY0',
    'Differential Equations class': r'https://classroom.google.com/u/0/c/MzE4NjM4NTYwMjkw',
    'Differential Equations meet': r'https://iith.webex.com/iith/j.php?MTID=mdcd7957d51a50abba9fcadc07e366f0b',
    'Fabrication tutorial class': r'https://classroom.google.com/u/0/c/MzEwNDg5NTM1MTU2',
    'Digital Systems class': r'https://classroom.google.com/c/MjczNTE4MjY5NDE3',
    'Signals class': r'https://classroom.google.com/c/Mjk3NjMyMTUxNTA0',
    'Basic Electrical class': r'https://classroom.google.com/c/Mjk4MDM3Mzk2OTgz'
}
GREET = ['hello charlie', 'are you there', 'hey charlie', 'charlie']
RETURN_GREET = ['always there for you sir', 'online and ready sir', 'i am ready sir']
INTRO = ['introduce yourself', 'who are you', 'what is your name']
Adjectives = ['awesome', 'great', 'fine']

''' REQUIRED APIs and URLs '''
news_url_base = r'https://newsapi.org/v2/top-headlines?country=in&apiKey=2738c3307a314006b2cd1ac9607ac8bd&pageSize=10'
news_api_key = r"your newsapi_key"
weather_api_key = r'your weatherapi_key'
weather_url_base = rf'http://api.openweathermap.org/data/2.5/weather?appid={weather_api_key}&units=metric&q='
wolframalpha_api_key = r"your wolframalpha key"

''' ASSISTANT MODES '''
TALKER = True
DRONE = False

''' REQUIRED FUNCTIONS '''
def initialize():
    speak("Initializing boot sequence")
    speak('Checking all the system utilities boss')
    speak("All processes and utilities are in good condition")
    speak("Internet connection is stable")
    speak("All drivers are functioning well boss")
    speak("Looks everything is good")
    speak("I am JARVIS, a personalized voice assistant")
    greetMe()
    speak('''I am Ready to rock and roll. Wake me with the key word "Hello JARVIS"''')

def get_number_grade(param):
    if param == 'A+' or param == 'A':
        return 10
    elif param == 'A-':
        return 9
    elif param == 'B':
        return 8
    elif param == 'B-':
        return 7
    elif param == 'C':
        return 6
    elif param == "C-":
        return 5
    elif param == 'D':
        return 4
    elif param == 'FR':
        return 0

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    if 0 <= time_now.hour < 12:
        speak("Good Morning sir. Hope you will have a great day ahead")
    elif 12 <= time_now.hour < 17:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")

def getTime(time):
    if time.hour == 0:
        print(f"Time now - 12:{time.minute} AM")
        speak(f"Now, the time is 12 {time.minute} AM sir")
    elif time.hour == 12:
        print(f"Time now - 12:{time.minute} PM")
        speak(f"Now, the time is 12 {time.minute} PM sir")
    elif 0 < time.hour < 12:
        print(f"Time now - {time.hour}:{time.minute} AM")
        speak(f"Now, the time is {time.hour} {time.minute} AM sir")
    elif 12 < time.hour <= 23:
        print(f"Time now - {time.hour}:{time.minute} PM")
        speak(f"Now, the time is {time.hour-12} {time.minute} PM sir")
    else:
        speak("Error occured while finding the time sir")

def getCPI():
    with open('courses.txt', 'r') as file:
        CREDITS = 0
        POINTS = 0
        for line in file:
            param = line.split(', ')
            CREDITS += int(param[1])
            POINTS += int(param[1]) * get_number_grade(param[2])
        print(f"Your CPI or CGPA till now is {POINTS/CREDITS:.3f} and you have completed {CREDITS} credits")
        speak(f"Your CPI or CGPA till now is {POINTS/CREDITS:.3f} and you have completed {CREDITS} credits")

def readNews(query):
    count = 1
    if 'tech' in query:
        news_url = news_url_base + '&category=technology'
    elif 'science' in query:
        news_url = news_url_base + '&category=science'
    elif 'business' in query:
        news_url = news_url_base + '&category=business'
    elif 'entertainment' in query:
        news_url = news_url_base + '&category=entertainment'
    elif 'sports' in query:
        news_url = news_url_base + '&category=sports'
    elif 'health' in query:
        news_url = news_url_base + '&category=health'
    elif 'overall' in query or 'general' in query:
        news_url = news_url_base + '&category=general'
    else:
        speak("Cannot fetch this news sir. I am sorry")
        return 0
    speak("Collecting the news..")
    try:
        response = requests.get(news_url).text
    except Exception:
        speak("Error raised while collecting news sir")
    news = json.loads(response)
    for article in news['articles']:
        print(f"News {count}")
        speak(f"News {count}")
        print(article['title'])
        speak(article['title'])
        speak("Description")
        print(article['description'])
        speak(article['description'])
        print(article['url'])
        speak("Sir, please go to this url to know more about this news,")
        count += 1
    speak("This is the end of today's news sir")

def greetOnBirthdays():
    if today.day == 23 and today.month == 3:
        speak("Sir, Wish you a very Happy Birthday. Thank you for creating me")
    elif today.day == 29 and today.month == 3:
        speak("Sir, today is Maanas's birthday. I wish him a very Happy Birthday.")
    elif today.day == 21 and today.month == 9:
        speak("Sir, Its your Mother's birthday today. I wish a very Happy Birthday to your mother")

def getCommand():
    bot = sr.Recognizer()
    bot.pause_threshold = 0.5
    bot.energy_threshold = 5000

    with sr.Microphone() as source:
        print("Listening..")
        speak("Waiting for command sir")
        bot.adjust_for_ambient_noise(source, duration=1)
        audio = bot.listen(source)
        try:
            print("Recognizing..")
            speak("Converting to text")
            text = bot.recognize_google(audio, language='en-in')
            print(f"You have said: {text}")
        except Exception as e:
            speak("An error has been raised sir")
            return 'None'
        return text

def getSystemStats():
    to_gb = 1024*1024*1024
    system = platform.system()
    release = platform.release()
    processor = platform.processor()
    cpus = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()
    RAM_usage = [psutil.virtual_memory().total / to_gb, psutil.virtual_memory().available / to_gb, psutil.virtual_memory().percent, psutil.virtual_memory().used / to_gb]
    ROM_usage = [psutil.disk_usage('/').total / to_gb, psutil.disk_usage('/').used / to_gb, psutil.disk_usage('/').free / to_gb, psutil.disk_usage('/').percent]
    battery_remaining = psutil.sensors_battery().percent
    speak("Here is the present status of the using laptop.")
    print(f"System Information: Operating System: {system}, Version: {release}, Processor: {processor}, Number of CPU: {cpus}")
    speak(f"System Information: Operating        System: {system}, Version: {release}, Processor: {processor}, Number of CPU: {cpus}")
    print(f"Sir, {cpu_percent} percent of the CPU is being used. ")
    speak(f"Sir, {cpu_percent} percent of the CPU is being used. ")
    print(f"RAM Usage Status: Total RAM available is {RAM_usage[0]:.2f} GB, Free RAM available is {RAM_usage[1]:.2f} GB, RAM used is {RAM_usage[3]:.2f} GB")
    speak(f"RAM Usage Status: Total RAM available is {RAM_usage[0]:.2f} GB, Free RAM available is {RAM_usage[1]:.2f} GB, RAM used is {RAM_usage[3]:.2f} GB")
    print(f"Percentage of RAM being used is {RAM_usage[2]:.2f} percent")
    speak(f"Percentage of RAM being used is {RAM_usage[2]:.2f} percent")
    print(f"ROM Usage Status: Total ROM available is {ROM_usage[0]:.2f} GB, Free ROM available is {ROM_usage[2]:.2f} GB, ROM used is {ROM_usage[1]:.2f} GB")
    speak(f"ROM Usage Status: Total ROM available is {ROM_usage[0]:.2f} GB, Free ROM available is {ROM_usage[2]:.2f} GB, ROM used is {ROM_usage[1]:.2f} GB")
    print(f"Percentage of ROM being used is {ROM_usage[3]:.2f} percent")
    speak(f"Percentage of ROM being used is {ROM_usage[3]:.2f} percent")
    print(f"{battery_remaining} percent of the battery is remaining, Sir")
    speak(f"{battery_remaining} percent of the battery is remaining, Sir")

def getWeather(query='Jeedimetla'):
    weathernews = requests.get(f'{weather_url_base}{query}').text
    weather = json.loads(weathernews)
    if weather['cod'] != 404:
        speak('Collecting the weather data, sir')
        # print(weather)
        temperature = weather['main']['temp']
        min_temp = weather['main']['temp_min']
        max_temp = weather['main']['temp_max']
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']
        wind_dir = weather['wind']['deg']
        visibility = weather['visibility']
        cloud_cover = weather['clouds']['all']
        description = weather['weather'][0]['description']
        weather = f"Sir, the weather in {query} is as follows. " \
                  f"Temperature is {temperature} degree Celsius. Minimum temperature can be {min_temp} degrees Celsius. " \
                  f"Maximum temperature can be {max_temp} degree Celsius. Ground level Pressure is {pressure} hectopascals. " \
                  f"Relative humidity is {humidity} percent. Windspeed is around {wind_speed} metres per second, inclined at {wind_dir} degrees. . " \
                  f"Visibility is around {visibility} percent. Clouds cover is approximately {cloud_cover} percent. " \
                  f"Finally, the description about this weather is, {description}"
        print(weather)
        speak(weather)
        speak('This is all about the present weather, sir')

''' MODE FUNCTIONS '''
def talker_mode():
    speak("I am in the Talker Mode")
    Auth = False
    global TALKER
    global DRONE
    while not Auth and TALKER == True:
        bot = sr.Recognizer()
        bot.pause_threshold = 0.5
        bot.energy_threshold = 4000
        with sr.Microphone() as source:
            voice = bot.listen(source)
            try:
                wake = bot.recognize_google(voice)
                speak(wake)
                if 'hello' in wake or 'jarvis' in wake:
                    Auth = True
            except:
                print("Exception")
        while Auth and TALKER == True:
            today = datetime.date.today()
            query = getCommand().lower()
            if query != "none":
                if 'how are you' in query:
                    print(f"I am always {random.choice(Adjectives)} sir. Hope you are happy, healthy and safe")
                    speak(f"I am always {random.choice(Adjectives)} sir. Hope you are happy, healthy and safe")

                elif 'sleep' in query:
                    speak("Entering sleep mode")
                    Auth = False

                elif 'drone' in query:
                    TALKER = False
                    DRONE = True

                elif 'who am i' in query:
                    speak("You are Ashish, my creator. I am very grateful to you")

                elif 'open google' in query:
                    speak("Opening Google..")
                    webbrowser.open("https://www.google.com/")

                elif 'open youtube' in query:
                    speak("Opening Youtube..")
                    webbrowser.open('https://www.youtube.com/')

                elif query in INTRO:
                    speak("Hello Sir, I am Mojo. I am a personalized voice assistant developed by Ashish..")

                elif 'wikipedia' in query:
                    query = query.replace("wikipedia", "")
                    speak("Searching in Wikipedia..")
                    try:
                        result = wikipedia.summary(query, sentences=5)
                        print(result)
                        speak(f"According to wikipedia, {result}")
                    except Exception as e:
                        speak("An error has been raised sir")

                elif 'search' in query and 'in google' in query:
                    result = query.replace('search', "")
                    result = result.replace('in google', "")
                    speak(f"Searching for {result}")
                    webbrowser.open(f'http://google.com/search?q={result}')
                    speak("Opened")

                elif 'cgpa' in query or 'cpi' in query:
                    getCPI()

                elif 'open gmail' in query:
                    speak("Opening Gmail..")
                    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

                elif 'open codechef' in query:
                    speak("Opening Codechef..")
                    webbrowser.open('https://www.codechef.com/')

                elif 'open hackerrank' in query:
                    speak('Opening Hackerrank..')
                    webbrowser.open('https://www.hackerrank.com/dashboard')

                elif 'news' in query and ('read' in query or 'tell' in query):
                    readNews(query)

                elif 'open whatsapp' in query:
                    speak("Opening Whatsapp")
                    subprocess.call('C://Users//Balu//AppData//Local//WhatsApp//WhatsApp.exe')

                elif 'open matlab' in query:
                    speak("Opening matlab")
                    subprocess.call('D://aashu//MATLAB//bin//matlab.exe')

                elif 'open arduino' in query:
                    speak('Opening Arduinp')
                    subprocess.call('D://aashu//Arduino//arduino.exe')

                elif 'open vs code' in query:
                    speak('Opening VS Code')
                    subprocess.call('C://Users//Balu//AppData//Local//Programs//Microsoft VS Code//Code.exe')

                elif 'open prime' in query:
                    speak("Opening Prime Video..")
                    webbrowser.open("https://www.primevideo.com/")

                elif 'open hotstar' in query:
                    speak("Opening Hotstar..")
                    webbrowser.open("https://www.hotstar.com/in")

                elif 'make a note' in query or 'note this' in query:
                    print('What do I have to note sir?')
                    speak('What do I have to note sir?')
                    text = getCommand().lower()
                    date = datetime.datetime.now()
                    file_name = f"{str(date).replace(':', '-')}-notepad.txt"
                    with open(file_name, 'w') as file:
                        file.write(text)
                    subprocess.Popen(['C://Program Files (x86)//Notepad++//notepad++.exe', file_name])

                elif 'close' in query:
                    speak("Which application should i close, sir?")
                    app = getCommand().lower()
                    if app == 'notepad':
                        os.close('C://Program Files (x86)//Notepad++//notepad++.exe')
                    if app == 'whatsapp':
                        os.kill("C://Users//Balu//AppData//Local//WhatsApp//WhatsApp.exe")
                    if app == 'matlab':
                        os.close('D://aashu//MATLAB//bin//matlab.exe')
                    if app == 'arduino':
                        os.close('D://aashu//Arduino//arduino.exe')

                elif 'time now' in query:
                    getTime(datetime.datetime.now())

                elif 'open' in query and ('class' in query or 'meet' in query):
                    for key in links.keys():
                        if key.lower() in query:
                            speak(f"Opening {key}")
                            webbrowser.open(links[key])

                elif 'screenshot' in query:
                    speak("Taking the screenshot sir")
                    time.sleep(1)
                    image = ImageGrab.grab()
                    image.show()

                elif 'ip address' in query:
                    host = socket.gethostname()
                    ip = socket.gethostbyname(host)
                    print(f"Your computer name is {host} and your IP address is {ip}")
                    speak(f"Your computer name is {host} and your IP address is {ip}")

                elif 'weather' in query:
                    print("Which place's weather do you want to know sir?")
                    speak("Which place's weather do you want to know sir?")
                    weat = getCommand()
                    getWeather(weat)

                elif 'system' in query and ('perform' in query or 'doing' in query or 'status' in query):
                    getSystemStats()

                elif 'calculate' in query or 'solve' in query:
                    speak('Processing the required fields')
                    client = wolframalpha.Client(wolframalpha_api_key)
                    answer = client.query(query)
                    result = answer.results
                    try:
                        res = next(result).text
                        print(f"Answer for your question is {res}")
                        speak(f"Answer for your question is {res}")
                    except Exception as e:
                        print(e)
                        speak(f"{e} Error has been occured sir")

                elif 'joke' in query:
                    joke = pyjokes.get_joke(language='en')
                    print(joke)
                    speak(joke)

                elif 'what is' in query or 'who is' in query or 'tell me about' in query or 'where is' in query:
                    speak('Fetching required data')
                    client = wolframalpha.Client(wolframalpha_api_key)
                    answer = client.query(query)
                    result = answer.results
                    try:
                        try:
                            res = next(result).text
                            speak("Results obtained from Wolfram Alpha")
                            print(res)
                            speak(res)
                        except:
                            ans = wikipedia.summary(query, sentences=5)
                            speak("Results obtained from Wikipedia")
                            print(ans)
                            speak(ans)
                    except Exception as e:
                        print(e)
                        speak(f"Unable to fetch results, sir")

                elif 'thank you' in query:
                    print("You are always welcome sir. Its my pleasure")
                    speak("You are always welcome sir. Its my pleasure")

                elif 'bye' in query or 'see you later' in query:
                    speak('I will be at your service whenever you need. Bye Bye. See you later sir')
                    exit(0)

                elif 'shut' in query and 'down' in query:
                    speak('Shutting down the system')
                    time.sleep(2)
                    os.system('shutdown /s /t 1')

                elif 'restart' in query and 'system' in query:
                    speak("Restarting the system")
                    time.sleep(2)
                    os.system('shutdown /r /t 1')
    speak("Exiting Talker mode")

def drone_mode():
    global TALKER
    global DRONE
    speak("We are in drone mode")
    while True and DRONE == True:
        query = getCommand().lower()
        if 'exit'in query:
            speak("Leaving drone mode")
            exit(0)
        elif 'hello' in query:
            speak("Hello Sir, I am now controlling your drone")
        elif 'talker' in query:
            DRONE = False
            TALKER = True
    speak("Exiting Drone mode")


""" ACTION BEGINS ;) """

if __name__ == "__main__":
    initialize()
    if psutil.sensors_battery().percent < 10:
        while not psutil.sensors_battery().power_plugged:
            speak("Power low")
            notification.notify(
                title="Low power",
                message="Please recharge the device using a power source as soon as possible",
                timeout=5
            )
            time.sleep(2)
    # greetOnBirthdays()
    while True:
        if TALKER:
            talker_mode()
        if DRONE:
            drone_mode()
        else:
            speak("I am not in any mode sir. Would you like me to go offine?")
            com = getCommand()
            if 'exit' in com or 'go offline' in com:
                quit()
