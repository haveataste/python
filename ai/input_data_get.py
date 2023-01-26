import tensorflow as tf
import numpy as np
import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
'''
print("type of 'mnist' is %s" % (type(mnist)))
print("number of train data is %d" % (mnist.train.num_examples))
print("number of test data is %d" % (mnist.test.num_examples))
'''
