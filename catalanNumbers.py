#Created by SHADOWMALICE
#Catalan Numbers

n, c0 = 0, 1
while c0 <= 1e9:
    print(c0)
    c1 = (4*n+2)/(n+2)*c0
    c0, c1 = c1, (4*n+2)/(n+2)*c0
    n += 1



