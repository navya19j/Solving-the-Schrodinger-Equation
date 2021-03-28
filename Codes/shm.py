import matplotlib.pyplot as plt 

def f(x,y,z):
    return z

def g(x,y,z,k):
    m = 1
    c = float(-k*y/m)
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
    return (x,y,z)

def harmonic(x_o,y_o,z_o):
    k=1
    time=[x_o]
    distance=[y_o]
    speed=[z_o]
    for i in range (0,2000):  
        h = 0.01
        final = runge_kutta(x_o,y_o,z_o,h,k,i+1)
        time.append(final[0])
        distance.append(final[1])
        speed.append(final[2])
    plt.plot(time,distance,color="green")
    plt.show()

x_o = 0
y_o = 0
z_o = 1
harmonic(x_o,y_o,z_o)