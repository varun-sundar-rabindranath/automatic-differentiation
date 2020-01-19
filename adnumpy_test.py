
import ad_numpy as anp
#from utils import rand_vectors


if __name__ == "__main__":

    #np = np_.change_numpy(np)
    #np.array = np_.change_ndarray(np.array)

    #print ("changed np.array ", np.array)

    print ("anp ndarray : ", anp.ndarray)

    anp.array.__subclasshook__ = anp.ndarray_

    #x = anp.random.rand(4, 1).view(anp.ndarray_)
    x = anp.random.rand(4, 1)

    #print(dir(np_.ndarray_))

    #x = rand_vectors(1, 4)

    print ("x ", x, " | type : ", x.__class__.__name__)

    print ("x shape ", x.shape)

    #w = rand_vectors(4, 2)
    #b = rand_vectors(1, 2)

    w = anp.random.rand(2, 4).view(anp.ndarray_)
    b = anp.random.rand(2, 1).view(anp.ndarray_)

    print ("w shape ", w.shape)

    y = anp.matmul(w, x) + b

    print ("Y shape ", y.shape)
