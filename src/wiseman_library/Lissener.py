from . import Recorder
from . import Recognizer
from . import tempfile_manager
names = [
    "wiseman"
]

__lissening = True

def lissen(function, recordtime=3,recorderfunction=Recorder.record,recognizefunction=Recognizer.recognize):
    global __lissening
    __lissening = True
    while __lissening:
        recordedfile = recorderfunction(recordtime)
        text = recognizefunction(recordedfile).lower()
        for name in names:
            replacedtext = text.replace(name, '')
            if name in text:
                function(name, replacedtext)
    
def stop_listen():
    global __lissening
    __lissening = False
    tempfile_manager.clean_tempfiles()