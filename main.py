import numpy as np

from Connect import Connect
from macar import  Macar_algorithm


Connect1 = Connect()

mached = Macar_algorithm()


points1 = np.array([[-1, 0, 1], [0, 0, 1], [1, 0, 1], [-1, 0, 0], [0, 0, 0]])
points2 = np.array([[0, 10, 0], [8, 10, 0], [8, 10, 6], [0, 10, 6], [4, 22, 3]])

mached.matches(points1,points2)
