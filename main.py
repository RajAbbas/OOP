from ndimensionalvector import Vector
from range import Range

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1:", v1)
print("v2:", v2)
print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Scalar multiplication:", v1 * 3)
print("Dot product:", v1.dot(v2))
print("Dimension of v1:", v1.dimension)

print("Iterating v1:", [x for x in v1])


print("\nTesting Range class:")
r = Range(2, 10, 2)
print("Range object:", r)
print("Length:", len(r))
print("Items via indexing:", [r[i] for i in range(len(r))])
print("Items via iteration:", [x for x in r])
