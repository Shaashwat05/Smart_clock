from gtts import gTTS 
import playsound

def text_to_speech(text):

    language = 'en'

    myobj = gTTS(text=text, lang=language, slow=False) 

    myobj.save("welcome.mp3") 


    playsound.playsound('welcome.mp3', True)




