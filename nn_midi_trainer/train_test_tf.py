import tensorflow as tf
import time
"""
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
"""
x = tf.placeholder(tf.float32,[None,24 * 88])

W = tf.Variable(tf.zeros([24 * 88, 88]))
b = tf.Variable(tf.zeros([88]))

y = tf.nn.softmax(tf.matmul(x,W) + b) # actual

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

xx,yy = readmidi_nn.makeMidi_nn(playlist,24)

batch = data_set_nn.data_set_nn(xx,yy)

for i in range(10000):
    """
    batch_xs, batch_ys = mnist.train.next_batch(100)
    """
    batch_xs, batch_ys = batch.get_next_batch(size=100)

    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # test output
    if i % 20 == 0:
        batch_xs, batch_ys = batch.get_next_batch(size=1)
        _y = sess.run(y,feed_dict={x:batch_xs})

        count = 0
        for i in _y:
            for j in i:
                if j > 0.9:
                    count+=1
        print count