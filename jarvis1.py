import shutil
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import winreg

engine=pyttsx3.init()

def get_chrome_path():
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe") as key:
            chrome_path, _ = winreg.QueryValueEx(key, "")
            return chrome_path
    except FileNotFoundError:
        return None

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("I am JARVIS")

def time():
    Time=datetime.datetime.now().strftime('%I:%M:%S')
    speak("The current time is")
    speak(Time)



def Date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def GreetMe():
    speak("Welcome back ma'am!")
    Date()
    time()
    hour=datetime.datetime.now().hour
    if(hour>=6 and hour<12):
        speak("Good morning ma'am!")
    elif(hour>=12 and hour<18):
        speak("Good afternoon ma'am!")
    elif(hour>=18 and hour<22):
        speak("Good evening ma'am!")
    else:
        speak("Good night ma'am!")
    speak("JARVIS at your service. Please tell me how can i help you.")


def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"

    return query
def SendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",'576')
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com","123")
    server.sendmail("abc@gmail.com",to,content)

def screenshot():
    img=pyautogui.screenshot()
    img.save("code.png")

def CPU():
    usage=str(psutil.cpu_percent())
    speak("The CPU is at"+usage)
    battery=psutil.sensors_battery()
    speak("The battery is at")
    speak(battery)

def jokes():
    speak(pyjokes.get_joke())

if __name__=="__main__":
    GreetMe()
    while True:
        query=TakeCommand().lower()
        if 'date' in query:
            Date()
        elif 'time' in query:
            time()
        elif 'wikipedia' in query:
            print("Searching...")
            query=query.replace("wikipedia","")
            try:
                result=wikipedia.summary(query,sentences=2)
                print(result)
                speak(result)
            except Exception as e:
                print(e)
                speak("Match not found")
        elif 'send email' in query:
            
            speak("What should i say?")
            content=TakeCommand()
            to="xyz@gmail.com"
            try:
                SendEmail(to,content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the mail.")
        
        elif 'search in chrome' in query:
            chrome_path = get_chrome_path()
            print(chrome_path)
            speak("What should i search?")
            chromepath=f"{chrome_path} %s"
            search=TakeCommand()
            speak("You said me to search that"+search)
            wb.get(chromepath).open_new_tab(search+".com")
        
        elif 'play songs' in query:
            songs_dir="Music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'remember that' in query:
            speak("What should i remember?")
            data=TakeCommand()
            speak("You said me to remember that"+data)
            remember=open('data.txt','a')
            remember.write(data)
            remember.close()
        
        elif'do you know anything'in query:
            remember=open('data.txt','r')
            speak("You said me to remember that"+remember.read())
        
        elif 'screenshot' in query:
            screenshot()
            speak("Done")
        
        elif 'cpu' in query:
            CPU()
        
        elif 'joke' in query:
            jokes()
        
        elif 'log out' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'offline' in query:
            quit()