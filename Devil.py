import os
import random
import time
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
#import smtplib as slip
#import pyjokes as pk



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
def tc():
    v = sc.Recognizer()
    with sc.Microphone() as src:
        print("listening")
        v.pause_threshold = 0.5
        audio=v.listen(src,timeout=10,phrase_time_limit=10)
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
    tim = time.strftime("%I:%M %p")

    if hr>=0 and hr<=12:
        spk("Good Morning , its {tim} BOSS")
    elif hr>12 and hr<=18:
        spk(f"Good Afternoon , its {tim} BOSS")
    else:
        spk(f"Good Evening , its {tim} BOSS")
    spk("I am, Devil, how can i help you ?")


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
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cp.release()
            cv2.destroyAllWindows()

        elif"play song" in query or "music" in query:
            music_dir="C:\\Users\\SHIVASAI\\Downloads\\songs"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir,songs[0]))

        elif "video" in query or "movie" in query:
            vid_dir="C:\\Users\\SHIVASAI\\Downloads\\video"
            video = os.listdir(vid_dir)
            rd = random.choice(video)
            os.startfile(os.path.join(vid_dir,video[0]))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            spk(f"your ip address is {ip}")

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

        elif "send message" in query or "text" in query:
            time.sleep(120)
            kit.sendwhatmsg("+919113516754","HI AMMA",12,30)

        elif"close notepad" in query:
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

        elif "gangster" in query:
            kit.playonyt("Gangster Paradise - COOLIO")

        elif"shift"in query or "window"in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        elif"headlines devil"in query:
            spk("Doing BOSS")
            news()


        elif "clear" in query:
            spk("Thank You BOSS,Have a great day")
            sys.exit()

        spk("BOSS,any other work")




