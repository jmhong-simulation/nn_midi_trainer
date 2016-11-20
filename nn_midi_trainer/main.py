import time
import os
from mido import MidiFile

import readmidi_nn

from pyPlayMusic import pyPlayMusic

playlist = readmidi_nn.readmidi("\sampleMidi\moonlight.mid")
"""
for play in playlist:
    #print play
    pyPlayMusic.playNotes(play).play()
    time.sleep(160/480.)
"""
x,y = readmidi_nn.makeMidi_nn(playlist)
