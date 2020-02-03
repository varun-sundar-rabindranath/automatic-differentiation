import numpy as np_
from functools import wraps
from decorators import *

#class ndarray_(np.ndarray):
#    pass
#
#def change_ndarray(func):
#    @wraps(func)
#    def wrapper(*args, **kwargs):
#        return func(*args, **kwargs).view(ndarray_)
#    return wrapper
#
#def change_numpy(func):
#    @wraps(func)
#    def wrapper(*args, **kwargs):
#        return func(*args, **kwargs)
#    return wrapper

# wrapper around ndarray classes
class ndarray_(np_.ndarray):

    alias = None

    #def __new__(cls, name, bases, local):
    #    #print ("ndarray_ __new__ is called")
    #    #for attr in local:
    #    #    value = local[attr]
    #    #    if callable(value):
    #    #        print ("Value ", value)
    #    #        local[attr] = primitive(value)
    #    print ("__new__")
    #    self.wrap_attrs()
    #    return type.__new__(cls, name, bases, local)

    #def __init__(self, *args, **kwargs):
    #    print ("__init__")
    #    self.wrap_attrs()
    #    return super(self).__init__(*args, **kwargs)

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        #self.__div__ = primitive(self.__div__)
        self.__mod__ = primitive(self.__mod__)
        self.__abs__ = primitive(self.__abs__)
        self.__radd__ = primitive(self.__radd__)
        self.__rsub__ = primitive(self.__rsub__)
        self.__rmul__ = primitive(self.__rmul__)
        self.__rpow__ = primitive(self.__rpow__)
        #self.__rdiv__ = primitive(self.__rdiv__)
        self.__rmod__ = primitive(self.__rmod__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)
        self.__hash__ = primitive(self.__hash__)
        self.__truediv__ = primitive(self.__truediv__)
        self.__matmul__ = primitive(self.__matmul__)
        self.__rtruediv__ = primitive(self.__rtruediv__)
        self.__rmatmul__ = primitive(self.__rmatmul__)

        #for item in dir(self):
        #    if (item == "wrap_attrs"):
        #        continue
        #    if item.startswith("__") and callable(getattr(self, item)) and type(getattr(self, item)) is not type:
        #        setattr(self, item, primitive(getattr(self, item)))

#int8	Byte (-128 to 127)
class int8_(np_.int8):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)

#int16	Integer (-32768 to 32767)
class int16_(np_.int16):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)

#int32	Integer (-2147483648 to 2147483647)
class int32_(np_.int32):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)

#int64	Integer (-9223372036854775808 to 9223372036854775807)
class int64_(np_.int64):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        #self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)

        self.__array__ = primitive(self.__array__)
        self.__array_interface__ = primitive(self.__array_interface__)
        self.__array_priority__ = primitive(self.__array_priority__)
        self.__array_struct__ = primitive(self.__array_struct__)
        self.__array_wrap__ = primitive(self.__array_wrap__)

#uint8	Unsigned integer (0 to 255)
class uint8_(np_.uint8):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)


#uint16	Unsigned integer (0 to 65535)
class uint16_(np_.uint16):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)

#uint32	Unsigned integer (0 to 4294967295)
class uint32_(np_.uint32):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)

#uint64	Unsigned integer (0 to 18446744073709551615)
class uint64_(np_.uint64):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)


#float_	Shorthand for float64.
#float16	Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
class float16_(np_.float16):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)

#float32	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
class float32_(np_.float32):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)

#float64	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
class float64_(np_.float64):

    alias = None

    @classmethod
    def wrap_attrs(self):

        #print ("Wrapping ", self.__name__)
        self.__neg__ = primitive(self.__neg__)
        self.__add__ = primitive(self.__add__)
        self.__sub__ = primitive(self.__sub__)
        self.__mul__ = primitive(self.__mul__)
        self.__pow__ = primitive(self.__pow__)
        self.__div__ = primitive(self.__div__)
        self.__abs__ = primitive(self.__abs__)
        self.__eq__ = primitive(self.__eq__)
        self.__ne__ = primitive(self.__ne__)
        self.__gt__ = primitive(self.__gt__)
        self.__ge__ = primitive(self.__ge__)
        self.__lt__ = primitive(self.__lt__)
        self.__le__ = primitive(self.__le__)

# wrapped types
wrapped_types = {np_.ndarray : ndarray_, np_.int8 : int8_, np_.int16 : int16_, np_.int32 : int32_, np_.int64 : int64_, np_.uint8 : uint8_, np_.uint16 : uint16_, np_.uint32 : uint32_, np_.uint64 : uint64_, np_.float16 : float16_, np_.float32 : float32_, np_.float64 : float64_}
scalar_wrapper_types = {np_.int8 : int8_, np_.int16 : int16_, np_.int32 : int32_, np_.int64 : int64_, np_.uint8 : uint8_, np_.uint16 : uint16_, np_.uint32 : uint32_, np_.uint64 : uint64_, np_.float16 : float16_, np_.float32 : float32_, np_.float64 : float64_}

for name, obj in np_.__dict__.items():

    # wrap all values
    if callable(obj) and type(obj) is not type:
        globals()[name] = primitive(obj)
    else:
        globals()[name] = obj

#globals()['ndarray'] = ndarray_
