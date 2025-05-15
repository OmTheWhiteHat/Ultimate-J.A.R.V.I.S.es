import os
import eel
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *



def start():
    
    eel.init("frontend") 
    
    play_assistant_sound()
    @eel.expose
    def init():
        try:
            eel.hideLoader()
            speak("Welcome to Jarvis")
            speak("Ready for Face Authentication")
            flag = recoganize.AuthenticateFace()
            if flag == 1:
                speak("Face recognized successfully")
                eel.hideFaceAuth()
                eel.hideFaceAuthSuccess()
                speak("Welcome to Your Assistant")
                eel.hideStart()
                play_assistant_sound()
                return "authenticated"
            else:
                speak("Face not recognized. Please try again")
                return "unauthorized"
        except Exception as e:
            print("Error in init():", e)
            return {"status": "error", "message": str(e)}
        
    os.system('start msedge.exe --app="http://127.0.0.1:8000/index.html"')
    
    
    
    eel.start("index.html", mode=None, host="localhost", block=True) 

