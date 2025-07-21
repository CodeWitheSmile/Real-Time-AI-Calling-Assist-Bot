import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)  # Speed (default ~200)
    engine.setProperty('volume', 1.0)  # Volume: 0.0 to 1.0

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female (may vary by system)

    engine.say(text)
    engine.runAndWait()

