import time
import os
from mido import MidiFile

from pyPlayMusic import pyPlayMusic

#http://www.piano-midi.de/beeth.htm
mid = MidiFile(os.getcwd()+'\sampleMidi\moonlight.mid')
note=[]
tmp_event=[]
event_list=[]
duration =0
timing =0  #add all of ticks
"""
for i in range(0,88):  #initialize note
   note.append(0)
"""
print ("Ticks per beat:"),
print (mid.ticks_per_beat)
for i, track in enumerate(mid.tracks):
    print('Track {} : {} '.format(i, track.name))

for message in track:
    timing += message.time
    if message.type == 'note_on' and message.bytes()[2] != 0:
        event_list.append([message.bytes()[1]-20,timing])

    """
    if message.type == 'note_on' and note[event[1]-20] == 0: #Sometimes show only 'note_on'
        #print message
        note[event[1]-20] =timing #  filenumber of Note C4 is 40 and number of Evete[1] C4 is 60. These diffrence is 20
    elif  message.type == 'note_off' :
        duration=(timing - note[event[1]-20])
        event_list.append([ note[event[1]-20] , event[1]-20 , duration])
        note[event[1]-20] = 0
    elif message.type == 'note_on' and note[event[1]-20] != 0 :
        duration=(timing - note[event[1]-20])
        event_list.append([ note[event[1]-20] , event[1]-20 , duration])
        note[event[1]-20] = 0
    else:     #All functions is included except Note_on, Note_off
        continue
    """

time_ = 0
playone = []
playlist = []

print event_list

for i in event_list:
    if len(playone) == 0 or time_ == i[1]:
        playone.append(i[0])
    else:
        playlist.append(playone)
        playone = [i[0]]
        time_ = i[1]

print playlist

for play in playlist:
    print play
    pyPlayMusic.playNotes(play).play()
    time.sleep(160/480.)
