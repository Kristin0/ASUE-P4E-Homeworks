class Vector3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, vec):
        if isinstance(vec, int):
            return Vector3D(self.x + vec, self.y + vec, self.z + vec)
        return Vector3D(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __sub__(self, vec):
        if isinstance(vec, int):
            return Vector3D(self.x - vec, self.y - vec, self.z - vec)
        return Vector3D(self.x - vec.x, self.y - vec.y, self.z - vec.z)

    def dot_product(self, vec):
        return (self.x * vec.x + self.y * vec.y + self.z * vec.z)
     
    def scalar_mul(self, sc):
        return Vector3D(self.x * sc, self.y * sc, self.z * sc)
     
    def norm_eu(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def vec_mul(self, vec):
        return Vector3D(self.x * vec.y - self.y * vec.x, 
                self.z * vec. x - self.x * vec.z, self.y * vec.z - self.z *
                vec.y)
    
    def __str__(self):
        return f'[{self.x}, {self.y}, {self.z}]'


v1 = Vector3D(1,2,3)
v2 = Vector3D(3,2,1)
v3 = v1 + v2
print(str(v3))

v4 = v1.scalar_mul(3)
print(str(v4))

c = v1.dot_product(v2)
print(c)

c3 = v1.norm_eu()
print(round(c3, 3))
