import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()  # Make sure to run and wait for the engine to speak the text

def input_instruction():
    instruction = ""
    try:
        with sr.Microphone() as origin:
            print("listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "siri" in instruction:
                instruction = instruction.replace("siri", "")
                print(instruction)
    except:
        pass
    return instruction

def play_Siri():
    while True:
        instruction = input_instruction()
        print(instruction)
        if "play" in instruction:
            song = instruction.replace("play", "")
            talk("playing " + song)
            pywhatkit.playonyt(song)
        elif 'time' in instruction:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            talk("the time is " + time)
        elif 'date' in instruction:
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            talk("the date is " + date)
        elif 'how are you' in instruction:
            talk("I am fine, how about you?")
        elif 'who are you' in instruction:
            talk("I am siri, your personal assistant")
            talk("I can help you with playing songs, telling time and date, and many features are coming soon")
            talk("What can I do for you?")
        elif 'who is' in instruction:
            human = instruction.replace("who is", "")
            info = wikipedia.summary(human, 1)
            talk(info)
        elif 'exit' in instruction:
            talk("For sure, have a nice day")
            break
        elif 'what is' in instruction:
            object = instruction.replace("what is", "")
            info = wikipedia.summary(object, 1)
            talk(info)
        else:
            talk("I am not able to understand you. Can you repeat, please?")

if __name__ == "__main__":
    play_Siri()