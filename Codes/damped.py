import matplotlib.pyplot as plt 

def f(x,y,z):
    return z

def g(x,y,z,k,b):
    m = 1
    c = (-k*y-b*z)/m
    return c

def runge_kutta( x_o, y_o, z_o, h_o, l,i,b):
    h = h_o/10  
    y = y_o  
    x = x_o  
    z = z_o  
    k = 10*i
    for j in range (0,k):
        k_1 = h*f(x,y,z)  
        l_1 = h*g(x,y,z,l,b)  
        k_2 = h*f(x+h/2,y+k_1/2,z+l_1/2)  
        l_2 = h*g(x+h/2,y+k_1/2,z+l_1/2,l,b)  
        k_3 = h*f(x+h/2,y+k_2/2,z+l_2/2)  
        l_3 = h*g(x+h/2,y+k_2/2,z+l_2/2,l,b)  
        k_4 = h*f(x+h,y+k_3,z+l_3)  
        l_4 = h*g(x+h,y+k_3,z+l_3,l,b)  
        x += h  
        y += (k_1/6 + k_2/3 + k_3/3 + k_4/6)  
        z += (l_1/6 + l_2/3 + l_3/3 + l_4/6)   
    return (x,y,z)

def damped(distance,wave,x_o,y_o,z_o,b):  
    k=1
    for i in range (0,1000):  
        h = 0.01  
        final = runge_kutta(x_o,y_o,z_o,h,k,i+1,b)
        distance.append(final[0])
        wave.append(final[1])
    

x_1 = 0
y_1 = 1
z_1 = -1
b = 2
distance=[x_1]
wave=[y_1]
derivative=[z_1]
damped(distance,wave,x_1,y_1,z_1,b)
plt.plot(distance,wave,color="red",label = "critical")
b = 1/2
distance=[x_1]
wave=[y_1]
derivative=[z_1]
damped(distance,wave,x_1,y_1,z_1,b)
plt.plot(distance,wave,color="blue",label = "under damped")
b = 3
distance=[x_1]
wave=[y_1]
derivative=[z_1]
damped(distance,wave,x_1,y_1,z_1,b)
plt.plot(distance,wave,color="green",label = "overdamped")
plt.xlabel("x")
plt.ylabel("\u03C8")
plt.legend()
plt.show()