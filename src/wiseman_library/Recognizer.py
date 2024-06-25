import speech_recognition as sr

def recognize_from_google(voice="voice.wav", lang='en'):
    engine = sr.Recognizer()
    with sr.AudioFile(voice) as source:
        voice_data = engine.record(source)
        try:
            text = engine.recognize_google(voice_data, language=lang) 
            return text
        except sr.UnknownValueError as e:
            return str(e)
        except sr.RequestError as e:
            return str(e)
        
def recognize(voice="voice.wav", lang='en'):
    return recognize_from_google(voice)
