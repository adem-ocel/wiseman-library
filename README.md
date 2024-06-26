
# wiseman library

 
Wiseman is a Python library for adding voice assistant features to your applications and building personal assistant applications.


## Features

- executes the function you give when called
- can be called by more than one name
- voice recording
- audio playback
- voice to text
- text-to-speech (Gtts)
- text-to-speech (Elevenlabs)


## download

Run this project to use it

```bash
 pip install wiseman_library
```

  
## Usage/Examples





|function|module|function
|---|---|---|
|lissen()|wiseman_library| listens to the microphone at the specified interval and calls the given function when its name is called|   
|stop_listen()|wiseman_library|stops listening to microphone| 
|record()|wiseman_library.Recorder| records audio for the given recording time and saves it to the given location|   
|recognize()|wiseman_library.Recognizer|translates the given audio to text with the default method|
|recognize_from_google()|wiseman_library.Recognizer| converts the given voice to text with the speech_recognition library|
|play_sound()|wiseman_library.speaker|plays the given sound file|
|speak()|wiseman_library.speaker|reads text with default text reader|
|speak_with_eleven_labs()|wiseman_library.speaker| Speaks text with eleven_labs api|
|speak_with_gtts()|wiseman_library.speaker| Speaks text with Gtts|








Example of **lissen() function**
```python
import wiseman_library
def fun(name,text):
    print(name+" :: "+text)
wiseman_library.lissen(function=fun)
```

  
## Authors and Acknowledgments

- [@adem-ocel](https://github.com/adem-ocel) for design and development.

  [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
