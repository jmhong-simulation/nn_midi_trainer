import tensorflow as tf

x = tf.placehodler(tf.float32,[None,24 * 88])

W = tf.Variable(tf.zeros([24 * 88, 88]))
b = tf.Variable(tf.zeros[88])

y = tf.nn.softmax(tf.matmul(x,W) + b) # actual

y_ = tf.placehodler(tf.float32, [None, 88] ) # want

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(1000):
  batch_xs, batch_ys = """mnist.train.next_batch(100)"""
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})