import numpy as np

# Four corners of a hospital treatment area: each row is [x, y]
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# Rotation angle of 45 degrees
angle = np.deg2rad(45)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

# Scale horizontally by 2 and vertically by 1.5
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combined transformation
transformation = rotation @ scale

# Transform the floor-plan coordinates
transformed_points = points @ transformation.T

print("Original hospital floor-plan points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed floor-plan points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))
