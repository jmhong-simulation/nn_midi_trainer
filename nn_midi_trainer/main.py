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
for i in range(0,88):  #initialize note
   note.append(0)
print ("Ticks per beat:"),
print (mid.ticks_per_beat)
for i, track in enumerate(mid.tracks):
    print('Track {} : {} '.format(i, track.name))
for message in track:
    event= message.bytes()   #event consists of [function, note, velocity]
    timing += message.time
    if message.type == 'note_on' and note[event[1]-20] == 0: #Sometimes show only 'note_on' 
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
tick_start =0
tick_end = timing
event_list.sort()
time_table=[]
beat_list=[]
beat=1             
div_per_beat =4
for i in range(len(event_list)):
    if event_list[i][0] < beat * mid.ticks_per_beat/div_per_beat:
        beat_list.append(event_list[i])
    else :
        beat_list.append(event_list[i])
        time_table.append(beat_list[:])
        for num in range(len(beat_list)):
            beat_list.pop()
        beat+=1
#for i in range(len(time_table)) :
#    print (i),(" : "),(time_table[i])
for i in range(len(time_table)) :
   for j in range(len(time_table[i])):
      pyPlayMusic.playNotes(codes=[time_table[i][j][1]]).play()
   time.sleep((80/(float(480))))
