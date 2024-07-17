from . import Recorder
from . import Recognizer
names = [
    "wiseman"
]

__lissening = True

def lissen(function, recordtime=3):
    global __lissening
    __lissening = True
    while __lissening:
        recordedfile = Recorder.record(recordtime)
        text = Recognizer.recognize(recordedfile).lower()
        for name in names:
            replacedtext = text.replace(name, '')
            if name in text:
                function(name, replacedtext)
    
def stop_listen():
    global __lissening
    __lissening = False
