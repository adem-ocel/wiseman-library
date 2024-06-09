import Recorder
import Recognizer
names = [
    "wiseman"
]

__lissening = True

def lissen(function, recordtime=3):
    __lissening = True
    while __lissening:
        Recorder.record(3,"voice.wav")
        text = Recognizer.recognize().lower()
        for name in names:
            replacedtext = text.replace(name, '')
            if name in text:
                function(name, replacedtext)
def stop_listen():
    __lissening = False

def printer(name, replacedtext):
    print ("---------------------------------------------------------")
lissen(printer)