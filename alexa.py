from os import system
from pyttsx3 import speak
speak("Hello alexa how can i help you ")
print("hello alexa how can i help you")
while True:
 p=input("command: ")
 p=p.lower()
 if ((("start" in p) or ("open" in p )or ("execute" in p)) and (("notepad" in p) or ("editor" in p))):
    speak("really you want open notepad")
    x=int(input("you want open notepad please enter number 1 otherwise enter any number:"))
    if x==1:
        system("start notepad")
        print("alexa : notepad is opened")
        speak("notepad is opened")
    else:
        print("now i change my decision.I want to open other .")
        speak("give a new command")
        
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and (("chrome" in p) or ("browser" in p))):
    speak("really you want open chrome")
    x=int(input("you want open chrome please enter number 1 otherwise enter any number:"))
    if x==1:
        system("start chrome")
        print("alexa : chrome is opened")
        speak("chrome is opened ")
    else:
        print("now i change my decision.I want to open other .")
        speak("give new command")
        
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and ("python" in p)):
     speak("really you want open python")
     x=int(input("you want open python please enter number 1 otherwise enter any number:"))
     if x==1:
         system("start python")
         print("alexa : python is opened")
         speak("python is opened")
     else:
         print("now i change my decision.I want to open other .")
         speak("give new command")
     
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and (("media player" in p)or ("window media" in p))):
     speak("really you want open media player")
     x=int(input("you want open media player please enter number 1 otherwise enter any number:"))
     if x==1:
         system("start wmplayer")
         print("alexa : media player is opened")
         speak("media player is opened")
     else:
         print("now i change my decision.I want to open other .")
         speak("give new command")
    
 elif((("start" in p) or ("open" in p ) or ("execute" in p) )and  ("internet exp" in p )):
     speak("really you want open internet explore")
     x=int(input("you want open internet explore please enter number 1 otherwise enter any number:"))
     if x==1:
         system("start iexplore")
         print("alexa :internet explore is opened")
         speak(" internet explore is opened")
     else:
         print("now i change my decision.I want to open other .")
         speak("give new command")
         
 elif ((("start" in p) or ("open" in p )or ("execute" in p)) and (("excel" in p ) or ("microsoft excel" in p ))) :
     speak("really you want open microsoft excel")
     x=int(input("you want open microsoft excel please enter number 1 otherwise enter any number:"))
     if x==1:
         system("start EXCEL")
         print("alexa : excel is opened")
         speak("excel is opened")
     else:
         print("now i change my decision.I want to open other .")
         speak("give new command")
         
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and ("powerpoint" in p )):
     speak("really you want open powerpoint")
     x=int(input("you want open powerpoint please enter number 1 otherwise enter any number:"))
     if x==1:
         system("start POWERPNT")
         print("alexa : powerpoint is opened")
         speak("powerpoint is opened")
     else:
         print("now i change my decision.I want to open other .")
         speak("give new command")
         
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and ("calculator" in p ) ):
     speak("really you want open calculator")
     x=int(input(" really you want open calculator please enter number 1 otherwise enter any number:"))
     if x==1:
         system("start calc")
         print("alexa : calculator is opened")
         speak("calculator  is opened")
     else:
         print("now i change my decision.I want to open other .")
         speak("give the new command :")
         
 elif ((("log off" in p) or ("sign off " in p )) and (("laptop" in p ) or ("computer" in p ) or ("system" in p ))):
     speak("really you want shutdown your system")
     x=int(input("you want shutdown your system please enter number 1 otherwise enter any number:"))
     if x==1:
         system("SHUTDOWN/s")
         print("alexa : signing off ")
         speak("your system is shutdown")
     else:
         print("now i change my decision.I want to open other .")
         speak("give new command")
         
 elif ((("start" in p) or ("open" in p) ) and ("explorer" in p )):
     speak("really you want open file explorer")
     x=int(input("you want open file explorer please enter number 1 otherwise enter any number:"))
     if x==1:
         system("start explorer")
         print("alexa : explorer is opened")
         speak("file explorer is opened")
     else:
         print("now i change my decision.I want to open other .")
         speak("give new command")
         
 elif ("terminate" in p) or ("quit" in p) :
    print("alexa Thank you!!!")
    speak("your program is quit")
    break  
 else:
    print(" does not support")
    speak("alexa you entered worng check again")
