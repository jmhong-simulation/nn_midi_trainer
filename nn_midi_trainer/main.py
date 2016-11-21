import time
import os
from mido import MidiFile

import readmidi_nn
import data_set_nn

from pyPlayMusic import pyPlayMusic

playlist = readmidi_nn.readmidi("/sampleMidi/moonlight.mid")
"""
for play in playlist:
    #print play
    pyPlayMusic.playNotes(play).play()
    time.sleep(160/480.)
"""
x,y = readmidi_nn.makeMidi_nn(playlist,24)

batch = data_set_nn.data_set_nn(x,y)

batchX, batchY = batch.get_next_batch(size=100)
print len(x[0])
print len(y[0])
for i in batchY:
    a = []
    for j in range(len(i)):
        if i[j] == 1:
            a.append(j)
    print a
    pyPlayMusic.playNotes(a).play()
    time.sleep(160 / 480.)