import googletrans
import speech_recognition as sr
import gtts
recognizer=sr.Recognizer()
translator=googletrans.Translator()

##print(googletrans.LANGUAGES)
d=googletrans.LANGUAGES
text =input("enter text to translate")
t=input("translating language")

li=d.items()
for i in li:
    if i[1]==t:
        s=i[0]
    
translated=translator.translate(text,dest=s)
print("translated text",translated.text)
