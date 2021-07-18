import googletrans
import speech_recognition as sr
import gtts
import playsound
recognizer=sr.Recognizer()
translator=googletrans.Translator()
try:
    with sr.Microphone() as source:
        print('speak now')
        voice=recognizer.listen(source)
        text=recognizer.recognize_google(voice,language='en')
        print(text)
except:
    pass
t=input("translating language")

d=googletrans.LANGUAGES
li=d.items()
for i in li:
    if i[1]==t:
        s=i[0]
        break
translated=translator.translate(text,dest=s)
converted_audio=gtts.gTTS(translated.text,lang=s)
converted_audio.save("r.mp3")
playsound.playsound("r.mp3")
