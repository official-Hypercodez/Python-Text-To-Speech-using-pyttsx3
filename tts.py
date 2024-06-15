import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voices",voices[0].id)

def speak(query):
	engine.say(query)
	engine.runAndWait()

if __name__ == "__main__":
	speak('thanks for watching')