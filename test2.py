import tensorflow as tf  # now import the tensorflow module
print(tf.version.VERSION)  # make sure the version is 2.x / print(tf.__version__) 

t = tf.zeros([2, 3])  # create a tensor of zeros with shape [2, 3]

print(t.shape)  # print the shape of the tensor
print(t.dtype)  # print the data type of the tensor
print(t.numpy())  # convert the tensor to a numpy array and print it
print(t.numpy().shape)  # print the shape of the numpy array
print(t.numpy().dtype)  # print the data type of the numpy array
print(t.numpy().tolist())  # convert the numpy array to a list and print it
print(t.numpy().tolist()[0])  # print the first element of the list
print(t.numpy().tolist()[0][0])  # print the first element of the first row of the list
print(t.numpy().tolist()[0][0] == 0)  # check if the first element of the first row is 0

t = tf.reshape(t, [1, -1])
print(t)
