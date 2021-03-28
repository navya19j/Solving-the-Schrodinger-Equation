# Solution Of Schrodinger Equation For Hydrogen and Positronium Atoms

![picture alt](./images/iitd.png)
## Indian Institute Of Technology, Delhi

### CLL-113

### Numerical Methods In Chemical Engineering

---

### **Abstract:**

This paper has described the Schrodinger wave equation for the hydrogen and positronium atom.  Using the Runge-Kutta method of order 4, this was solved.  The numerical outcomes were discussed along with the graphs of probability and radial wave-function. The oscillator of quantum harmonic and infinite potential well have also been addressed well. Their energy eigenstates and wave functions have been obtained using the Runge-Kutta method of order 4. All the findings acquired   from the numerical approach are accurate in comparison to the analytical solutions. The Schrodinger equation is an integral part of quantum mechanics, and the RK4 method helps us in solving it in a more efficient manner.

---

### **Introduction:**

$$-\frac{\hbar^{2}}{2 m} \nabla^{2} \psi(\mathbf{r})+V(\mathbf{r})=E \psi(\mathbf{r})
\\\int_{-\infty}^{+\infty} \Psi^{*}(\mathrm{x}) \Psi(\mathrm{x}) \mathrm{d} \mathrm{x}=1$$

This paper is concerned with the numerical solutions of the radial Schrodinger wave equation for the hydrogen and positronium atoms using the Runge-Kutta method. Schrodinger equation is an important quantum mechanical equation yielding wave functions as its solution. It rarely becomes possible to solve this equation analytically; the Runge Kutta method is thus discussed in this paper to provide accurate numerical methods to such equations where no analytical counterpart exists.
The Runge-Kutta method of order 4 is a method of numerical integration based on the formalism of Euler , but with better precis to solve initial value problems.
As an extension, this approach is also discussed for two other quantum mechanical systems: the infinite potential well and the quantum harmonic oscillator to attain their energy eigenstates and corresponding wave functions from the Schrodinger equation. 
Harmonic oscillators often occur in classical mechanics, a pendulum (with small displacements), spring-mass systems, and electric current flow in a circuit, being a few examples. As an extension, these mechanical systems: the simple harmonic oscillator and damped free harmonic oscillator with no damping, are also discussed numerically using the RK4 method in the paper.

---

### Problem Formulation**:**

- **Assumptions:**

For hydrogen, reduced mass is defined as: 

$$\mu=\frac{\mathrm{m}_{\mathrm{p}} \mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{p}}+\mathrm{m}_{\mathrm{e}}}$$

Here, on dividing *u* by *mp:*

$$\mu=\frac{m_{e}}{1+m_{e} / m_{p}}$$

For this, the assumption is:

$$\frac{m_{e}}{m_{p}} \sim 0$$

For ease of calculations, another assumption for infinite potential well is:

$$\begin{array}{c}
\left.\left(\hbar^{2} / 2 m\right)=1\right.
\end{array}$$

---

- **Equations Used and Boundary Conditions:**
    - **Schrodinger Equation:**

        $$\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial \psi}{\partial r}\right)+\frac{1}{r^{2} \sin \theta} \frac{\partial}{\partial \theta}\left(\sin \theta \frac{\partial \psi}{\partial \theta}\right)+\frac{1}{r^{2} \sin ^{2} \theta} \frac{\partial^{2} \psi}{\partial \phi^{2}}+\frac{2 m}{\hbar^{2}}(E-U) \psi=0$$

    - **Schrodinger Equation for Radial Part:**

        $$\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}+\frac{2}{\mathrm{r}} \frac{\mathrm{d}}{\mathrm{dr}}\right] \mathrm{R}(\mathrm{r})+\frac{2 \mu}{\hbar^{2}}\left[\mathrm{E}+\mathrm{V}(\mathrm{r})-\frac{l(l+1) \hbar^{2}}{2 \mu \mathrm{r}^{2}}\right] \mathrm{R}(\mathrm{r})=0$$

        - **Initial Values for Radial Part:**

        $$\left.R(r)\right|_{r=10^{-4}}=10^{-6},\left.\frac{d R}{d r}\right|_{r=10^{-4}}=-1000$$

    ---

    - **Schrodinger Equation for Angular Part:**

        $$\frac{\sin ^{2} \theta}{R} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial R}{\partial r}\right)+\frac{\sin \theta}{\Theta} \frac{\partial}{\partial \theta}\left(\sin \theta \frac{\partial \Theta}{\partial \theta}\right)+\frac{2 m r^{2} \sin ^{2} \theta}{\hbar^{2}}\left(\frac{Z e^{2}}{4 \pi \epsilon_{0} r}+E\right)=-\frac{1}{\Phi} \frac{\partial^{2} \Phi}{\partial \phi^{2}}$$

        - **Initial Values for Angular Part:**

        $$\theta=\pi/6\\\\\Theta=1.69929\\\\\frac{d \Theta}{d \theta}=0.97745$$

        ---

    - **Equation for Infinite Well:**

        $$\frac{d^{2}}{d x} \psi(x)=\frac{-2 m_{e} E}{\hbar^{2}} \cdot \psi(x)$$

        - **Boundary conditions for Infinite Well:**

        $$\psi(0)=1, \frac{d \psi(0)}{d x}=0, \psi(0)=0, \frac{d \psi(0)}{d x}=1
        \\\psi(x \rightarrow-\infty)=0, \psi(x \rightarrow \infty)=0$$

        ---

    - **Equation for Harmonic Oscillator:**

        $$\frac{-\hbar}{2 m} \frac{d^{2}}{d x^{2}} \psi(x)+\frac{m \omega^{2}}{2} x^{2} \psi(x)=E \psi(x)$$

        - **Boundary conditions for Harmonic Oscillator:**

        $$\psi(-L / 2)=0, \psi(+L / 2)=0, E>0,  V(x=-L/2)=\infty, V(x=L/2)=\infty$$

    ---

    - **Equation for  Simple Harmonic Oscillator (Classical Model)**

        $$\begin{array}{l}m y^{\prime \prime}+k y=0 \\\end{array}$$

        - **Boundary conditions for  Simple Harmonic Oscillator(Classical Model):**

        $$\\y(0)=0, \quad y^{\prime}(0)=1$$

    ---

    - **Equation for  Damped Harmonic Oscillator (Classical Model)**

        $$m y^{\prime \prime}(t)+\gamma y^{\prime}(t)+k y(t)=0$$

        - **Boundary conditions for  Simple Harmonic Oscillator(Classical Model):**

        $$\\y(0)=1, \quad y^{\prime}(0)=-1$$

        ---

- **Derivation of 4th order Runge-Kutta:**

Runge-Kutta is a method that is widely used to solve differential problems whose initial values are given. It is  a very efficient method as it does not require us to calculate the higher order derivatives of the function and solves the problems with high accuracy. There are Runge-Kutta methods that go upto the 10th order, but the most frequently used are the methods from order 1-5. We have more scope we have to increase the step size while maintaining the accuracy for higher order RK methods.

The derivation of Runge Kutta is based on Taylor series expansion which is written as:

$$y_{n+1}=y_{n}+h f_{n}+\frac{1}{2} h^{2}\left(\frac{d f}{d x}\right)_{n}+\cdots+\frac{1}{p !} h^{p}\left(\frac{d^{p-1} f}{d x^{p-1}}\right)_{n}+O\left(h^{p+1}\right)$$

For 4th order equation,  first four terms of Taylor series are used:

$$y_{i+1}=y_{i}+f\left(x_{i}, y_{i}\right) h+\frac{1}{2 !} f^{\prime}\left(x_{i}, y_{i}\right) h^{2}+\frac{1}{3 !} f^{\prime \prime}\left(x_{i}, y_{i}\right) h^{3}+\frac{1}{4 !} f^{\prime \prime \prime}\left(x_{i}, y_{i}\right) h^{4}$$

The Runge Kutta  Equation for a general '*s'* order can be written as:

$$y_{t+h}=y_{t}+h \cdot \sum_{i=1}^{s} a_{i} k_{i}+\mathcal{O}\left(h^{s+1}\right)$$

where increments for *y* at *i*-th order are:

$$k_{i}=y_{t}+h \cdot \sum_{j=1}^{s} \beta_{i j} f\left(k_{j}, t_{n}+\alpha_{i} h\right)$$

Here, the values of the constants are chosen as:

$$\begin{array}{r}\alpha_{i} \\\alpha_{1}=0 \\\alpha_{2}=\frac{1}{2} \\\alpha_{3}=\frac{1}{2} \\\alpha_{4}=1\end{array}$$

$$\begin{array}{r}\beta_{i j} \\\beta_{21}=\frac{1}{2} \\\beta_{32}=\frac{1}{2} \\\beta_{43}=1\end{array}$$

*y* can be defined **as:

$$\begin{array}{c}y_{t+h}^{1}=y_{t}+h f\left(y_{t}, t\right) \\y_{t+h}^{2}=y_{t}+h f\left(y_{t+h / 2}^{1}, t+\frac{h}{2}\right) \\y_{t+h}^{3}=y_{t}+h f\left(y_{t+h / 2}^{2}, t+\frac{h}{2}\right) \\\text { where } y_{t, h / 2}^{1}=\frac{y_{t}+y_{t+h}^{1}}{2} \text { and } y_{t+h / 2}^{2}=\frac{y_{t}+y_{t+h}^{2}}{2}\end{array}$$

*k* can be defined as:

$$k_{1}=f\left(y_{t}, t\right)$$

$$\begin{aligned}k_{2} &=f\left(y_{t+h / 2}^{1}, t+\frac{h}{2}\right)=f\left(y_{t}+\frac{h}{2} k_{1}, t+\frac{h}{2}\right) \\&=f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right) \\k_{3} &=f\left(y_{t+h / 2}^{2}, t+\frac{h}{2}\right)=f\left(y_{t}+\frac{h}{2} f\left(y_{t}+\frac{h}{2} k_{1}, t+\frac{h}{2}\right), t+\frac{h}{2}\right) \\&=f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right] \\k_{4} &=f\left(y_{t+h}^{3}, t+h\right)=f\left(y_{t}+h f\left(y_{t}+\frac{h}{2} k_{2}, t+\frac{h}{2}\right), t+h\right) \\&=f\left(y_{t}+h f\left(y_{t}+\frac{h}{2} f\left(y_{t}+\frac{h}{2} f\left(y_{t}, t\right), t+\frac{h}{2}\right), t+\frac{h}{2}\right), t+h\right) \\&=f\left(y_{t}, t\right)+h \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right]\right]\end{aligned}$$

Hence, substituting *k* in *y* gives:

$$ 
\begin{aligned}y_{t+h}=& y_{t}+h\left\{a \cdot f\left(y_{t}, t\right)+b \cdot\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right]+\right.\\&+c \cdot\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right]\right]+\\&\left.+d \cdot\left[f\left(y_{t}, t\right)+h \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right]\right]\right]\right\}+\mathcal{O}\left(h^{5}\right) \\=& y_{t}+a \cdot h f_{t}+b \cdot h f_{t}+b \cdot \frac{h^{2}}{2} \frac{d f_{t}}{d t}+c \cdot h f_{t}+c \cdot \frac{h^{2}}{2} \frac{d f_{t}}{d t}+\\&+c \cdot \frac{h^{3}}{4} \frac{d^{2} f_{t}}{d t^{2}}+d \cdot h f_{t}+d \cdot h^{2} \frac{d f_{t}}{d t}+d \cdot \frac{h^{3}}{2} \frac{d^{2} f_{t}}{d t^{2}}+d \cdot \frac{h^{4}}{4} \frac{d^{3} f_{t}}{d t^{3}}+\mathcal{O}\left(h^{5}\right)\end{aligned}$$

Comparing the above equation to Taylor's series expansion for first four terms:

$$\left\{\begin{array}{l}a+b+c+d=1 \\\frac{1}{2} b+\frac{1}{2} c+d=\frac{1}{2} \\\frac{1}{4} c+\frac{1}{2} d=\frac{1}{6} \\\frac{1}{4} d=\frac{1}{24}\end{array}\right.$$

$$a=\frac{1}{6}, b=\frac{1}{3}, c=\frac{1}{3}, d=\frac{1}{6}$$

which gives the final result as:

$$y_{i+1}=y_{i}+\frac{1}{6}\left(k_{1}+2 k_{2}+2 k_{3}+k_{4}\right) h$$

where:

$$\begin{aligned}k_{1} &=f\left(x_{i}, y_{i}\right) \\k_{2} &=f\left(x_{i}+\frac{1}{2}, y_{i}+\frac{1}{2} k_{1} h\right) \\k_{3} &=f\left(x_{i}+\frac{1}{2}, y_{i}+\frac{1}{2} k_{2} h\right) \\k_{4} &=f\left(x_{i}+h, y_{i}+k_{3} h\right)\end{aligned}$$

---

### **Numerical Analysis:**

- **Numerical Analysis of  Radial Schrodinger Equation:**

The final formulas for a fourth order Runge-Kutta equation are:

$$\begin{aligned}\Delta y^{(1)} &=h f\left(x_{i}, y_{i}, z_{i}\right) \\\Delta z^{(1)} &=h g\left(x_{i}, y_{i}, z_{i}\right) \\\Delta y^{(2)} &=h f\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{1}}{2}, z_{i}+\frac{\Delta z^{1}}{2}\right) \\\Delta z^{(2)} &=h g\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{1}}{2}, z_{i}+\frac{\Delta z^{1}}{2}\right) \\\Delta y^{(3)} &=h f\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{2}}{2}, z_{i}+\frac{\Delta z^{2}}{2}\right) \\\Delta z^{(3)} &=h g\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{2}}{2}, z_{i}+\frac{\Delta z^{2}}{2}\right) \\\Delta y^{(4)} &=h f\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{3}}{2}, z_{i}+\frac{\Delta z^{3}}{2}\right) \\\Delta z^{(4)} &=h g\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{3}}{2}, z_{i}+\frac{\Delta z^{3}}{2}\right)\end{aligned}$$

$$\text where, h=\frac{x_{n}-x_{0}}{n}$$

The incrementation done after  each iteration is as follows:

$$x_{i}=a+i h$$

$$\begin{array}{l}y_{i+1}=y_{i}+\frac{1}{6}\left(\Delta y^{(1)}+2 \Delta y^{(2)}+2 \Delta y^{(3)}+\Delta y^{(4)}\right) +O(h^{5}) \\z_{i+1}=z_{i}+\frac{1}{6}\left(\Delta z^{(1)}+2 \Delta z^{(2)}+2 \Delta z^{(3)}+\Delta z^{(4)}\right)+O(h^{5})\end{array}$$

The application of the above formulas in the Schrodinger equation is done as given below.

$$\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}+\frac{2}{\mathrm{r}} \frac{\mathrm{d}}{\mathrm{dr}}\right] \mathrm{R}(\mathrm{r})+\frac{2 \mu}{\hbar^{2}}\left[\mathrm{E}+\mathrm{V}(\mathrm{r})-\frac{l(l+1) \hbar^{2}}{2 \mu \mathrm{r}^{2}}\right] \mathrm{R}(\mathrm{r})=0$$

$$\frac{d R}{d r}=z$$

$$\frac{d z}{d r}=\frac{d^{2} R}{d r^{2}}$$

The above equations are then simplified to:

$$\\{r} = x
\\{R} = y
\\\frac{d R}{d r}=z $$

$$\frac{d y}{d x}=z=f(x, y, z) \\\frac{d z}{d x}=-\frac{2 z}{x}-\frac{2 A \mu}{\hbar^{2}} y=g(x, y, z)$$

where  

$$A = \left[\mathrm{E}+\mathrm{V}(\mathrm{r})-\frac{l(l+1) \hbar^{2}}{2 \mu \mathrm{r}^{2}}\right]$$

$$\begin{array}{l}
k_{1}=h f\left(x_{0}, y_{0}, z_{0}\right) \\
l_{1}=h g\left(x_{0}, y_{0}, z_{0}\right) \\
k_{2}=h f\left(x_{0}+\frac{h}{2}, y_{0}+\frac{k_{1}}{2}, z_{0}+\frac{l_{1}}{2}\right) \\
l_{2}=h g\left(x_{0}+\frac{h}{2}, y_{0}+\frac{k_{1}}{2}, z_{0}+\frac{l_{1}}{2}\right) \\
k_{3}=hf\left(x_{0}+\frac{h}{2}, y_{0}+\frac{k_{2}}{2}, z_{0}+\frac{l_{2}}{2}\right) \\
l_{3}=hg \left(x_{0}+\frac{h}{2}, y_{0}+\frac{k_{2}}{2}, z_{0}+\frac{l_{2}}{2}\right) \\
x_{4}=h f\left(x_{0}+h, y_{0}+k_{3}, z_{0}+l_{3}\right)\\
l_{4}=hg \left(x_{0}+{h}, y_{0}+k_{3}, z_{0}+l_{3}\right) \\
\end{array}$$

The initial values taken are:

$$\left.R(r)\right|_{r=10^{-4}}=10^{-6},\left.\frac{d R}{d r}\right|_{r=10^{-4}}=-1000$$

$$\left.y\right|_{x=10^{-4}}=10^{-6},\left.z\right|_{x=10^{-4}}=-1000$$

The standard values taken were:

$$\hbar^{2}=7.6199682 \mathrm{~m}_{e} \mathrm{eV} . \mathrm{A}^{\circ 2}$$

$$\mathrm{V}(\mathrm{r})=\frac{\mathrm{e}^{2}}{4 \pi \varepsilon_{\mathrm{o}} \mathrm{r}}$$

$$\frac{e^{2}}{4 \pi \varepsilon_{0}}=14.39998 \mathrm{eV} \cdot \mathrm{A}^{\circ}$$

$$\mu=\frac{\mathrm{m}_{\mathrm{p}} \mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{p}}+\mathrm{m}_{\mathrm{e}}} \text { for hydrogen atom }$$

$$\mu=\frac{\mathrm{m}_{\mathrm{e}} \mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{e}}+\mathrm{m}_{\mathrm{e}}}=\frac{\mathrm{m}_{\mathrm{e}}}{2} \text { for positronium atom }$$

$$\mathrm{m}_{\mathrm{e}} \mathrm{c}^{2}=0.51101 \times 10^{6} \mathrm{eV}$$

---

- **Numerical Analysis for Angular Schrodinger Equation:**

The Schrodinger wave equation can be further written as:

$$\psi(r, \theta, \phi)=R(r) \Theta(\theta) \Phi(\phi)$$

Substituting the above expression and the potential into the spherical polar representation of the wave equation, we find, after some manipulation:

$$\frac{\sin ^{2} \theta}{R} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial R}{\partial r}\right)+\frac{\sin \theta}{\Theta} \frac{\partial}{\partial \theta}\left(\sin \theta \frac{\partial \Theta}{\partial \theta}\right)+\frac{2 m r^{2} \sin ^{2} \theta}{\hbar^{2}}\left(\frac{Z e^{2}}{4 \pi \epsilon_{0} r}+E\right)=-\frac{1}{\Phi} \frac{\partial^{2} \Phi}{\partial \phi^{2}}$$

which on further solving, can be reduced into equations dependent on theta and phi respectively as:

$$\frac{1}{\sin \theta} \frac{d}{d \theta}\left(\sin \theta \frac{d \Theta}{d \theta}\right)+\left[l(l+1)-\frac{m_{l}^{2}}{\sin ^{2} \theta}\right] \Theta=0$$

$$\frac{d^{2} \Phi}{d \phi^{2}}-m_{l}^{2} \Phi=0$$

Solving these two equations analytically gives us the solution as shown below:

$$\begin{array}{lll}\ell & m_{\ell} & Y_{\ell m_{l}}(\theta, \phi)=\Theta_{\ell m_{l}}(\theta) \Phi_{m_{l}}(\phi) \\0 & 0 & (1 / 4 \pi)^{1 / 2} \\1 & 0 & (3 / 4 \pi)^{1 / 2} \cos \theta \\1 & \pm 1 & \mp(3 / 8 \pi)^{1 / 2} \sin \theta e^{\pm i \phi} \\2 & 0 & (5 / 16 \pi)^{1 / 2}\left(3 \cos ^{2} \theta-1\right) \\2 & \pm 1 & \mp(15 / 8 \pi)^{1 / 2} \sin \theta \cos \theta e^{\pm i \phi} \\2 & \pm 2 & (15 / 32 \pi)^{1 / 2} \sin ^{2} \theta e^{\pm 2 i \phi}\end{array}$$

In this term paper, the angular part of the Schrodinger wave function is numerically calculated for the p(z) orbital, using the RK4 method. The IVP solved for such a system is :- 

$$\theta=x
\\\Theta=y
$$

$$\frac{dy}{d x}=z=f(x, y, z) \\\frac{d z}{dx}=-{2 y}-{z}*{cotx} =g(x, y, z)$$

The  initial values taken were:

$$\theta=\pi/6\\\\\Theta=1.69929\\\\\frac{d \Theta}{d \theta}=0.97745$$

---

- **Numerical Analysis for Infinite Potential Well problem:**

A particle is trapped between two regions of infinite potential. The wave function outside the well is zero and it does not jump at it's boundaries.  The Schrodinger equation for such a system is as follows.:-

$$\frac{d^{2}}{d x} \psi(x)=\frac{-2 m_{e} E}{\hbar^{2}} \cdot \psi(x)$$

For ease of calculations,

$$\begin{array}{c}
\text { Let } \left.\left((\hbar^{2} / 2 m\right)=1\right)
\end{array}$$

$$\frac{d^{2} \psi}{d x^{2}}=-E \psi$$

Boundary conditions:-

$$\psi(-L / 2)=0, \psi(+L / 2)=0, E>0$$

$$V(x=-L/2)=\infty, V(x=L/2)=\infty$$

Since it is known that the solution to such a problem is symmetrical about the origin, it can be assumed that the wave functions assume the form of a sine or cosine curve, therefore 2 boundary conditions arise:

$$\psi(0)=1, \frac{d \psi(0)}{d x}=0$$

$$\psi(0)=0, \frac{d \psi(0)}{d x}=1$$

---

- **Numerical Analysis for Quantum Harmonic Oscillator:**

$$\begin{array}{c}\nu=\frac{\omega_{0}}{2 \pi} \\E=\hbar \omega_{0}\left(n+\frac{1}{2}\right) \\\omega=\sqrt{\frac{k}{m}}\end{array}$$

$$V(x)=\frac{1}{2} k x^{2}=\frac{1}{2} m(\omega x)^{2}$$

$$\frac{-\hbar}{2 m} \frac{d^{2}}{d x^{2}} \psi(x)+\frac{m \omega^{2}}{2} x^{2} \psi(x)=E \psi(x)$$

$$\psi(x \rightarrow-\infty)=0, \psi(x \rightarrow \infty)=0$$

$$E=\hbar \omega_{0}\left(n+\frac{1}{2}\right), n=0,1,2 \ldots$$

$$a=\sqrt{\frac{\hbar}{m_{e} \omega}}$$

$$y=\frac{x}{a}=\frac{x}{\sqrt{\frac{\hbar}{m \omega}}}$$

$$\hat{E}=\frac{2 E}{\hbar \omega}$$

$$\frac{d^{2}}{d y^{2}} \Psi(y)+y^{2} \Psi(y)=\hat{E} \Psi(y)$$

$$\begin{array}{l}\Psi^{\prime}(y)=\Phi \\\Phi^{\prime}(y)=\left(\hat{E}-y^{2}\right) \Psi\end{array}$$

Solving the Schrodinger wave equation for simple harmonic oscillator, gives us the function that is proportional to x*e^-x^2, and the graph obtained by the RK4 method also shows such trend where it is 0 at x=0, and then it oscillates around it.  This graph which is obtained from the numerical method aligns with the analytical solution .

---

- **Numerical Analysis for Simple Harmonic Oscillator (Classical Model):**

$$\begin{array}{l}m y^{\prime \prime}+k y=0 \\y(0)=0, \quad y^{\prime}(0)=1\end{array}$$

$$y=A \sin \left(\omega_{0} t+\delta\right)$$

$$z^{\prime}(t)=f(t, z(t))$$

$$z^{\prime}=\left[\begin{array}{l}z_{1} \\z_{2}\end{array}\right]^{\prime}=\left[\begin{array}{c}z_{2} \\\frac{-k}{m} z_{1}\end{array}\right]=f(z)$$

---

- **Numerical Analysis for Damped Harmonic Oscillator (Classical Model):**

Solving the equation for Damped Oscillation gives us:

$$
\begin{array}{l}m y^{\prime \prime}(t)+\gamma y^{\prime}(t)+k y(t)=0\\y(0)=1, \quad y^{\prime}(0)=-1\end{array}$$

The roots of the characteristic equation are:

$$r_{1}, r_{2}=\frac{-\gamma \pm \sqrt{\gamma^{2}-4 k m}}{2 m}$$

$$1. \text Over Damped: \ \ \ \gamma^{2}>4 k m, where\ \  \gamma = 3\ \  for \ \ m = 1 kg$$

where the general solution is:

$$y(t)=c_{1} e^{r_{1} t}+c_{2} e^{r_{2} t}$$

$$2. Critically Damped: \ \ \ \gamma^{2}=4 k m, where\ \  \gamma = 2 \  for \ \ m = 1 kg$$

where the general solution is:

$$y(t)=c_{1} e^{\gamma t / 2 m}+c_{2} t e^{\gamma t / 2 m}$$

$$3. Under Damped: \ \ \ \gamma^{2}< 4 k m, where\ \  \gamma = 1/2\ \  for  \ \ m = 1 kg$$

where the general solution is:

$$\begin{aligned}y(t) &=e^{-\gamma t / 2 m}\left[c_{1} \cos (\mu t)+c_{2} \sin (\mu t)\right] \\&=R e^{-\gamma t / 2 m} \sin (\mu t+\delta)\end{aligned}$$

---

### **Results:**

- **Result for  Radial Schrodinger Equation:**

$$\mathrm{V}(\mathrm{r})=\frac{\mathrm{e}^{2}}{4 \pi \varepsilon_{\mathrm{o}} \mathrm{r}}$$

According to the formula, potential energy is inversely proportional to *r* which leads the potential to infinity at small values of *r*. Based on this,  the initial value of *r* can be assumed as *10^-4*. As the value of *r* increases, the graph shows a drastic change in the values of the wave function, and this tells us about the rate of change of the wave function with respect to *r* i.e. the derivative to have a high value, which we have here taken as -1000. Then using trial and error, we calculate the value of initial energy for which the wave function comes out to be convergent. The initial energy value obtained for the ground state of hydrogen, i.e. l=0, is -13.6506eV and for the positronium atom, the value is -6.803eV. These values are consistent with those obtained by analytical calculations in quantum mechanics and modern physics.

![picture alt](./images/Untitled.png)

Probability wave function obtained from the Runge Kutta method for the ground state wave function of hydrogen and positronium atom.

![picture alt](./images/Radial.jpeg)

Radial wave function obtained from the Runge Kutta method for the ground state wave function of hydrogen and positronium atom.

The graphs obtained by the numerical method are consistent with those obtained using analytical methods. In the probability wave function graph, we can observe that the probability increases as we move further away from the nucleus, hits maximum at a point, and then starts decreasing. This is in line with the analytical observations which state that the probability density of an electron is very low when it is extremely close to the nucleus, is maximum at a certain distance, and decreases after that.  

The radial wave function is proportional to *r**e^-k*r* where k is a constant and that is also observed from the graph as at r=0, the function value is 0 and as we move away from the nucleus, it grows exponentially and then tends to a constant value zero at large values of r as e^-k*r* becomes very small.

---

- **Results for Angular Schrodinger Equation:**

Polar angle ranges from 0 to $pi$.

![picture alt](./images/angular.png)

Angular wave function plot for wave orbital p(z) i.e. l=1 and m=0

The hydrogen 'p' orbitals correspond to $l =1$ and in such a system $m_{l}$  takes values -1,0,1. In this research paper, angular wave plot has been numerically calculated for  $m_l =0$ i.e. the $p_z$ orbital.  The 2-D angular plot obtained through numerical analysis closely resembles the cross-section of a $p$ orbital.  Since, the wave function is symmetrical about the azimuthal angle, rotating the above 2-dimensional plot about the (0-180) axis of symmetry, generates the analytically calculated dumbbell shaped p orbital.

The above numerically generated plot also guarantees the proportionality of the angular wave function to cosine of the polar angle, which is in agreement with the analytically obtained values of the Legendre polynomial for $p_z$. The plot also proves the existence of 1 nodal plane (90-270 ) in the plane.

---

- **Results for Infinite Potential Well:**

![picture alt](./images/odd_soln.png)

Wave function for Odd Solution

![picture alt](./images/even_soln.png)

Wave Function for Even solution

![picture alt](./images/Untitled1.png)

Potential Diagram for a particle in a box

In an infinite well, the wave function exists from -L/2 to L/2 as the potential is infinite outside those boundaries. Solving the equation of the wave function by applying boundary conditions tells us that it is a sine or cosine wave. This can be observed in the graphs obtained by solving the infinite well problem using the RK4 method. The odd solution represents the curve of a sine wave whereas the even solution represents the solution of a cosine wave.

The energy eigen value for such a wave function is observed at E = 5.0. 

**Calculation of  Energy Eigen value:**

To calculate the Energy value, the loop for the calculation of wave solutions is started with an energy value of 0. The value of energy is incremented with a step size of 5.0. The algorithm terminates as soon as the value of the wave function state at L/2 reaches 10^(-5)  thereby being close to zero and satisfying the boundary equations for the Schrodinger equation. This value is used to calculate the wave function using the Runge Kutta implementation.

---

- **Results for Quantum Harmonic Oscillator:**

![picture alt](./images/harmonic_quantum.png)

Wave function for the ground state of the Quantum Harmonic Oscillator

The graph above shows the wave function for the ground state of the Quantum Harmonic Oscillator. We can see that it's concentrated at the origin, which means the particle spends most of its time around the origin.  Also, the wave function is symmetric about the origin and this is seen for even-numbered energy states. We also get to observe that the graph which is obtained by the numerical solution is aligned with the analytical solution, hence the result is accurate. 

---

- **Results for Simple Harmonic Oscillator:**

![picture alt](./images/shm.png)

Wave Function for a Simple Harmonic Oscillator

Solving the final equation for the harmonic wave function by incorporating the boundary values gives the solution where the wave function is proportional to x*e^*-x^2,* which can also be observed in the graph that is obtained through the RK4 numerical method. the function is 0 at x=0 and as x increases it reaches a maximum value and then back to zero after which it again goes to a minimum value, following such trend, the particle undergoes a simple harmonic motion. As it is not under any external non conservative force, the amplitude of the oscillation remains constant.

---

- **Result for Damped Harmonic Oscillator:**

![picture alt](./images/1damp.png)

Wave functions for critical, under-damped and over-damped oscillation

The graph above represents the wave function for under-damped, critical, and over-damped oscillation. These graphs are numerically solved by the RK4 method and they completely align with the solution we get analytically. 

The damping coefficient is greater than the undamped resonance frequency for the over-damped oscillation, and the damped oscillator will prompt it to approach zero amplitude, but gradually. The damping coefficient equals the undamped resonance frequency approaching zero amplitude quicker than the over-damped oscillator for systems in critical damping.

For a system with small damping, the period and frequency are almost equal to simple harmonic motion. However, the amplitude gradually decreases, which is the case of Under-damped oscillations. This occurs because the non-conservative damping force withdraws energy from the system, usually in the form of thermal energy. The above graph displays oscillation trends identical to the analytically obtained solutions with decreasing amplitude, indicating that the RK4 method gave accurate results.

---

### Conclusion:

This paper has implemented the Runge-Kutta method to solve the Schrodinger equation for a hydrogen and positronium atom. Runge - Kutta is a numerical method employed to solve differential equations effectively and precisely. This study's numerical results are in good accordance with analytical computations for the hydrogen atom results in modern physics and quantum mechanics. This method can also examine quantum systems with different potentials, such as an infinite well and a harmonic oscillator.

---

### **Path Forward:**

$$\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}+\frac{2}{\mathrm{r}} \frac{\mathrm{d}}{\mathrm{dr}}\right] \mathrm{R}(\mathrm{r})+\frac{2 \mu}{\hbar^{2}}\left[\mathrm{E}+\mathrm{V}(\mathrm{r})-\frac{l(l+1) \hbar^{2}}{2 \mu \mathrm{r}^{2}}\right] \mathrm{R}(\mathrm{r})=0$$

In the term paper, Schrodinger's equation for a ground-state hydrogen atom, for which l=o is solved. The code developed in the paper can be extended to solve for excited states of the hydrogen atom with l>0. This will change the Energy (*E*) and azimuthal quantum number (*l*) in the equation. Similarly, the code can also be used to calculate wave functions of atoms other than hydrogen and positronium.  The angular part for excited states and other atoms can also be similarly calculated using the code developed in the paper.

The code developed in this paper can be used to solve any second-order initial value problem occurring in nature. The f and g functions and the initial values will be changed suitably to numerically calculate solutions to any second-order ode.

- Scope of Improvement :-
While researching the topic we came across interesting research papers and original ideas. This led us to realize the scope of improvements in our methodology and codes developed :
    - For calculating the eigen values, we used brute force to assume an initial value and then increment it till the boundary conditions are achieved. We realized that this step can be improvised by incorporating the bisection method into our code and thus making it more efficient.
    - In cases where initial values of the problem statement do not exist, Newton Raphson method can be used to obtain  such values and then follow the common routine to solve the ODE using the RK4 method.
    - We also realized that methods with higher efficiency such as RK5 exist.

    ---


### **References:**

1. Ali Asghar Mowlav, Application of Runge-Kutta numerical methods to solve the Schrödinger equation for hydrogen and positronium atoms, International Journal of Recent Research and Applied Sciences, Volume 5, Pages 289-293, Year 2010
2. M. Sadeghi , F. Mohammadi and N. Aalipour, Numerical study of the radial Schrodinger Equation for Hydrogen atom using Legendre wavelet, Caspian Journal of Mathematical Sciences, Volume 8, Pages 35-42, Year 2019
3. Brigham Young University, Applied and Computational Mathematics Emphasis, IVP, Math 437, Volume 4, Year 2017
4. Neill Lambert, Numerical Solutions of Schrodinger’s Equation,TB2, Year 2001
5. Marie Christine, Solving The Stationary One Dimensional Schrodinger Equation With The Shooting Method, Bachelor Thesis, Vienna Institute of Technology, Year 2016
6. Qinghe Ming, Yanping Yang, and Yonglei Fang, An Optimized Runge-Kutta Method for the Numerical Solution of the Radial Schrodinger Equation, Mathematical Problems in Engineering Volume 2012, Article ID 867948, Year 2012
7. Prof. Sameer Sapra, CML100, Class notes

This paper has implemented the Runge-Kutta method to solve the Schrodinger equation for a hydrogen and positronium atom. Runge - Kutta is a numerical method employed to solve differential equations effectively and precisely. This study's numerical results are in good accordance with analytical computations for the hydrogen atom results in modern physics and quantum mechanics. This method can also examine quantum systems with different potentials, such as an infinite well and a harmonic oscillator.