# gradient calculating functions

import numpy as np
from ad_numpy import wrapped_types

# a and b are the 1D input vectors are c is the output scalar
# return gradients w.r.t a and b in that order
def dot_1Dx1D_grad(a, b, c, crule_grad):
    # sanity check
    assert len(shape(a)) == 1
    assert len(shape(b)) == 1
    return b * crule_grad, a * crule_grad

def dot_2Dx2D_grad(a, b, c, crule_grad):

    # sanity check
    assert len(shape(a)) == 2
    assert len(shape(b)) == 2

    ga = np.zeros_like(a)
    gb = np.zeros_like(b)

    nr = a.shape[0]
    nc = b.shape[1]

    # every row of a vs every column of b
    for i in range(nr):
        for j in range(nc):
            g_bj, g_ai = dot_1Dx1D_grad(a[i,:], b[:,j], c[i][j])

            # update gradient w.r.t the jth column of b
            gb[:,j] = gb[:,j] + g_bj
            ga[i,:] = ga[i,:] + g_ai

    return ga * crule_grad, gb * crule_grad

def dot_1Dx2D_grad(a, b, c):

    # sanity check
    assert len(shape(a)) == 1
    assert len(shape(b)) == 2

    ga = np.zeros_like(a)
    gb = np.zeros_like(b)

    nc = b.shape[1]

    # the row of a against every column of b
    for j in range(nc):
            g_bj, g_a = dot_1Dx1D_grad(a, b[:,j], c[j])

            # update gradient w.r.t the jth column of b
            gb[:,j] = gb[:,j] + g_bj
            ga = ga + g_a

    return ga * crule_grad, gb * crule_grad

def dot_2Dx1D_grad(a, b, c, crule_grad):

    # sanity check
    assert len(shape(a)) == 2
    assert len(shape(b)) == 1

    ga = np.zeros_like(a)
    gb = np.zeros_like(b)

    nr = a.shape[0]

    # every row of a vs the column b
    for i in range(nr):
        g_b, g_ai = dot_1Dx1D_grad(a[i,:], b, c[i])

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
grad_fn_mapping = {np.dot : dot_grad, np.asarray : identity_grad}
