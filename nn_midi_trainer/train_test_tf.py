import tensorflow as tf
import time
"""
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
"""
x = tf.placeholder(tf.float32,[None,24 * 88])
y_ = tf.placeholder(tf.float32,[None,88])

W = tf.Variable(tf.zeros([24 * 88, 88]))
b = tf.Variable(tf.zeros([88]))

x = tf.nn.relu(x)
y =  tf.matmul(x,W) + b
"""
# Create model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer with RELU activation
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Construct model
pred = multilayer_perceptron(x, weights, biases)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Initializing the variables
init = tf.initialize_all_variables()

"""
# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, y_))
train_step = tf.train.AdamOptimizer(0.001).minimize(cost)


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

correct_answer = 0
train_answer = 0
for k in range (1):
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
            for i in _y:
                index = 0
                max_=0.0
                print("")
                print(i)
                for j in i:
                    if((j / max_) > 0.90 ):
                        if j>max_:
                            max_=j
                        if y_target_batch[0][index] == 1:
                            correct_answer+=1
                    index+=1
            train_answer += 1
            print (float(correct_answer) * 100 / float(train_answer)), ("%")    #Not Correct percentage It only one node
    print "reset"
playone = []
playlist = []
for i in range(250):
    x_input_batch, y_target_batch = batch_feeder.get_next_batch(size=1)
    _y = sess.run(y, feed_dict={x: x_input_batch})
    for j in _y:
        note =1
        for k in j:
            if((k/ max_) > 0.9 ):
                if k>max_:
                    max_=k
                playone.append(note)
            note= note+1
    playlist.append(playone)
    playone=[]
print (playlist)

