import numpy as np
from decorators import *
from utils import rand_vectors

@print_args
def run_input(x, t, W1, B1, W2, B2):

    x = x.reshape(x.shape[0], 1)
    t = t.reshape(t.shape[0], 1)

    # compose network
    y1 = np.matmul(W1, x) + B1
    y2 = np.matmul(W2, y1) + B2
    # loss;
    loss = np.linalg.norm(y2 - t)

    return loss

if __name__ == "__main__":

    np.random.seed(0)

    print ("Random vectors : ", rand_vectors(2, 4))

    # inputs
    X = rand_vectors(2, 10)
    # targets
    T = rand_vectors(2, 10)

    # neural network composition
    # layer 1 with 4 nodes
    W1 = rand_vectors(2, 4)
    B1 = rand_vectors(1, 4)

    # layer 2 / output layer has 2 nodes
    W2 = rand_vectors(4, 2)
    B2 = rand_vectors(1, 2)

    # run every input against its target
    loss = 0.0
    for i in range(10):
        loss = loss + run_input(X[i], T[i], W1, B1, W2, B2)

    print ("Total loss ", loss)

