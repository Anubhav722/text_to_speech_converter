import pyttsx
engine = pyttsx.init()
string = raw_input("Enter text to convert to speech: ")
engine.say(string)
engine.runAndWait()
