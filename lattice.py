from vpython import sphere, vector, color

L = 5
R = 0.3
for i in range(-L, L + 1, 2):
    for j in range(-L, L + 1, 2):
        for k in range(-L, L + 1, 2):
            sphere(pos=vector(i, j, k), radius=R, color=color.green)
for i in range(-L+1, L, 2):
    for j in range(-L+1, L, 2):
        for k in range(-L, L + 1, 2):
            sphere(pos=vector(i, j, k), radius=R, color=color.blue)
