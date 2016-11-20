import numpy as np

class data_set_nn():
    def __init__(self,setX,set_y):
        self._dataX = setX
        self._dataY = set_y
        self._batch_index = 0
        self._dataX_length = len(setX)

    def get_next_batch(self,size=100):
        self._batch_index += size

        batch_xs = []
        batch_ys = []

        for i in range(self._batch_index, self._batch_index+size):
            array = []
            for j in range(len(self._dataX[i%self._dataX_length])):
                for q in self._dataX[i%self._dataX_length][j]:
                    array.append(q)
            batch_xs.append(array)



        array = []
        for i in range(self._batch_index, self._batch_index+size):
            for j in self._dataY[i%self._dataX_length]:
                array.append(j)
            batch_ys.append(array)
            array=[]

        batch_xs = np.asarray(batch_xs,dtype=np.float64)
        batch_ys = np.asarray(batch_ys,dtype=np.float64)

        return batch_xs, batch_ys