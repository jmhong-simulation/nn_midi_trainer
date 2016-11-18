"""
    Coded by Davi Innovation
    davinnovation at gmail.com

    playNotes
"""

import pyaudio
import os
import time
import numpy

global get_PyAudio
get_PyAudio = pyaudio.PyAudio()

class playNotes():
    def __init__(self,codes=[40], chunk_size=2**15):
        import wave
        cwd = os.path.dirname(os.path.realpath(__file__))
        self._wfs = []

        for code in codes:
            c = ""
            if code > 0 and code < 10:
                c = "0"+str(code)
            elif code < 89:
                c = str(code)
            else:
                print("out of code index")
                exit()
            self._wfs.append(wave.open(cwd + "\piano88\Piano 0" + c + ".wav", 'rb'))


    def play(self,onset=None):
        """
        Play is handled in the background (multithreading)
        """
        import threading
        self.onset = onset
        trial = 0
        while trial < 3:
            try:
                trial += 1
                self._thread_play = threading.Thread(target=self._play)
                self._thread_play.start()
                return
            except Exception:
                raise RuntimeError('Could not set up thread')

    def _play(self):

        def callback(in_data, frame_count, time_info, status):
            datas = []
            decodeddatas = []
            for wf in self._wfs:
                datas.append(wf.readframes(frame_count))
            for data in datas:
                decodeddatas.append(numpy.fromstring(data,numpy.int16))
            data = (sum(decodeddatas) * 0.5).astype(numpy.int16)
            return (data,pyaudio.paContinue)

        self._stream = get_PyAudio.open(format=get_PyAudio.get_format_from_width(self._wfs[0].getsampwidth()),
										channels=self._wfs[0].getnchannels(),
										rate=self._wfs[0].getframerate(),
										output=True,
										stream_callback=callback)

        while self._stream.is_active():
            time.sleep(0.1)
        self._stream.stop_stream()
        self._stream.close()


# example
if __name__ == '__main__':
    playNotes(codes=[57]).play()
    time.sleep(0.3)
    playNotes(codes=[57, 59]).play()
    time.sleep(0.3)
    playNotes(codes=[57, 60, 63]).play()
    time.sleep(0.3)
    playNotes(codes=[57, 60, 63,66]).play()
    time.sleep(0.3)
    playNotes(codes=[57, 60, 63,66,69]).play()
    time.sleep(0.3)
    playNotes(codes=[57, 60, 63,66,69,72]).play()
    time.sleep(0.3)
    playNotes(codes=[57, 60, 63,66,69,72,75]).play()
    time.sleep(0.3)
    playNotes(codes=[57, 60, 63,66,69,72,75,78]).play()
    time.sleep(0.3)
    playNotes(codes=[57, 60, 63,66,69,72,75,78,81]).play()