# coding:utf-8
import tensorflow as tf

# Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2
# 为了提升CPU计算速度的。若你有支持cuda的GPU，则可以忽略这个问题，因为安装SSE4.1, SSE4.2, AVX, AVX2, FMA, 仅仅提升CPU的运算速度（大概有3倍）。
# 忽视警告，并屏蔽警告搜索
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = tf.constant('Hello, TensorFlow!')
a = tf.constant(10)
b = tf.constant(32)
with tf.Session() as sess:
    print sess.run(hello)
    print sess.run(a+b)
    print sess.run(a*b)
