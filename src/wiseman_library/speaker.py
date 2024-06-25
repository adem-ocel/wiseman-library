
from elevenlabs import play
from elevenlabs.client import ElevenLabs
import pygame
from gtts import gTTS
import os

class ElevenLabsApi_info:
    api_key=""
    voice="D1xRw7f8ZHedI7xJgfvz"
    model="eleven_multilingual_v2"

def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def speak_with_eleven_labs(self,text):
    client = ElevenLabs(api_key=ElevenLabsApi_info.api_key)

    audio = client.generate(
    text= text,
    voice=ElevenLabsApi_info.voice,
    model=ElevenLabsApi_info.model
    )
    play(audio)


def speak_with_gtts(text,lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("saying.mp3")
    play_sound("saying.mp3")    
    os.remove("saying.mp3")

class speak_methods:
    gtts = speak_with_gtts
    elevenlabs = speak_with_eleven_labs

speak_method=speak_methods.gtts

def speak(text,lang='en',speak_method=speak_method):
    speak_method(text,lang)    