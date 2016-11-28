import tensorflow as tf
import numpy as np
import time
"""
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
"""
x = tf.placeholder(tf.float32,[None,24 * 88])

W = tf.Variable(tf.zeros([24 * 88, 88]))
b = tf.Variable(tf.zeros([88]))

y = tf.nn.softmax(tf.matmul(x,W) + b) # actual #softmax is for classification

y_ = tf.placeholder(tf.float32, [None, 88] ) # want
print x,W,b,y,y_
"""
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])
"""
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

##########

import readmidi_nn
import data_set_nn


playlist = readmidi_nn.readmidi("/sampleMidi/moonlight.mid")

#TODO: rename xx->x_input, yy->y_target
x_input,y_target = readmidi_nn.makeMidi_nn(playlist,24)

#TODO: batch_feeder
batch_feeder = data_set_nn.data_set_nn(x_input,y_target)

train_answer=1
wrong_answer=1
for i in range(10000):
    """
    batch_xs, batch_ys = mnist.train.next_batch(100)
    """
    x_input_batch, y_target_batch = batch_feeder.get_next_batch(size=100)
    sess.run(train_step, feed_dict={x: x_input_batch, y_: y_target_batch})

    # test output
    if i % 1000 == 0:
        continue



playlist = []
x_input_batch, y_target_batch = batch_feeder.get_next_batch(size=1)
for i in range(300):
    playone = []
    _y = sess.run(y, feed_dict={x: x_input_batch})

    for j in _y:
        hum = 0
        hum_arr = []
        note =1
        for k in j:
            if (k > 0.2):
                hum_arr.append(k)
                hum+=1
            if(k > 0.2):
                playone.append(note)
            note= note+1
        #print hum, hum_arr
    playlist.append(playone)

    next = []
    for i in range(1,89):
        if i in playone:
            next.append(1)
        else:
            next.append(0)
    #print x_input_batch, [next]
    x_input_batch = np.append(x_input_batch[0][88:],next)
    x_input_batch = np.asarray([x_input_batch])
    #print x_input_batch
print (playlist)

