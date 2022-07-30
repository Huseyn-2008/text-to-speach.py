import pyttsx3
#pip install pyttsx3

engine = pyttsx3.init()

def text_to_spech():
    text = input("Enter something: ")
    if text == 'exit':
        exit()
    else:
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[1].id)
        engine.say(text)
        engine.runAndWait()
while True:
    text_to_spech()
