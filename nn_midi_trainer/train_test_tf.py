import tensorflow as tf
import time
"""
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
"""
x = tf.placeholder(tf.float32,[None,24 * 88])

W = tf.Variable(tf.zeros([24 * 88, 88]))
b = tf.Variable(tf.zeros([88]))

y = tf.nn.softmax(tf.matmul(x,W) + b) # actual #softmax is for classification
#y = tf.nn.sigmoid(tf.matmul(x,W) + b)
#y = tf.nn.relu(tf.matmul(x,W) + b)

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
#this may work as meansquared error
#mean_squared = tf.reduce_mean(tf.square(y_ - y ))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
#train_step = tf.train.GradientDescentOptimizer(0.5).minimize(mean_squared)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

##########

import readmidi_nn
import data_set_nn


playlist = readmidi_nn.readmidi("/sampleMidi/moonlight.mid")

#TODO: rename xx->x_input, yy->y_target
#xx,yy = readmidi_nn.makeMidi_nn(playlist,24)
x_input,y_target = readmidi_nn.makeMidi_nn(playlist,24)

#TODO: batch_feeder
#batch = data_set_nn.data_set_nn(xx,yy)
batch_feeder = data_set_nn.data_set_nn(x_input,y_target)

train_answer=1
wrong_answer=1
for i in range(10000):
    """
    batch_xs, batch_ys = mnist.train.next_batch(100)
    """
    #rename x_input_batch, y_target_batch
    #batch_xs, batch_ys = batch.get_next_batch(size=100)
    x_input_batch, y_target_batch = batch_feeder.get_next_batch(size=100)
    #sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    sess.run(train_step, feed_dict={x: x_input_batch, y_: y_target_batch})
    # test output
    if i % 20 == 0:
        #batch_xs, batch_ys = batch.get_next_batch(size=1)
        x_input_batch, y_target_batch = batch_feeder.get_next_batch(size=1)
        #_y = sess.run(y,feed_dict={x:batch_xs})
        _y = sess.run(y, feed_dict={x: x_input_batch})

        #count = 0
        print(_y)

        for i in _y:
            index = 0
            for j in i:
                if(j>0.9):
                    if y_target_batch[0][index] == 0:
                        wrong_answer+=1
                        break
                """     // This version make only one note so can't make chord
                 else :
                    if y_target_batch[0][index] == 1:
                        wrong_answer += 1
                        break
              """
                index+=1
        train_answer += 1
        print (100.0 - (float(wrong_answer) * 100 / float(train_answer))), ("%")

playone = []
playlist = []
for i in range(300):
    x_input_batch, y_target_batch = batch_feeder.get_next_batch(size=1)
    _y = sess.run(y, feed_dict={x: x_input_batch})
    for j in _y:
        note =1
        for k in j:
            if(k > 0.9 ):
                playone.append(note)
            note= note+1
    playlist.append(playone)
    playone=[]
print (playlist)

