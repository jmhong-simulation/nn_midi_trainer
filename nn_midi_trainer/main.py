import time
import os
from mido import MidiFile

from pyPlayMusic import pyPlayMusic


mid = MidiFile(os.getcwd()+'\sampleMidi\Merry Go Round of Life (piano solo).mid')
note = []
timing = 0
for i in range(0, 88):
    note.append(0)
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))

for message in track:
    event = message.bytes()  # event consists of [function, note, deltatime]
    if 144 <= event[0] < 160:  # 0x90~0x9F note_on
        note[event[1] - 20] = 1  # filenumber of Note C4 is 40 and number of Evete[1] C4 is 60. These diffrence is 20
        print event[1]
        pyPlayMusic.playNotes(codes=[event[1] - 20]).play()
        time.sleep(0.3)
    elif 128 <= event[0] < 144:  # 0x80~0x8F note_off
        note[event[1] - 20] = 0
        # print note
    else:  # All function except Note_on, Note_off
        continue
