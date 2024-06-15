This Python script utilizes the pyttsx3 library to convert text to speech. The script is designed to initialize the text-to-speech engine, select a voice, and then speak a given text string.

Requirements
Python 3.x
pyttsx3 library
Installation
Before running the script, you need to install the pyttsx3 library. You can install it using pip:

pip install pyttsx3

Usage
Initialization: The script initializes the pyttsx3 engine using the sapi5 driver, which is typically used on Windows.

Voice Selection: It retrieves the available voices and sets the engine to use the first voice in the list.

Speak Function: A function speak(query) is defined to take a text string (query) as input and convert it to speech using the engine.

Main Execution: When the script is run as the main module, it calls the speak function with the text 'thanks for watching'.

code example

import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")

# Get the list of available voices
voices = engine.getProperty("voices")

# Set the engine to use the first voice in the list
engine.setProperty("voice", voices[0].id)

# Function to convert text to speech
def speak(query):
    engine.say(query)
    engine.runAndWait()

# Main block to test the speak function
if __name__ == "__main__":
    speak('thanks for watching')


    Customization
    
Changing Voice: You can change the voice by selecting a different index from the voices list.
Changing Text: Modify the string passed to the speak function to change the spoken text.

Troubleshooting
Ensure that pyttsx3 is correctly installed.
If you encounter issues with voice selection, check the list of available voices by printing voices and inspect their properties.
