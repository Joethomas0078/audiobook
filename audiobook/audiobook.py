import pyttsx3

f = open('file.txt', 'r')

engine = pyttsx3.init()
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')

#f
#engine.setProperty('voice', voices[1].id)

#m
engine.setProperty('voice', voices[0].id)

engine.save_to_file(f.read(), 'book.mp3')
engine.runAndWait()
engine.stop()