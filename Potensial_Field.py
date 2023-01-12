import numpy as np

# potansiyel alanı tanımlama
def potential_field(x, y, goal_x, goal_y):
    return np.sqrt((goal_x - x)**2 + (goal_y - y)**2)

# engel alanı tanımlama
def obstacle_field(x, y, obstacle_x, obstacle_y, obstacle_radius):
    return np.maximum(np.sqrt((obstacle_x - x)**2 + (obstacle_y - y)**2) - obstacle_radius, 0)

