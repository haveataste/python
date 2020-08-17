# coding:utf-8
import tensorflow as tf

# Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2
# 为了提升CPU计算速度的。若你有支持cuda的GPU，则可以忽略这个问题，因为安装SSE4.1, SSE4.2, AVX, AVX2, FMA, 仅仅提升CPU的运算速度（大概有3倍）。
# 忽视警告，并屏蔽警告搜索
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点加到默认图中.
# 构造器的返回值代表该常量 op 的返回值.
matrix1 = tf.constant([[3., 3.]])
# 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.constant([[2.],[2.]])
# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)
# 默认图现在有三个节点, 两个 constant() op, 和一个matmul() op. 为了真正进行矩阵相乘运算, 并得到矩阵乘法的结果, 你必须在会话里启动这个图.

# 在一个会话中启动图
# 构造阶段完成后, 才能启动图. 启动图的第一步是创建一个 Session 对象, 如果无任何创建参数, 会话构造器将启动默认图.欲了解完整的会话 API, 请阅读Session 类.
# 启动默认图.
sess = tf.Session()
# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数. 
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回矩阵乘法 op 的输出.
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
# 返回值 'result' 是一个 numpy `ndarray` 对象.
result = sess.run(product)
print result
# ==> [[ 12.]]

# 任务完成, 关闭会话.
sess.close()
# Session 对象在使用完后需要关闭以释放资源. 除了显式调用 close 外, 也可以使用 "with" 代码块 来自动完成关闭动作.
'''
with tf.Session() as sess:
  result = sess.run([product])
  print result
'''
