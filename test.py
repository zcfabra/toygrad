import numpy as np




class Tensor():
    def __init__(self, array_like):
        self.data = np.array(array_like)
        self.shape = self.data.shape
        self.type = self.data.dtype
    
    def shape(self):
        return self.shape

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
        self.type = self.data.dtype
        return self


a = Tensor([0,1,2,3,4])
print(a.type)
b = a.to_float()
print(b.type)
c = a.to_float(16)
print(c.type)