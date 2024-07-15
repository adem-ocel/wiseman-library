
from elevenlabs import play
from elevenlabs.client import ElevenLabs
import pygame
from gtts import gTTS
import os
from . import tempfile_manager
lang = 'en'
class ElevenLabsApi_info:
    api_key=""
    voice="D1xRw7f8ZHedI7xJgfvz"
    model="eleven_multilingual_v2"

def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def speak_with_eleven_labs(text):
    client = ElevenLabs(api_key=ElevenLabsApi_info.api_key)

    audio = client.generate(
    text= text,
    voice=ElevenLabsApi_info.voice,
    model=ElevenLabsApi_info.model
    )
    play(audio)


def speak_with_gtts(text,lang=lang):
    tts = gTTS(text=text, lang=lang)
    file = "/temp/"+tempfile_manager.tempfilename()
    tts.save(file)
    play_sound(file)    

class speak_methods:
    gtts = speak_with_gtts
    elevenlabs = speak_with_eleven_labs

speak_method=speak_methods.gtts

def speak(text,lang=lang,speak_method=speak_method):
    speak_method(text,lang)    