import speech_recognition as sr
import io

lang = 'en'

def recognize_from_google(voice_byte_array, lang=lang):
    engine = sr.Recognizer()
    audio_buffer = io.BytesIO(voice_byte_array)
    with sr.AudioFile(audio_buffer) as source:
        voice_data = engine.record(source)
        try:
            text = engine.recognize_google(voice_data, language=lang)
            return text
        except sr.UnknownValueError as e:
            return str(e)
        except sr.RequestError as e:
            return str(e)

        
recognize = recognize_from_google
