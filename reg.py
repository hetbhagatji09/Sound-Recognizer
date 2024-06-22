import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

while True:
    try:
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            print("Say something")
            audio = recognizer.listen(source)
            
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

    except sr.UnknownValueError:
        # Handle the error if speech is unintelligible
        print("Sorry, I could not understand the audio")
        continue

    
