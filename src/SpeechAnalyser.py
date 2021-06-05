import speech_recognition as sr

r = sr.Recognizer()
sample = sr.AudioFile("sample_audio.wav")
with sample as source:
    audio = r.record(source)
    text = r.recognize_google(audio)
    print(text)