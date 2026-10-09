import numpy as np
import matplotlib.pyplot as plt

def create_object():
    # Use a parameter to create graphics
    t = np.linspace(0, 2*np.pi)
    # Full circle (face)
    x1 = np.cos(t) + 1.0
    y1 = np.sin(t) + 1.0
    # Two smaller full circles (eyes)
    x2 = np.cos(t)/10 + 0.6
    y2 = np.sin(t)/10 + 1.5
    x3 = np.cos(t)/10 + 1.4
    y3 = np.sin(t)/10 + 1.5
    # Half circle (mouth)
    x4 = np.cos(t/2)/2 + 1.0
    y4 = -np.sin(t/2)/2 + 1.0
    # Merge to create an augmented vector
    p = np.zeros((3, 200))
    p[0, :] = 5.0/2.0*np.hstack((x1, x2, x3, x4))
    p[1, :] = 5.0/2.0*np.hstack((y1, y2, y3, y4))
    p[2, :] = np.ones((1, 200))
    return p

def draw(p1, p2):
    plt.figure(figsize = (14, 7))
    plt.subplot(1, 2, 1)
    plt.plot(p1[0, :50], p1[1, :50])
    plt.fill(p1[0, 50:100], p1[1, 50:100])
    plt.fill(p1[0, 100:150], p1[1, 100:150])
    plt.fill(p1[0, 150:200], p1[1, 150:200])
    plt.axhline(0, color = 'red')
    plt.axvline(0, color = 'red')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.title('Original object')
    plt.subplot(1, 2, 2)
    plt.plot(p2[0, :50], p2[1, :50])
    plt.fill(p2[0, 50:100], p2[1, 50:100])
    plt.fill(p2[0, 100:150], p2[1, 100:150])
    plt.fill(p2[0, 150:200], p2[1, 150:200])
    plt.axhline(0, color = 'red')
    plt.axvline(0, color = 'red')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.title('Transformed object')
    plt.show()

def problem1(id):
    p = create_object()
    rng = np.random.default_rng(id)
    shift_x, shift_y = 0, 0
    while shift_x == 0 and shift_y == 0: 
        shift_x = 2.5*rng.integers(-3, 2)
        shift_y = 2.5*rng.integers(-3, 2)
    T = np.array([[1, 0, shift_x],
                  [0, 1, shift_y],
                    [0, 0, 1]])
    p2 = T @ p
    return p2

def problem2(id):
    p = create_object()
    rng = np.random.default_rng(id)
    shift_x, shift_y = 0, 0
    while shift_x == 0 and shift_y == 0:  
        shift_x = 2.5*rng.integers(-3, 2)
        shift_y = 2.5*rng.integers(-3, 2)
    T = np.array([[1, 0, shift_x],
                  [0, 1, shift_y],
                    [0, 0, 1]])
    angle = rng.integers(1, 4)*90
    theta = np.radians(angle)
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])
    p2 = R @T @ p

    return p2

def problem3(id):
    p = create_object()
    rng = np.random.default_rng(id)
    shift_x, shift_y = 0, 0
    while shift_x == 0 and shift_y == 0:
        shift_x = 2.5*rng.integers(-3, 2)
        shift_y = 2.5*rng.integers(-3, 2)
    T = np.array([[1, 0, shift_x],
                  [0, 1, shift_y],
                    [0, 0, 1]])
    angle = rng.integers(1, 4)*90
    theta = np.radians(angle)
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])
    if rng.integers(0, 2) == 0:
        s = 1.5  
    else:
        s = 0.5
    S = np.array([[s, 0, 0],
                  [0, s, 0],
                  [0, 0, 1]])
    p2 = S @ R @ T @ p

    return p2

def problem4(id):
    p = create_object()
    rng = np.random.default_rng(id)
    shift_x, shift_y = 0, 0
    while shift_x == 0 and shift_y == 0:  
        shift_x = 2.5*rng.integers(-3, 2)
        shift_y = 2.5*rng.integers(-3, 2)
    T = np.array([[1, 0, shift_x],
                  [0, 1, shift_y],
                    [0, 0, 1]])
    angle = rng.integers(1, 4)*90
    theta = np.radians(angle)
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])
    if rng.integers(0, 2) == 0:  
        s = 1.5
    else:
        s = 0.5
    S = np.array([[s, 0, 0],
                  [0, s, 0],
                  [0, 0, 1]])
    if rng.integers(0, 2) == 0:  
        sx = -1.0
    else:
        sx = 1.0
    if rng.integers(0, 2) == 0:
        sy = -1.0
    else:
        sy = 1.0
    Rf = np.array([[sx, 0, 0],
                          [0, sy, 0],
                          [0, 0, 1]])   
    p2 = Rf @ S @ R @ T @ p

    return p2

def problem5(id):

    rng = np.random.default_rng(id)
    p = move_to_center(create_object())
    shift_x, shift_y = 0, 0
    while shift_x == 0 and shift_y == 0:  
        shift_x = rng.integers(-5, 6)
        shift_y = rng.integers(-5, 6)
    T = np.array([[1, 0, shift_x],
                  [0, 1, shift_y],
                    [0, 0, 1]])
    angle = 0
    while angle == 0:  
        angle = rng.integers(-4, 5)*90
    theta = np.radians(angle)
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],    
                    [0, 0, 1]])
    if rng.integers(0, 2) == 0: 
        sx = -1.0
    else:
        sx = 1.0
    if rng.integers(0, 2) == 0:
        sy = -1.0   
    else:
        sy = 1.0
    Rf = np.array([[sx, 0, 0],
                    [0, sy, 0],
                    [0, 0, 1]])
    if rng.integers(0, 2) == 0:
        shx = np.tan(np.radians(45))  
        shy = 0.0  
    else:
        shx = 0.0  
        shy = np.tan(np.radians(45))  
    Sh = np.array([[1, shx, 0],
                   [shy, 1, 0],
                   [0, 0, 1]])
    transformations = [T, R, Rf, Sh]
    rng.shuffle(transformations)
    for transform in transformations:
        p = transform @ p
    return p   

def move_to_center(p):

    shift_x, shift_y = -1, -1
    T = np.array([[1, 0, shift_x],
                    [0, 1, shift_y],
                        [0, 0, 1]])
    p2 = T @ p
    return p2