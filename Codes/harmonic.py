import matplotlib.pyplot as plt 
import math

def f(x,y,z):
    return z

def g(x,y,z,E):
    c = float((x**2-E)*y)
    return c

def runge_kutta( x_o, y_o, z_o, h_o, E,i):
    h = h_o/10  
    y = y_o  
    x = x_o  
    z = z_o  
    k = 10*i
    for j in range (0,k):
        k_1 = h*f(x,y,z)  
        l_1 = h*g(x,y,z,E)  
        k_2 = h*f(x+h/2,y+k_1/2,z+l_1/2)  
        l_2 = h*g(x+h/2,y+k_1/2,z+l_1/2,E)  
        k_3 = h*f(x+h/2,y+k_2/2,z+l_2/2)  
        l_3 = h*g(x+h/2,y+k_2/2,z+l_2/2,E)  
        k_4 = h*f(x+h,y+k_3,z+l_3)  
        l_4 = h*g(x+h,y+k_3,z+l_3,E)  
        x += h  
        y += (k_1/6 + k_2/3 + k_3/3 + k_4/6)  
        z += (l_1/6 + l_2/3 + l_3/3 + l_4/6)   
    return (x,y,-x)

def harmonic(x_o,y_o,z_o):  
    #let L = 4
    distance=[x_o]
    wave=[y_o]
    E = 1
    for i in range (0,400):  
        h = 0.01  
        final = runge_kutta(x_o,y_o,z_o,h,E,i+1)
        distance.append(final[0])
        wave.append(final[1])
        wave.append(final[1])
        distance.append(final[2])

    plt.plot(distance,wave,color="red")
    plt.xlabel("x")
    plt.ylabel("\u03C8")
    plt.legend()
    plt.show()

x_1 = 0
y_1 = 1
z_1 = 0
harmonic(x_1,y_1,z_1)