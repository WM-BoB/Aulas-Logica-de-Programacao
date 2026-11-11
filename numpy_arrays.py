import numpy

def random_array(shape):
    return numpy.random.rand(*shape)

print("Random array with shape (2, 3):\n", random_array((2, 3)))