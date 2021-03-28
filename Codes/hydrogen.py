import matplotlib.pyplot as plt


def f(x, y, z):
    return z


def g(x, y, z, E, u, m_e):
    # l = 0 - ((l)(l+1)(pow(h,2)))/(2*u*pow(x,2)
    k = 7.6199682*m_e
    V = 14.39998/x
    A = E + V
    B = u/k
    c = (-2 * ((z / x) + A * B * y))
    return c


def runge_kutta(x_o, y_o, z_o, h_o, E, u, m_e, i):
    h = h_o/10
    y = y_o
    x = x_o
    z = z_o
    k = 10*i
    for j in range(0, k):
        k_1 = h*f(x, y, z)
        l_1 = h*g(x, y, z, E, u, m_e)
        k_2 = h*f(x+h/2, y+k_1/2, z+l_1/2)
        l_2 = h*g(x+h/2, y+k_1/2, z+l_1/2, E, u, m_e)
        k_3 = h*f(x+h/2, y+k_2/2, z+l_2/2)
        l_3 = h*g(x+h/2, y+k_2/2, z+l_2/2, E, u, m_e)
        k_4 = h*f(x+h, y+k_3, z+l_3)
        l_4 = h*g(x+h, y+k_3, z+l_3, E, u, m_e)
        x += h
        y += (k_1/6 + k_2/3 + k_3/3 + k_4/6)
        z += (l_1/6 + l_2/3 + l_3/3 + l_4/6)
    return (x, y, z)


myfile = open("R.txt", "w")
myfile1 = open("radius.txt", "w")
myfile2 = open("prob.txt", "w")
# print("Enter atom: ")
# atom = str(input())
x_o = 0.0001
y_o = pow(10, -6)
z_o = float(-1000)
m_e = 0.51101*pow(10, 6)


E = -13.6056
u = m_e

radial = [y_o]
radius = [x_o]
slope = [z_o]
prob = [(x_o*y_o)**(2)]
myfile2.write("\n")
for i in range(0, 4000):
    h = 0.001
    final = runge_kutta(x_o, y_o, z_o, h, E, u, m_e, i+1)
    radius.append(final[0])
    radial.append(final[1])
    slope.append(final[2])
    k = ((final[0]*final[1])**2)
    prob.append(k)

E = -6.803
u = m_e/2

p_radial = [y_o]
p_radius = [x_o]
p_slope = [z_o]
p_prob = [(x_o*y_o)**(2)]
myfile2.write("\n")
for i in range(0, 4000):
    h = 0.001
    final = runge_kutta(x_o, y_o, z_o, h, E, u, m_e, i+1)
    p_radius.append(final[0])
    p_radial.append(final[1])
    p_slope.append(final[2])
    k = ((final[0]*final[1])**2)
    p_prob.append(k)


# plt.plot(radius, radial, color="green", label='Hydrogen')
# plt.plot(p_radius, p_radial, color="red", label='Positronium')
# plt.xlabel("r(A*)")
# plt.ylabel("R(r)")

plt.plot(radius, prob, color="green", label='Hydrogen')
plt.plot(p_radius, p_prob, color="red", label='Positronium')
plt.xlabel("r(A*)")
plt.ylabel("(rR(r))^2")

plt.legend()
plt.show()
