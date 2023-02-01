import numpy as np



"""
Tensor Class (datatype defaults to float32)
"""
class Tensor():
    def __init__(self, array_like):
        if isinstance(array_like, list):
            self.data = np.array(array_like, dtype=np.float32)
        elif isinstance(array_like, np.ndarray):
            self.data = array_like.astype(np.float32)


    def __matmul__(self, other):
        return self.matmul(other)
    def matmul(self, other):
        return self.data.__matmul__(other.data)
    @property
    def shape(self): return self.data.shape

    @property
    def type(self): return self.data.dtype
    @property
    def dtype(self):
        return self.type

    def __add__(self, other):
        ret = self.data + other.data
        return Tensor(ret)

    def __repr__(self):
        return f"{self.data}"

    def to_float(self, size=32):
        if size == 16:
            self.data = self.data.astype(np.float16)
        elif size == 32:
            self.data = self.data.astype(np.float32)
        elif size == 64:
            self.data = self.data.astype(np.float64)
        else:
            raise Exception(f"Data size {size} not supported for floats") 
        return self
    def to_int(self, size=32):
        if size == 32:
            self.data = self.data.astype(np.int32)
        elif size == 64:
            self.data = self.data.astype(np.int64)
        elif size == 16:
            self.data = self.data.astype(np.int16)
        elif size == 8:
            self.data = self.data.astype(np.int8)
        return self



    @classmethod 
    def randn(cls, *dims, **kwargs): return cls(np.random.randn(*dims), **kwargs)
    @classmethod
    def ones(cls, *dims, **kwargs): return cls(np.ones(dims, dtype=np.float32), **kwargs)
    @classmethod 
    def zeros(cls, *dims, **kwargs): return cls(np.zeros(dims, dtype=np.float32), **kwargs)
    @classmethod
    def eye(cls, dims, **kwargs):
        return cls(np.eye(dims, dtype=np.float32), **kwargs)
    
a = Tensor.ones(10,30)
b = Tensor.ones(30, 40)

c = a @ b
print(c.shape)

d = Tensor.randn(10,10,20)
print(d.shape)