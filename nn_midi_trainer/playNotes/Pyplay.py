import pyaudio
import wave
import time
import numpy
import os

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
    playmusic([57])    # press one key
    playmusic([57,59]) # press two key
    playmusic([57,60,63]) # press three key
