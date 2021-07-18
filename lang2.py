import googletrans
import speech_recognition as sr
import gtts
recognizer=sr.Recognizer()
translator=googletrans.Translator()
try:
    with sr.Microphone() as source:
        print('speak now')
        voice=recognizer.listen(source)
        text=recognizer.recognize_google(voice)
        print(text)
except:
    pass
d=googletrans.LANGUAGES

t=input("translating language")

li=d.items()
for i in li:
    if i[1]==t:
        s=i[0]
    
translated=translator.translate(text,dest=s)
print("translated text",translated.text)
