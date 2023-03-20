import numpy as np
def random_point_ellipsoid(a,b,c):
    u = np.random.rand()
    v = np.random.rand()
    theta = u * 2.0 * np.pi
    phi = np.arccos(2.0 * v - 1.0)
    sinTheta = np.sin(theta);
    cosTheta = np.cos(theta);
    sinPhi = np.sin(phi);
    cosPhi = np.cos(phi);
    rx = a * sinPhi * cosTheta;
    ry = b * sinPhi * sinTheta;
    rz = c * cosPhi;
    return rx, ry, rz

x1= random_point_ellipsoid(1,1,1)
x2=random_point_ellipsoid()
print(x)