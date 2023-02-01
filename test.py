import numpy as np




class Tensor():
    def __init__(self, array_like):
        self.data = np.array(array_like)
        self.shape = self.data.shape
        self.type = self.data.dtype
    
    def shape(self):
        return self.shape

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
        self.type = self.data.dtype
        return self
    


a = Tensor([0,1,2,3,4])
print(a.type)
b = a.to_float()
print(b.type)
c = a.to_float(16)
print(c.type)


a = Tensor([1,2,3,4,5])
b = Tensor([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
c = a + b 
print(c.shape)
print(c)