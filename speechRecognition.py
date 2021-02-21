import speech_recognition as sr;
import webbrowser as wb;
import pyaudio;

r1 = sr.Recognizer();

with sr.Microphone() as source:
    print("speak anything")
    audio = r1.listen(source)
    try:
        text =  r1.recognize_google(audio)
        print("you said: ",format(text))
    except:
        print('failed'.format(e))