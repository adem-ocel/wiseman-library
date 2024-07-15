#tempfile_manager.py
import random
import string
import os
import glob
import time
def tempfilename():
    length = 22
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def clean_tempfiles():
    for file in glob.glob(os.path.join('temp', '*')):
        os.remove(file)
        print(file)