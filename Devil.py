import os
import random
import time
from PyPDF2 import PdfReader
import pyautogui
import pyttsx3
import speech_recognition as sc
import datetime
import cv2
import requests
from pywhatkit import playonyt
from requests import get
from wikipedia import summary
import webbrowser
import pywhatkit as kit
import sys
#import smtpmail as slip
import pyjokes as pk 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def spk(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

    
def news():
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6ed667a322df40418ade476103b8dd78'
    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        spk(f"today's {day[i]} news is : {head[i]}")


def tc() -> str:
    v = sc.Recognizer()
    with sc.Microphone() as src:
        print("listening")
        v.pause_threshold = 0.5
        audio=v.listen(src,timeout=12,phrase_time_limit=12)
    try:
        print("Recognizing")
        query = v.recognize_google(audio, language='en-in')
        print(f"Command:{query}")
        #spk(query)

    except Exception as e:
        spk("Say that Again Boss")
        return"none"
    return query

def wish():
    hr=int(datetime.datetime.now().hour)
    tim = time.strftime("%I:%M:%S %p")

    if hr>=0 and hr<=12:
        spk(f"Good Morning , its {tim} BOSS")
    elif hr>12 and hr<=18:
        spk(f"Good Afternoon , its {tim} BOSS")
    else:
        spk(f"Good Evening , its {tim} BOSS")
    spk("I am, Devil, how can i help you")

def pdf_read():
    try:
        book = open('C:\\Users\\SHIVASAI\\Downloads\\imp pdf.pdf','rb')
    # Pdf= pdfreader.version(book)
        pdfreader = PdfReader(book)
        pages =len(pdfreader.pages)
        spk(f"Total number of pages in this book is {pages} Boss")
        spk("Boss Enter the page number you want to read")
        pg=int(input())
        page=pdfreader.pages[pg-1]
        text=page.extract_text()
        spk(text)
    except Exception as e:
        print(f"An error occurred:{e}")

if __name__=="__main__":
    wish()
    #tc()
    #spk("Hi Boss")
    while True:
    #if 1:

        query = tc().lower()
        if "notepad" in query:
            pth="C:\\Windows\\System32\\notepad.exe"
            os.startfile(pth)

        elif "cmd"in query:
            os.system("start cmd")

        elif "camera" in query:
            cp = cv2.VideoCapture(0)
            while True:
                ret, img = cp.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(10)& 0xFF == 27:
                    break
            cp.release()
            cv2.destroyAllWindows()

        elif"play song" in query or "music" in query:
            music_dir="C:\\Users\\SHIVASAI\\Downloads\\songs\\music"
            songs = [song for song in os.listdir(music_dir) if song.endswith(".mp3")]
            if songs:
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

        elif "video" in query or "movie" in query:
            vid_dir="C:\\Users\\SHIVASAI\\Downloads\\video"
            video = os.listdir(vid_dir)
            rd = random.choice(video)
            os.startfile(os.path.join(vid_dir,video[0]))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            spk(f"your ip address is {ip}")
            print(f"ip {ip}")

        elif "wikipedia" in query:
            spk("searching wikipedia...")
            query=query.replace("wikipedia","")
            results = summary(query, sentences=1)
            spk("According to wikipedia")
            spk(results)
            print(results)

        elif "youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "linkedin" in query:
            webbrowser.open("linkedin.com")

        elif "stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "google" in query:
            spk("What do you need Boss")
            cm= tc().lower()
            webbrowser.open(f"{cm}")

        elif "open case" in query:
            webbrowser.open("www.google.com")

        #elif "send message" in query or "text" in query:
            #time.sleep(120)
            #kit.sendwhatmsg("+919113516754","HI AMMA",12,30)

        elif"close note" in query:
            spk("Done BOSS")
            os.system("taskkill /f /im notepad.exe")

        elif "close cmd" in query:
            spk("Done BOSS")
            os.system("taskkill /f /im cmd.exe")

        elif"close player"in query:
            spk("Done BOSS")
            os.system("taskkill /f /im vlc.exe")

        elif"die"in query:
            spk("bye,BOSS")
            os.system("shutdown /s /t 5")

        elif "reboot" in query:
            spk("Will see you soon,BOSS")
            os.system("shutdown /r /t 5")

        elif "again" in query:
            kit.playonyt("see you again")

        elif"be" in query:
            kit.playonyt("believer")

        elif "walk" in query:
            kit.playonyt("Alan Walker")

        elif"stupid" in query:
            kit.playonyt("Skibidi Toilet Full Song Music Video")

        elif"sigma" in query:
            kit.playonyt("Sigma Boy (RMX)")

        elif"let's go" in query:
            kit.playonyt("AUTOMOTIVO MANGOS–(DJ BRZ 013)")

        elif"gamer" in query:
            kit.playonyt("Chapati Hindustani Gamer")

        elif"minecraft" in query:
            kit.playonyt("Hindustan Gamer Loggy")

        elif"game" in query:
            kit.playonyt("")

        elif"gojo" in query:
            kit.playonyt("empathy - crystal castles [edit audio]")

        elif "gangster" in query:
            kit.playonyt("Gangster Paradise -COOLIO")

        elif"shift"in query or "window"in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        elif"headlines devil"in query:
            spk("Working on it BOSS")
            news()


        elif "clear" in query:
            spk("Thank You BOSS,Have a great day")
            sys.exit()

        elif"introduce yourself"in query or "tell me about you"in query or "tell me about yourself"in query:
            spk("Glad to hear that, I am, Devil ,An AI developed by Shiva G ,Here to do your work easy by voice ")

        elif "where am i" in query or "where are we" in query:
            spk("Working on it BOSS")
            try:
                ip=requests.get('https://api.ipify.org').text
                print(ip)
                url='https://get.geojs.io/v1/ip/geo/'+ip+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data['city']
                country=geo_data['country']
                spk(f"I am not sure, but here is some info of city {city} and country {country}")
            except  ExceptionGroup as e:
                spk("Sorry i am not able to get it ")
                pass

        elif"take screenshot"in query:
            spk("Working on it BOSS, suggest a Name ")
            name=tc().lower()
            spk(f"Taking screenshot of {name} Boss")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            spk(f"Screenshot taken and saved as {name} Boss")

        elif"read pdf"in query:
            pdf_read()

        elif"hello"in query or "hi"in query:
            spk("Hello Boss")
            spk("How are you ?")

        elif"i am fine"in query or "i am good"in query or "i am doing well"in query :
            spk("Great BOSS")
            spk("its glad to hear that")

        elif"i am not fine"in query or "i am not good"in query or "i am not doing well"in query:
            spk("Sure BOSS")
            spk("Tell me how can i help you")

        elif"what is your name"in query:
            spk("I am Devil")

        elif"who are you"in query:
            spk("I am an Ai model developed by Shiva G")

        elif"dance"in query:
            spk("Sorry I am not able to dance")
            spk("But i can tell you a joke")
            spk("that is ...........")
            spk("I am so intelligent.........")

        elif"what's an AI"in query:
            spk("An Artificial Helper in everything or By Doing work easy for humans")
            spk("Created By humans.......")
            spk("Example, i am Created by Shiva G")

        spk("BOSS,any other work")
