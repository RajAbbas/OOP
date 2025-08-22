class Vector:
    def __init__(self, coords):
        self._coords = list(coords)
        self.dimension = len(self._coords)
        
    def __len__(self):
        return self.dimension

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions should match for addition")
        new_coords = [self._coords[i] + other._coords[i] for i in range(self.dimension)]
        return Vector(new_coords)

    def __sub__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions must match for subtraction")
        new_coords = [self._coords[i] - other._coords[i] for i in range(self.dimension)]
        return Vector(new_coords)
#ScalarMultiplication
    def __mul__(self, scalar):
        new_coords = [x * scalar for x in self._coords]
        return Vector(new_coords)

    def __eq__(self, other):
        return self._coords == other._coords

    def __str__(self):
        return f"Vector({self._coords})"

    def get_dimension(self):
        return self.dimension

    def set_dimension(self, new_dim):
        if new_dim < self.dimension:
            self._coords = self._coords[:new_dim]
        elif new_dim > self.dimension:
            for _ in range(new_dim - self.dimension):
                self._coords.append(0)

        self.dimension = new_dim

    def dot(self, other):
        # dot product
        if self.dimension != other.dimension:
            raise ValueError("Dimensions must match for dot product")
        result = 0
        for i in range(self.dimension):
            result += self._coords[i] * other._coords[i]
        return result
    
    def cross(self, other):
        # I don't know the full logic behind cross product, 
        # but I followed the standard formula for 3D vectors
        if self.dimension != 3 or other.dimension != 3:
            raise ValueError("Cross product is only defined for 3D vectors")

        x1, y1, z1 = self._coords
        x2, y2, z2 = other._coords

        new_coords = [
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2
        ]
        return Vector(new_coords)
 
