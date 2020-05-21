import speech_recognition as sr 
from time_date import dt
from weather import weather,set_city
from t2s import text_to_speech

r = sr.Recognizer()
m = sr.Microphone()

valid = False
while not valid:
    city = input("enter the city you live in:")
    valid = set_city

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
                date_time = dt()
                text_to_speech(" the time is " + str(date_time))
                       
            if("date" in Mytext):
                date_time = dt()
                text_to_speech(" the time is " + str(date_time))

            if("weather" in Mytext):
                temperature, humidity, pressure, cond = weather(city)
                text_to_speech("the temperature is " + str(temperature) + "and" + str(cond))

            if(Mytext[len(Mytext)-4:] == 'quit'):
                start = False

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 