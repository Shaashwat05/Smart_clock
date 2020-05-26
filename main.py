import speech_recognition as sr 
from time_date import dt
from weather import weather,set_city
from t2s import text_to_speech
from news import news
import nltk
from summarization import summary

nltk.download('stopwords')

r = sr.Recognizer()
m = sr.Microphone()

valid = False
while not valid:
    city = input("enter the city you live in:")
    valid = set_city

start = True



def stp_words(Mytext):
    stopwords = nltk.corpus.stopwords.words('english')
    str = ''
    for word in Mytext:
        if word not in stopwords:
            return word



while(start):

    try:
        with m as source:

            r.adjust_for_ambient_noise(source)
            
            print("the date and time are :", dt())

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

            if("news" in Mytext):
                keyword = stp_words(Mytext)
                story = news(keyword)
                summ = summary(story)
                text_to_speech(summ)


            if(Mytext[len(Mytext)-4:] == 'quit'):
                start = False

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 