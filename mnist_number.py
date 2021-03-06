# tutorial from https://www.oreilly.com/learning/not-another-mnist-tutorial-with-tensorflow

# import tensorflow as tf
# mnist = tf.keras.datasets.mnist
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
import matplotlib.pyplot as plt
import numpy as np
import random as ran

def TRAIN_SIZE(num):
    print ('Total Training Images in Dataset = ' + str(mnist.train.images.shape))
    print ('--------------------------------------------------')
    x_train = mnist.train.images[:num, :]
    print ('x_train Examples Loaded = ' + str(x_train.shape))
    y_train = mnist.train.labels[:num, :]
    print ('y_train Examples Loaded = ' + str(y_train.shape))
    print ('')
    return x_train, y_train

def TEST_SIZE(num):
    print ('Total Test Examples in Dataset = ' + str(mnist.test.images.shape))
    print ('--------------------------------------------------')
    x_test = mnist.test.images[:num, :]
    print ('x_test Examples Loaded = ' + str(x_test.shape))
    y_test = mnist.test.labels[:num, :]
    print ('y_test Examples Loaded = ' + str(y_test.shape))
    return x_test, y_test

global x_train, y_train
global x_test, y_test

def display_digit(num):
    print (y_train[num])
    label = y_train[num].argmax(axis=0)
    image = x_train[num].reshape([28, 28])
    plt.title('Example: {}  Label: {}'.format(num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.savefig('static/display_digit.png')

def display_mult_flat(start, stop):
    images = x_train[start].reshape([1, 784])
    for i in range(start+1, stop):
        images = np.concatenate((images, x_train[i].reshae([1, 784])))
    plt.imshow(images, cmap=plt.get_cmap('gray_r'))
    plt.savefig('static/display_mult_flat.png')


# this will be called publicly 
def run_with_variables(train_set_size, learning_rate, train_steps, batch_test_set_size):
    # setting variables
    x_train, y_train = TRAIN_SIZE(train_set_size)
    x_test, y_test = TEST_SIZE(batch_test_set_size)
    LEARNING_RATE = learning_rate
    TRAIN_STEPS = train_steps

    # Session creation
    sess = tf.Session()
    x = tf.placeholder(tf.float32, shape=[None, 784])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    
    # initialize variables
    init = tf.global_variables_initializer()
    sess.run(init)

    # Cross_entropy(cost) function
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

    # train with gradient descent
    print('hi~!', type(cross_entropy))
    training = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cross_entropy)
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # training loop
    for i in range(TRAIN_STEPS+1):
        sess.run(training, feed_dict={x: x_train, y_: y_train})
        if i % 100 == 0:
            print('Training Step: ' + str(i) + '  Accuracy =  ' +\
                str(sess.run(accuracy, feed_dict={x: x_test, y_: y_test})) + '  Loss = ' + \
                str(sess.run(cross_entropy, {x: x_train, y_: y_train})))

    # plotting graph
    for i in range(10):
        plt.subplot(2, 5, i+1)
        weight = sess.run(W)[:, i]
        plt.title(i)
        plt.imshow(weight.reshape([28, 28]), cmap=plt.get_cmap('seismic'))
        frame1 = plt.gca()
        frame1.axes.get_xaxis().set_visible(False)
        frame1.axes.get_yaxis().set_visible(False)
        plt.savefig('static/weights.png')


# test by random 
def display_compare(num):
    x_train = mnist.test.images[num, :].reshape(1, 784)
    y_train = mnist.test.labels[num, :]
    label = y_train.argmax()
    prediction = sess.run(y, feed_dict={x: x_train}).argmax()
    plt.title('Prediction: {}  Label: {}'.format(prediction, label))
    plt.imshow(x_train.reshape([28, 28]), cmap=plt.get_cmap('gray_r'))
    plt.savefig('static/compare.png')
