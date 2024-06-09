
from elevenlabs import play
from elevenlabs.client import ElevenLabs

class ElevenLabsApi_info:
    api_key=""
    voice="D1xRw7f8ZHedI7xJgfvz"
    model="eleven_multilingual_v2"

def speak_with_eleven_labs(self,text):
    client = ElevenLabs(api_key=ElevenLabsApi_info.api_key)

    audio = client.generate(
    text= text,
    voice=ElevenLabsApi_info.voice,
    model=ElevenLabsApi_info.model
    )
    play(audio)
def speak(self,text):
    speak_with_eleven_labs(text)    