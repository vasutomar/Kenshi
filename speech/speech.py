import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio = r.record(source)

command = r.recognize_google(audio)

with open('gen.txt', 'w') as file:
    print(command, file=file)