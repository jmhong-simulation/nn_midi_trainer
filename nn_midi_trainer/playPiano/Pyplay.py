import pyaudio
import wave
import time
import numpy
import os

# get current directory
cwd = os.getcwd() 

# open multiple waves
wf1 = wave.open(cwd+"piano88\Piano 030.wav", 'rb')
wf2 = wave.open(cwd+"piano88\Piano 001.wav",'rb')
p = pyaudio.PyAudio()

# attach wf2 to wf1 channel
def callback(in_data, frame_count, time_info, status):
    data1 = wf1.readframes(frame_count)
    data2 = wf2.readframes(frame_count)
    decodeddata1 = numpy.fromstring(data1, numpy.int16)
    decodeddata2 = numpy.fromstring(data2, numpy.int16)
    data = (decodeddata1 * 0.5 + decodeddata2 * 0.5).astype(numpy.int16)
    return (data, pyaudio.paContinue)

# open stream
stream = p.open(format=p.get_format_from_width(wf1.getsampwidth()),
                channels=wf1.getnchannels(),
                rate=wf1.getframerate(),
                output=True,
                stream_callback=callback)

# play stream
stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()
wf1.close()

p.terminate()
