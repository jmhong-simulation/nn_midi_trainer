import pyaudio
import wave
import time
import numpy
import os
from mido import MidiFile

# playmusic function
# @input type(codes) == array && 0 <= each data <= 88
def playmusic(codes=[]):

   cwd = os.getcwd()

   wfs = []

   for code in codes:
       wfs.append(wave.open(cwd+"\piano88\Piano 0"+str(code)+".wav",'rb'))

   p = pyaudio.PyAudio()

   def callback(in_data, frame_count, time_info, status):
       datas = []
       decodeddatas = []
       for wf in wfs:
           datas.append(wf.readframes(frame_count))
       for data in datas:
           decodeddatas.append(numpy.fromstring(data,numpy.int16))
       data = (sum(decodeddatas) * 0.5).astype(numpy.int16)
       return (data,pyaudio.paContinue)

   stream = p.open(format=p.get_format_from_width(wfs[0].getsampwidth()),
                   channels=wfs[0].getnchannels(),
                   rate=wfs[0].getframerate(),
                   output=True,
                   stream_callback=callback)

   stream.start_stream()

   while stream.is_active():
       time.sleep(0)
   stream.close()
   wfs[0].close()

   p.terminate()

   return True

#######HOW TO USE : main##########
if __name__ == '__main__':
#    playmusic([57])    # press one key
#    playmusic([57,59]) # press two key
#    playmusic([57,60,63]) # press three key
    mid = MidiFile('Merry Go Round of Life (piano solo).mid')
    note=[]
    timing =0
    for i in range(0,88):
       note.append(0)
    for i, track in enumerate(mid.tracks):
       print('Track {}: {}'.format(i, track.name))
    for message in track:
        event= message.bytes()   #event consists of [function, note, deltatime]
        if 144 <= event[0] < 160: #0x90~0x9F note_on 
            note[event[1]-20] =1 #  filenumber of Note C4 is 40 and number of Evete[1] C4 is 60. These diffrence is 20
            print event[1]
            playmusic([event[1]-20])   
        elif 128 <=event[0] <144: #0x80~0x8F note_off
            note[event[1]-20] =0
           # print note
        else:     #All function except Note_on, Note_off
            continue
