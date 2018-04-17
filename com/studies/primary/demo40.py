# import sys
# sys.path.append(r"D:/WorkSpace/IDEA_Python_Space/intelligent/com/studies/primary/tutorials/image/cifar10")
# import com.studies.primary.tutorials.image.cifar10.cifar10_input as cifar10_input
import com.studies.primary.cifar10_input as cifar10_input
import tensorflow as tf
import pylab

batch_size = 128
data_dir = 'D:/WorkSpace/data/Tensorflow_cifar10_data/cifar-10-batches-bin/'
images_test, labels_test = cifar10_input.inputs(eval_data=True,data_dir=data_dir,batch_size=batch_size)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
tf.train.start_queue_runners()
image_batch, label_batch = sess.run([images_test, labels_test])
print("__\n",image_batch[0])
print("__\n",label_batch[0])
pylab.imshow(image_batch[0])
pylab.show()
