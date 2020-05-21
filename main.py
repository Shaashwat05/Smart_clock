import speech_recognition as sr 
from time_date import dt
from weather import weather

r = sr.Recognizer()
m = sr.Microphone()

city = input("enter the city you live in:")

start = True

while(start):

    try:
        with m as source:

            r.adjust_for_ambient_noise(source)
            
            print("start speaking")
            audio = r.listen(source)
            Mytext = r.recognize_google(audio)
            Mytext = Mytext.lower()
            print(Mytext)
            if("time" in Mytext):
                date, time = dt()
                print(date)
            
            if("date" in Mytext):
                date, time = dt()
                print(date)

            if("weather" in Mytext):
                temperature, humidity, pressure, cond = weather(city)
            

            if(Mytext[len(Mytext)-4:] == 'quit'):
                start = False

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 