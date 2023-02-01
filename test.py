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
        self.grad = None
    def dot(self,other):
        self.data = np.dot(self.data, other.data)
        return self
    def __matmul__(self, other):
        return self.matmul(other)
    def matmul(self, other):
        self.data = self.data.__matmul__(other.data)
        return self
    @property
    def shape(self): return self.data.shape
    @property
    def type(self): return self.data.dtype
    @property
    def dtype(self):
        return self.type

    def __add__(self, other):
        if isinstance(other, Tensor):
            ret = self.data + other.data
        elif type(other) == "int" or type(other) == "float":
            ret = self.data + other
        return Tensor(ret)
    
    def __sub__(self,other):
        print(type(other))
        if isinstance(other, Tensor):
            ret = self.data - other.data
        elif type(other) == type(90) or type(other) == type(9.0):
            ret = self.data - other
        return Tensor(ret)
    
    def __mul__(self, other):
        if type(other) == type(1) or type(other) == type(1.0): self.data = self.data * other
        elif isinstance(other, np.ndarray): self.data =  self.data * other
        elif isinstance(other, Tensor): self.data = self.data * other.data

        return self

    def __truediv__(self, other):
        if type(other) == type(1) or type(other) == type(1.0):
            self.data = self.data / other
        elif isinstance(other, np.ndarray):
            self.data = self.data / other
        elif isinstance(other, Tensor):
            self.data = self.data / other.data
        return self
    def __floordiv__(self,other):
        return self.__truediv__(other).to_int()

    
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
    def ones_like(cls, array_like, **kwargs): return cls(np.ones_like(array_like.data if isinstance(array_like, Tensor) else array_like), **kwargs)
    @classmethod
    def zeros_like(cls, array_like, **kwargs): return cls(np.zeros_like(array_like if isinstance(array_like,Tensor) else array_like), **kwargs)
    @classmethod
    def ones(cls, *dims, **kwargs): return cls(np.ones(dims, dtype=np.float32), **kwargs)
    @classmethod 
    def zeros(cls, *dims, **kwargs): return cls(np.zeros(dims, dtype=np.float32), **kwargs)
    @classmethod
    def eye(cls, dims, **kwargs):
        return cls(np.eye(dims, dtype=np.float32), **kwargs)
    
a = Tensor.eye(10)
c = (a * 10 ) // 2
print(c)
