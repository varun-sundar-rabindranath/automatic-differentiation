# gradient calculating functions

import numpy as np
from ad_numpy import wrapped_types
import ad_numpy as anp

def get_grad(crule_grad, i, j):
    if np.isscalar(crule_grad):
        return crule_grad
    else:
        return crule_grad[i][j]

# a and b are the 1D input vectors are c is the output scalar
# return gradients w.r.t a and b in that order
def dot_1Dx1D_grad(a, b, c, crule_grad):
    # sanity check
    assert len(a.shape) == 1
    assert len(b.shape) == 1
    return b * crule_grad, a * crule_grad

def dot_2Dx2D_grad(a, b, c, crule_grad):

    # sanity check
    assert len(a.shape) == 2
    assert len(b.shape) == 2

    ga = np.zeros_like(a)
    gb = np.zeros_like(b)

    nr = a.shape[0]
    nc = b.shape[1]

    # every row of a vs every column of b
    for i in range(nr):
        for j in range(nc):

            g_ai, g_bj = dot_1Dx1D_grad(a[i,:], b[:,j], c[i][j], get_grad(crule_grad, i, j))

            #print ("1d array shapes ", a[i,:].shape, b[:,j].shape)
            #print ("output c shape ", c[i][j].shape)
            #print ("crule_grad ", crule_grad)
            #print ("g_ai shape ", g_ai.shape)
            #print ("g_bj shape ", g_bj.shape)

            #print ("1Dx1D ", a[i,:], b[:,j], g_ai, g_bj)

            # update gradient w.r.t the jth column of b
            gb[:,j] = gb[:,j] + g_bj
            ga[i,:] = ga[i,:] + g_ai

    return ga, gb

def dot_1Dx2D_grad(a, b, c):

    # sanity check
    assert len(a.shape) == 1
    assert len(b.shape) == 2

    ga = np.zeros_like(a)
    gb = np.zeros_like(b)

    nc = b.shape[1]

    # the row of a against every column of b
    for j in range(nc):
            g_bj, g_a = dot_1Dx1D_grad(a, b[:,j], c[j], get_grad(crule_grad, 0, j))

            # update gradient w.r.t the jth column of b
            gb[:,j] = gb[:,j] + g_bj
            ga = ga + g_a

    return ga, gb

def dot_2Dx1D_grad(a, b, c, crule_grad):

    # sanity check
    assert len(a.shape) == 2
    assert len(b.shape) == 1

    ga = np.zeros_like(a)
    gb = np.zeros_like(b)

    nr = a.shape[0]

    # every row of a vs the column b
    for i in range(nr):
        g_b, g_ai = dot_1Dx1D_grad(a[i,:], b, c[i], get_grad(crule_grad, i, 0))

        # update gradient w.r.t the jth column of b
        gb = gb + g_b
        ga[i,:] = ga[i,:] + g_ai

    return ga * crule_grad, gb * crule_grad

# return gradients w.r.t to the input a and b in that order
def dot_grad(args, kwargs, output, crule_grad):
    a = args[0]
    b = args[1]

    assert len(a.shape) <= 2 and "grad function for more dimensions not supported"
    assert len(b.shape) <= 2 and "grad function for more dimensions not supported"

    ga = None
    gb = None

    if len(a.shape) == 1 and len(b.shape) == 1:
        ga, gb = dot_1Dx1D_grad(a, b, output, crule_grad)

    if len(a.shape) == 2 and len(b.shape) == 2:
        ga, gb = dot_2Dx2D_grad(a, b, output, crule_grad)

    if len(a.shape) == 1 and len(b.shape) == 2:
        ga, gb = dot_1Dx2D_grad(a, b, output, crule_grad)

    if len(a.shape) == 2 and len(b.shape) == 1:
        ga, gb = dot_2Dx1D_grad(a, b, output, crule_grad)

    return {a.alias : ga, b.alias : gb}

def identity_grad(args, kwargs, output, crule_grad):

    ig = {}
    for arg in args:
        if type(arg) in wrapped_types.values():
            ig[arg.alias] = crule_grad
    return ig

# function - gradient function mapping
grad_fn_mapping = {"dot" : dot_grad, "asarray" : identity_grad, \
        "__add__" : identity_grad, "sum" : identity_grad,
        "rand" : identity_grad}
