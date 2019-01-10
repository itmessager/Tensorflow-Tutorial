"""

Dependencies:
tensorflow: 1.1.0
"""
import tensorflow as tf

# the Variable's first letter capitalized
var = tf.Variable(0)  # our first variable in the "global_variable" set

add_operation = tf.add(var, 1)
# tf.assign
update_operation = tf.assign(var, add_operation)

with tf.Session() as sess:
    # once define variables, you have to initialize them by doing this
    sess.run(tf.global_variables_initializer())  # variable needs initialize
    for _ in range(3):
        sess.run(update_operation)
        print(sess.run(var))
