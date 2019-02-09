import speech_recognition as sr
import summary as s

print('hi')
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

    
print('hi')
try:
    command = r.recognize_google(audio)

    with open('gen.txt', 'w') as f:
        print(command, file=f)

except:
    print('Soryy')

s.generate_summary('gen.txt')
