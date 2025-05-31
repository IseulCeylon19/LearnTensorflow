import tensorflow as tf  # now import the tensorflow module
# print(tf.version)  # make sure the version is 2.x
print(tf.__version__)  # print the version of TensorFlow
print(tf.version.VERSION)

t = tf.zeros([2, 3])  # create a tensor of zeros with shape [2, 3]

print(t.shape, t.dtype)
print(t.numpy())
print(t.numpy().shape, t.numpy().dtype, t.numpy().tolist(), t.numpy().tolist()[0])

t = tf.reshape(t, [1, -1])
print(t)
