import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops
ops.reset_default_graph()

sess = tf.Session()

identity_matrix = tf.diag([1.0,1.0,1.0])
print(sess.run(identity_matrix))

A = tf.truncated_normal([2,3])
print(sess.run(A))

B = tf.fill([2,3],5.0)
print(B)

C = tf.random_uniform([3,2])
print(sess.run(C))

D = tf.convert_to_tensor(np.array([[1.,2.,3.,],[-3.,-7.,-1.],[0.,5.,-2.]]))
print(sess.run(D))

print(sess.run(A+B))
print(sess.run(A-B))

print(sess.run(tf.matmul(B,identity_matrix)))

print(sess.run(tf.transpose(C)))

print(sess.run(tf.matrix_determinant(D)))

print(sess.run(tf.matrix_inverse(D)))

print(sess.run(tf.cholesky(identity_matrix)))

print(sess.run(tf.self_adjoint_eig(D)))

sess.close()