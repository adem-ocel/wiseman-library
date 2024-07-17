from elevenlabs import play
from elevenlabs.client import ElevenLabs
import pygame
from gtts import gTTS
from io import BytesIO

lang = 'en'

class ElevenLabsApi_info:
    api_key = ""
    voice = "D1xRw7f8ZHedI7xJgfvz"
    model = "eleven_multilingual_v2"

def play_sound(byte_data):
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(byte_data)
    sound.play()

def speak_with_eleven_labs(text):
    client = ElevenLabs(api_key=ElevenLabsApi_info.api_key)

    audio = client.generate(
        text=text,
        voice=ElevenLabsApi_info.voice,
        model=ElevenLabsApi_info.model
    )
    play(audio,use_ffmpeg=False)

def speak_with_gtts(text, lang=lang):
    tts = gTTS(text=text, lang=lang)
    byte_data = BytesIO()
    tts.write_to_fp(byte_data)
    byte_data.seek(0)
    play_sound(byte_data)


speak = speak_with_gtts
