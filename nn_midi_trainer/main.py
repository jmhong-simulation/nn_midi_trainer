import time
import os
from mido import MidiFile

import readmidi_nn
import data_set_nn

from pyPlayMusic import pyPlayMusic

# for windows "\sampleMidi\moonlight.mid"
playlist = readmidi_nn.readmidi("/sampleMidi/moonlight.mid")
"""
for play in playlist:
    #print play
    pyPlayMusic.playNotes(play).play()
    time.sleep(160/480.)
"""
x,y = readmidi_nn.makeMidi_nn(playlist,24)
print(len(x[0][0]))
print(len(y[0]))

batch = data_set_nn.data_set_nn(x,y)

# batch test
batchX, batchY = batch.get_next_batch(size=40)
print batchX
print batchY
batchX, batchY = batch.get_next_batch(size=33)
print batchX
print batchY
batchX, batchY = batch.get_next_batch(size=33)
print batchX
print batchY