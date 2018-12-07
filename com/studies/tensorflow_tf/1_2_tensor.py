# Tensors
# This function introduces various ways to create
# tensors in TensorFlow

import tensorflow as tf
from tensorflow.python.framework import ops
ops.reset_default_graph()

# Introduce tensors in tf
# Get graph handle
sess = tf.Session()

my_tensor = tf.zeros([1,20])

# Declare a variable
my_var = tf.Variable(tf.zeros([1,20]))

# Different kinds of variables
row_dim = 2
col_dim = 3

# Zero initialized variable
zero_var = tf.Variable(tf.zeros([row_dim,col_dim]))

# One initialized variable
ones_var = tf.Variable(tf.ones([row_dim,col_dim]))

# Shaped like other variable
sess.run(zero_var.initializer)
sess.run(ones_var.initializer)
zero_similar = tf.Variable(tf.zeros_like(zero_var))
ones_similar = tf.Variable(tf.ones_like(ones_var))

sess.run(ones_similar.initializer)
sess.run(zero_similar.initializer)

# Fill shape with a constant
fill_var = tf.Variable(tf.fill([row_dim,col_dim],-1))

# Create a variable from a constant
const_var = tf.Variable(tf.constant([8,6,7,5,3,0,9]))
# This can also be used to fill an array
const_fill_var = tf.Variable(tf.constant(-1,shape=[row_dim,col_dim]))

# Sequence generation
# Generates [0.0,0.5,10] includes the end
linear_var = tf.Variable(tf.linspace(start=0.0,stop=1.0,num=3))
# Generates [6,9,12] doesn't include the end
sequence_var = tf.Variable(tf.range(start=6,limit=15,delta=3))

# Random Numbers
# Random Normal
rnorm_var = tf.random_normal([row_dim,col_dim],mean=0.0,stddev=1.0)

# Add summaries to tensorboard
merged = tf.summary.merge_all()

# Initializer graph writer
writer = tf.summary.FileWriter("D:/WorkSpace/tensorboard/variable_logs",graph=sess.graph)

# Initialize operation
initialize_op = tf.global_variables_initializer()

# Run initialization of variable
sess.run(initialize_op)
sess.close()

'''
tensorboard --logdir=/D:/WorkSpace/tensorboard/variable_logs
http://localhost:6006/
'''