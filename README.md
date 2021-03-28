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

<a href="https://www.codecogs.com/eqnedit.php?latex=-\frac{\hbar^{2}}{2&space;m}&space;\nabla^{2}&space;\psi(\mathbf{r})&plus;V(\mathbf{r})=E&space;\psi(\mathbf{r})&space;\\\int_{-\infty}^{&plus;\infty}&space;\Psi^{*}(\mathrm{x})&space;\Psi(\mathrm{x})&space;\mathrm{d}&space;\mathrm{x}=1" target="_blank"><img src="https://latex.codecogs.com/png.latex?-\frac{\hbar^{2}}{2&space;m}&space;\nabla^{2}&space;\psi(\mathbf{r})&plus;V(\mathbf{r})=E&space;\psi(\mathbf{r})&space;\\\int_{-\infty}^{&plus;\infty}&space;\Psi^{*}(\mathrm{x})&space;\Psi(\mathrm{x})&space;\mathrm{d}&space;\mathrm{x}=1" title="-\frac{\hbar^{2}}{2 m} \nabla^{2} \psi(\mathbf{r})+V(\mathbf{r})=E \psi(\mathbf{r}) \\\int_{-\infty}^{+\infty} \Psi^{*}(\mathrm{x}) \Psi(\mathrm{x}) \mathrm{d} \mathrm{x}=1" /></a>

This paper is concerned with the numerical solutions of the radial Schrodinger wave equation for the hydrogen and positronium atoms using the Runge-Kutta method. Schrodinger equation is an important quantum mechanical equation yielding wave functions as its solution. It rarely becomes possible to solve this equation analytically; the Runge Kutta method is thus discussed in this paper to provide accurate numerical methods to such equations where no analytical counterpart exists.
The Runge-Kutta method of order 4 is a method of numerical integration based on the formalism of Euler , but with better precis to solve initial value problems.
As an extension, this approach is also discussed for two other quantum mechanical systems: the infinite potential well and the quantum harmonic oscillator to attain their energy eigenstates and corresponding wave functions from the Schrodinger equation. 
Harmonic oscillators often occur in classical mechanics, a pendulum (with small displacements), spring-mass systems, and electric current flow in a circuit, being a few examples. As an extension, these mechanical systems: the simple harmonic oscillator and damped free harmonic oscillator with no damping, are also discussed numerically using the RK4 method in the paper.

---

### Problem Formulation**:**

- **Assumptions:**

For hydrogen, reduced mass is defined as: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\mu=\frac{\mathrm{m}_{\mathrm{p}}&space;\mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{p}}&plus;\mathrm{m}_{\mathrm{e}}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\mu=\frac{\mathrm{m}_{\mathrm{p}}&space;\mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{p}}&plus;\mathrm{m}_{\mathrm{e}}}" title="\mu=\frac{\mathrm{m}_{\mathrm{p}} \mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{p}}+\mathrm{m}_{\mathrm{e}}}" /></a>

Here, on dividing *u* by *mp:*

<a href="https://www.codecogs.com/eqnedit.php?latex=\mu=\frac{m_{e}}{1&plus;m_{e}&space;/&space;m_{p}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\mu=\frac{m_{e}}{1&plus;m_{e}&space;/&space;m_{p}}" title="\mu=\frac{m_{e}}{1+m_{e} / m_{p}}" /></a>

For this, the assumption is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{m_{e}}{m_{p}}&space;\sim&space;0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{m_{e}}{m_{p}}&space;\sim&space;0" title="\frac{m_{e}}{m_{p}} \sim 0" /></a>
For ease of calculations, another assumption for infinite potential well is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{c}&space;\left.\left(\hbar^{2}&space;/&space;2&space;m\right)=1\right.&space;\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{c}&space;\left.\left(\hbar^{2}&space;/&space;2&space;m\right)=1\right.&space;\end{array}" title="\begin{array}{c} \left.\left(\hbar^{2} / 2 m\right)=1\right. \end{array}" /></a>

---

- **Equations Used and Boundary Conditions:**
    - **Schrodinger Equation:**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{1}{r^{2}}&space;\frac{\partial}{\partial&space;r}\left(r^{2}&space;\frac{\partial&space;\psi}{\partial&space;r}\right)&plus;\frac{1}{r^{2}&space;\sin&space;\theta}&space;\frac{\partial}{\partial&space;\theta}\left(\sin&space;\theta&space;\frac{\partial&space;\psi}{\partial&space;\theta}\right)&plus;\frac{1}{r^{2}&space;\sin&space;^{2}&space;\theta}&space;\frac{\partial^{2}&space;\psi}{\partial&space;\phi^{2}}&plus;\frac{2&space;m}{\hbar^{2}}(E-U)&space;\psi=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{1}{r^{2}}&space;\frac{\partial}{\partial&space;r}\left(r^{2}&space;\frac{\partial&space;\psi}{\partial&space;r}\right)&plus;\frac{1}{r^{2}&space;\sin&space;\theta}&space;\frac{\partial}{\partial&space;\theta}\left(\sin&space;\theta&space;\frac{\partial&space;\psi}{\partial&space;\theta}\right)&plus;\frac{1}{r^{2}&space;\sin&space;^{2}&space;\theta}&space;\frac{\partial^{2}&space;\psi}{\partial&space;\phi^{2}}&plus;\frac{2&space;m}{\hbar^{2}}(E-U)&space;\psi=0" title="\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial \psi}{\partial r}\right)+\frac{1}{r^{2} \sin \theta} \frac{\partial}{\partial \theta}\left(\sin \theta \frac{\partial \psi}{\partial \theta}\right)+\frac{1}{r^{2} \sin ^{2} \theta} \frac{\partial^{2} \psi}{\partial \phi^{2}}+\frac{2 m}{\hbar^{2}}(E-U) \psi=0" /></a>

    - **Schrodinger Equation for Radial Part:**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}&plus;\frac{2}{\mathrm{r}}&space;\frac{\mathrm{d}}{\mathrm{dr}}\right]&space;\mathrm{R}(\mathrm{r})&plus;\frac{2&space;\mu}{\hbar^{2}}\left[\mathrm{E}&plus;\mathrm{V}(\mathrm{r})-\frac{l(l&plus;1)&space;\hbar^{2}}{2&space;\mu&space;\mathrm{r}^{2}}\right]&space;\mathrm{R}(\mathrm{r})=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}&plus;\frac{2}{\mathrm{r}}&space;\frac{\mathrm{d}}{\mathrm{dr}}\right]&space;\mathrm{R}(\mathrm{r})&plus;\frac{2&space;\mu}{\hbar^{2}}\left[\mathrm{E}&plus;\mathrm{V}(\mathrm{r})-\frac{l(l&plus;1)&space;\hbar^{2}}{2&space;\mu&space;\mathrm{r}^{2}}\right]&space;\mathrm{R}(\mathrm{r})=0" title="\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}+\frac{2}{\mathrm{r}} \frac{\mathrm{d}}{\mathrm{dr}}\right] \mathrm{R}(\mathrm{r})+\frac{2 \mu}{\hbar^{2}}\left[\mathrm{E}+\mathrm{V}(\mathrm{r})-\frac{l(l+1) \hbar^{2}}{2 \mu \mathrm{r}^{2}}\right] \mathrm{R}(\mathrm{r})=0" /></a>

        - **Initial Values for Radial Part:**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\left.R(r)\right|_{r=10^{-4}}=10^{-6},\left.\frac{d&space;R}{d&space;r}\right|_{r=10^{-4}}=-1000" target="_blank"><img src="https://latex.codecogs.com/png.latex?\left.R(r)\right|_{r=10^{-4}}=10^{-6},\left.\frac{d&space;R}{d&space;r}\right|_{r=10^{-4}}=-1000" title="\left.R(r)\right|_{r=10^{-4}}=10^{-6},\left.\frac{d R}{d r}\right|_{r=10^{-4}}=-1000" /></a>

    ---

    - **Schrodinger Equation for Angular Part:**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\sin&space;^{2}&space;\theta}{R}&space;\frac{\partial}{\partial&space;r}\left(r^{2}&space;\frac{\partial&space;R}{\partial&space;r}\right)&plus;\frac{\sin&space;\theta}{\Theta}&space;\frac{\partial}{\partial&space;\theta}\left(\sin&space;\theta&space;\frac{\partial&space;\Theta}{\partial&space;\theta}\right)&plus;\frac{2&space;m&space;r^{2}&space;\sin&space;^{2}&space;\theta}{\hbar^{2}}\left(\frac{Z&space;e^{2}}{4&space;\pi&space;\epsilon_{0}&space;r}&plus;E\right)=-\frac{1}{\Phi}&space;\frac{\partial^{2}&space;\Phi}{\partial&space;\phi^{2}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{\sin&space;^{2}&space;\theta}{R}&space;\frac{\partial}{\partial&space;r}\left(r^{2}&space;\frac{\partial&space;R}{\partial&space;r}\right)&plus;\frac{\sin&space;\theta}{\Theta}&space;\frac{\partial}{\partial&space;\theta}\left(\sin&space;\theta&space;\frac{\partial&space;\Theta}{\partial&space;\theta}\right)&plus;\frac{2&space;m&space;r^{2}&space;\sin&space;^{2}&space;\theta}{\hbar^{2}}\left(\frac{Z&space;e^{2}}{4&space;\pi&space;\epsilon_{0}&space;r}&plus;E\right)=-\frac{1}{\Phi}&space;\frac{\partial^{2}&space;\Phi}{\partial&space;\phi^{2}}" title="\frac{\sin ^{2} \theta}{R} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial R}{\partial r}\right)+\frac{\sin \theta}{\Theta} \frac{\partial}{\partial \theta}\left(\sin \theta \frac{\partial \Theta}{\partial \theta}\right)+\frac{2 m r^{2} \sin ^{2} \theta}{\hbar^{2}}\left(\frac{Z e^{2}}{4 \pi \epsilon_{0} r}+E\right)=-\frac{1}{\Phi} \frac{\partial^{2} \Phi}{\partial \phi^{2}}" /></a>

        - **Initial Values for Angular Part:**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\theta=\pi/6\\\\\Theta=1.69929\\\\\frac{d&space;\Theta}{d&space;\theta}=0.97745" target="_blank"><img src="https://latex.codecogs.com/png.latex?\theta=\pi/6\\\\\Theta=1.69929\\\\\frac{d&space;\Theta}{d&space;\theta}=0.97745" title="\theta=\pi/6\\\\\Theta=1.69929\\\\\frac{d \Theta}{d \theta}=0.97745" /></a>

        ---

    - **Equation for Infinite Well:**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d^{2}}{d&space;x}&space;\psi(x)=\frac{-2&space;m_{e}&space;E}{\hbar^{2}}&space;\cdot&space;\psi(x)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{d^{2}}{d&space;x}&space;\psi(x)=\frac{-2&space;m_{e}&space;E}{\hbar^{2}}&space;\cdot&space;\psi(x)" title="\frac{d^{2}}{d x} \psi(x)=\frac{-2 m_{e} E}{\hbar^{2}} \cdot \psi(x)" /></a>

        - **Boundary conditions for Infinite Well:**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\psi(0)=1,&space;\frac{d&space;\psi(0)}{d&space;x}=0,&space;\psi(0)=0,&space;\frac{d&space;\psi(0)}{d&space;x}=1&space;\\\psi(x&space;\rightarrow-\infty)=0,&space;\psi(x&space;\rightarrow&space;\infty)=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\psi(0)=1,&space;\frac{d&space;\psi(0)}{d&space;x}=0,&space;\psi(0)=0,&space;\frac{d&space;\psi(0)}{d&space;x}=1&space;\\\psi(x&space;\rightarrow-\infty)=0,&space;\psi(x&space;\rightarrow&space;\infty)=0" title="\psi(0)=1, \frac{d \psi(0)}{d x}=0, \psi(0)=0, \frac{d \psi(0)}{d x}=1 \\\psi(x \rightarrow-\infty)=0, \psi(x \rightarrow \infty)=0" /></a>

        ---

    - **Equation for Harmonic Oscillator:**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{-\hbar}{2&space;m}&space;\frac{d^{2}}{d&space;x^{2}}&space;\psi(x)&plus;\frac{m&space;\omega^{2}}{2}&space;x^{2}&space;\psi(x)=E&space;\psi(x)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{-\hbar}{2&space;m}&space;\frac{d^{2}}{d&space;x^{2}}&space;\psi(x)&plus;\frac{m&space;\omega^{2}}{2}&space;x^{2}&space;\psi(x)=E&space;\psi(x)" title="\frac{-\hbar}{2 m} \frac{d^{2}}{d x^{2}} \psi(x)+\frac{m \omega^{2}}{2} x^{2} \psi(x)=E \psi(x)" /></a>

        - **Boundary conditions for Harmonic Oscillator:**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\psi(-L&space;/&space;2)=0,&space;\psi(&plus;L&space;/&space;2)=0,&space;E>0,&space;V(x=-L/2)=\infty,&space;V(x=L/2)=\infty" target="_blank"><img src="https://latex.codecogs.com/png.latex?\psi(-L&space;/&space;2)=0,&space;\psi(&plus;L&space;/&space;2)=0,&space;E>0,&space;V(x=-L/2)=\infty,&space;V(x=L/2)=\infty" title="\psi(-L / 2)=0, \psi(+L / 2)=0, E>0, V(x=-L/2)=\infty, V(x=L/2)=\infty" /></a>

    ---

    - **Equation for  Simple Harmonic Oscillator (Classical Model)**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{l}m&space;y^{\prime&space;\prime}&plus;k&space;y=0&space;\\\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{l}m&space;y^{\prime&space;\prime}&plus;k&space;y=0&space;\\\end{array}" title="\begin{array}{l}m y^{\prime \prime}+k y=0 \\\end{array}" /></a>

        - **Boundary conditions for  Simple Harmonic Oscillator(Classical Model):**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\\y(0)=0,&space;\quad&space;y^{\prime}(0)=1" target="_blank"><img src="https://latex.codecogs.com/png.latex?\\y(0)=0,&space;\quad&space;y^{\prime}(0)=1" title="\\y(0)=0, \quad y^{\prime}(0)=1" /></a>

    ---

    - **Equation for  Damped Harmonic Oscillator (Classical Model)**

        <a href="https://www.codecogs.com/eqnedit.php?latex=m&space;y^{\prime&space;\prime}(t)&plus;\gamma&space;y^{\prime}(t)&plus;k&space;y(t)=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?m&space;y^{\prime&space;\prime}(t)&plus;\gamma&space;y^{\prime}(t)&plus;k&space;y(t)=0" title="m y^{\prime \prime}(t)+\gamma y^{\prime}(t)+k y(t)=0" /></a>

        - **Boundary conditions for  Simple Harmonic Oscillator(Classical Model):**

        <a href="https://www.codecogs.com/eqnedit.php?latex=\\y(0)=1,&space;\quad&space;y^{\prime}(0)=-1" target="_blank"><img src="https://latex.codecogs.com/png.latex?\\y(0)=1,&space;\quad&space;y^{\prime}(0)=-1" title="\\y(0)=1, \quad y^{\prime}(0)=-1" /></a>

        ---

- **Derivation of 4th order Runge-Kutta:**

Runge-Kutta is a method that is widely used to solve differential problems whose initial values are given. It is  a very efficient method as it does not require us to calculate the higher order derivatives of the function and solves the problems with high accuracy. There are Runge-Kutta methods that go upto the 10th order, but the most frequently used are the methods from order 1-5. We have more scope we have to increase the step size while maintaining the accuracy for higher order RK methods.

The derivation of Runge Kutta is based on Taylor series expansion which is written as:

<a href="https://www.codecogs.com/eqnedit.php?latex=y_{n&plus;1}=y_{n}&plus;h&space;f_{n}&plus;\frac{1}{2}&space;h^{2}\left(\frac{d&space;f}{d&space;x}\right)_{n}&plus;\cdots&plus;\frac{1}{p&space;!}&space;h^{p}\left(\frac{d^{p-1}&space;f}{d&space;x^{p-1}}\right)_{n}&plus;O\left(h^{p&plus;1}\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?y_{n&plus;1}=y_{n}&plus;h&space;f_{n}&plus;\frac{1}{2}&space;h^{2}\left(\frac{d&space;f}{d&space;x}\right)_{n}&plus;\cdots&plus;\frac{1}{p&space;!}&space;h^{p}\left(\frac{d^{p-1}&space;f}{d&space;x^{p-1}}\right)_{n}&plus;O\left(h^{p&plus;1}\right)" title="y_{n+1}=y_{n}+h f_{n}+\frac{1}{2} h^{2}\left(\frac{d f}{d x}\right)_{n}+\cdots+\frac{1}{p !} h^{p}\left(\frac{d^{p-1} f}{d x^{p-1}}\right)_{n}+O\left(h^{p+1}\right)" /></a>

For 4th order equation,  first four terms of Taylor series are used:

<a href="https://www.codecogs.com/eqnedit.php?latex=y_{i&plus;1}=y_{i}&plus;f\left(x_{i},&space;y_{i}\right)&space;h&plus;\frac{1}{2&space;!}&space;f^{\prime}\left(x_{i},&space;y_{i}\right)&space;h^{2}&plus;\frac{1}{3&space;!}&space;f^{\prime&space;\prime}\left(x_{i},&space;y_{i}\right)&space;h^{3}&plus;\frac{1}{4&space;!}&space;f^{\prime&space;\prime&space;\prime}\left(x_{i},&space;y_{i}\right)&space;h^{4}" target="_blank"><img src="https://latex.codecogs.com/png.latex?y_{i&plus;1}=y_{i}&plus;f\left(x_{i},&space;y_{i}\right)&space;h&plus;\frac{1}{2&space;!}&space;f^{\prime}\left(x_{i},&space;y_{i}\right)&space;h^{2}&plus;\frac{1}{3&space;!}&space;f^{\prime&space;\prime}\left(x_{i},&space;y_{i}\right)&space;h^{3}&plus;\frac{1}{4&space;!}&space;f^{\prime&space;\prime&space;\prime}\left(x_{i},&space;y_{i}\right)&space;h^{4}" title="y_{i+1}=y_{i}+f\left(x_{i}, y_{i}\right) h+\frac{1}{2 !} f^{\prime}\left(x_{i}, y_{i}\right) h^{2}+\frac{1}{3 !} f^{\prime \prime}\left(x_{i}, y_{i}\right) h^{3}+\frac{1}{4 !} f^{\prime \prime \prime}\left(x_{i}, y_{i}\right) h^{4}" /></a>

The Runge Kutta  Equation for a general '*s'* order can be written as:

<a href="https://www.codecogs.com/eqnedit.php?latex=y_{t&plus;h}=y_{t}&plus;h&space;\cdot&space;\sum_{i=1}^{s}&space;a_{i}&space;k_{i}&plus;\mathcal{O}\left(h^{s&plus;1}\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?y_{t&plus;h}=y_{t}&plus;h&space;\cdot&space;\sum_{i=1}^{s}&space;a_{i}&space;k_{i}&plus;\mathcal{O}\left(h^{s&plus;1}\right)" title="y_{t+h}=y_{t}+h \cdot \sum_{i=1}^{s} a_{i} k_{i}+\mathcal{O}\left(h^{s+1}\right)" /></a>

where increments for *y* at *i*-th order are:

<a href="https://www.codecogs.com/eqnedit.php?latex=k_{i}=y_{t}&plus;h&space;\cdot&space;\sum_{j=1}^{s}&space;\beta_{i&space;j}&space;f\left(k_{j},&space;t_{n}&plus;\alpha_{i}&space;h\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?k_{i}=y_{t}&plus;h&space;\cdot&space;\sum_{j=1}^{s}&space;\beta_{i&space;j}&space;f\left(k_{j},&space;t_{n}&plus;\alpha_{i}&space;h\right)" title="k_{i}=y_{t}+h \cdot \sum_{j=1}^{s} \beta_{i j} f\left(k_{j}, t_{n}+\alpha_{i} h\right)" /></a>

Here, the values of the constants are chosen as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{r}\alpha_{i}&space;\\\alpha_{1}=0&space;\\\alpha_{2}=\frac{1}{2}&space;\\\alpha_{3}=\frac{1}{2}&space;\\\alpha_{4}=1\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{r}\alpha_{i}&space;\\\alpha_{1}=0&space;\\\alpha_{2}=\frac{1}{2}&space;\\\alpha_{3}=\frac{1}{2}&space;\\\alpha_{4}=1\end{array}" title="\begin{array}{r}\alpha_{i} \\\alpha_{1}=0 \\\alpha_{2}=\frac{1}{2} \\\alpha_{3}=\frac{1}{2} \\\alpha_{4}=1\end{array}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{r}\beta_{i&space;j}&space;\\\beta_{21}=\frac{1}{2}&space;\\\beta_{32}=\frac{1}{2}&space;\\\beta_{43}=1\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{r}\beta_{i&space;j}&space;\\\beta_{21}=\frac{1}{2}&space;\\\beta_{32}=\frac{1}{2}&space;\\\beta_{43}=1\end{array}" title="\begin{array}{r}\beta_{i j} \\\beta_{21}=\frac{1}{2} \\\beta_{32}=\frac{1}{2} \\\beta_{43}=1\end{array}" /></a>

*y* can be defined **as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{c}y_{t&plus;h}^{1}=y_{t}&plus;h&space;f\left(y_{t},&space;t\right)&space;\\y_{t&plus;h}^{2}=y_{t}&plus;h&space;f\left(y_{t&plus;h&space;/&space;2}^{1},&space;t&plus;\frac{h}{2}\right)&space;\\y_{t&plus;h}^{3}=y_{t}&plus;h&space;f\left(y_{t&plus;h&space;/&space;2}^{2},&space;t&plus;\frac{h}{2}\right)&space;\\\text&space;{&space;where&space;}&space;y_{t,&space;h&space;/&space;2}^{1}=\frac{y_{t}&plus;y_{t&plus;h}^{1}}{2}&space;\text&space;{&space;and&space;}&space;y_{t&plus;h&space;/&space;2}^{2}=\frac{y_{t}&plus;y_{t&plus;h}^{2}}{2}\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{c}y_{t&plus;h}^{1}=y_{t}&plus;h&space;f\left(y_{t},&space;t\right)&space;\\y_{t&plus;h}^{2}=y_{t}&plus;h&space;f\left(y_{t&plus;h&space;/&space;2}^{1},&space;t&plus;\frac{h}{2}\right)&space;\\y_{t&plus;h}^{3}=y_{t}&plus;h&space;f\left(y_{t&plus;h&space;/&space;2}^{2},&space;t&plus;\frac{h}{2}\right)&space;\\\text&space;{&space;where&space;}&space;y_{t,&space;h&space;/&space;2}^{1}=\frac{y_{t}&plus;y_{t&plus;h}^{1}}{2}&space;\text&space;{&space;and&space;}&space;y_{t&plus;h&space;/&space;2}^{2}=\frac{y_{t}&plus;y_{t&plus;h}^{2}}{2}\end{array}" title="\begin{array}{c}y_{t+h}^{1}=y_{t}+h f\left(y_{t}, t\right) \\y_{t+h}^{2}=y_{t}+h f\left(y_{t+h / 2}^{1}, t+\frac{h}{2}\right) \\y_{t+h}^{3}=y_{t}+h f\left(y_{t+h / 2}^{2}, t+\frac{h}{2}\right) \\\text { where } y_{t, h / 2}^{1}=\frac{y_{t}+y_{t+h}^{1}}{2} \text { and } y_{t+h / 2}^{2}=\frac{y_{t}+y_{t+h}^{2}}{2}\end{array}" /></a>

*k* can be defined as:

<a href="https://www.codecogs.com/eqnedit.php?latex=k_{1}=f\left(y_{t},&space;t\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?k_{1}=f\left(y_{t},&space;t\right)" title="k_{1}=f\left(y_{t}, t\right)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{aligned}k_{2}&space;&=f\left(y_{t&plus;h&space;/&space;2}^{1},&space;t&plus;\frac{h}{2}\right)=f\left(y_{t}&plus;\frac{h}{2}&space;k_{1},&space;t&plus;\frac{h}{2}\right)&space;\\&=f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)&space;\\k_{3}&space;&=f\left(y_{t&plus;h&space;/&space;2}^{2},&space;t&plus;\frac{h}{2}\right)=f\left(y_{t}&plus;\frac{h}{2}&space;f\left(y_{t}&plus;\frac{h}{2}&space;k_{1},&space;t&plus;\frac{h}{2}\right),&space;t&plus;\frac{h}{2}\right)&space;\\&=f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]&space;\\k_{4}&space;&=f\left(y_{t&plus;h}^{3},&space;t&plus;h\right)=f\left(y_{t}&plus;h&space;f\left(y_{t}&plus;\frac{h}{2}&space;k_{2},&space;t&plus;\frac{h}{2}\right),&space;t&plus;h\right)&space;\\&=f\left(y_{t}&plus;h&space;f\left(y_{t}&plus;\frac{h}{2}&space;f\left(y_{t}&plus;\frac{h}{2}&space;f\left(y_{t},&space;t\right),&space;t&plus;\frac{h}{2}\right),&space;t&plus;\frac{h}{2}\right),&space;t&plus;h\right)&space;\\&=f\left(y_{t},&space;t\right)&plus;h&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]\right]\end{aligned}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{aligned}k_{2}&space;&=f\left(y_{t&plus;h&space;/&space;2}^{1},&space;t&plus;\frac{h}{2}\right)=f\left(y_{t}&plus;\frac{h}{2}&space;k_{1},&space;t&plus;\frac{h}{2}\right)&space;\\&=f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)&space;\\k_{3}&space;&=f\left(y_{t&plus;h&space;/&space;2}^{2},&space;t&plus;\frac{h}{2}\right)=f\left(y_{t}&plus;\frac{h}{2}&space;f\left(y_{t}&plus;\frac{h}{2}&space;k_{1},&space;t&plus;\frac{h}{2}\right),&space;t&plus;\frac{h}{2}\right)&space;\\&=f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]&space;\\k_{4}&space;&=f\left(y_{t&plus;h}^{3},&space;t&plus;h\right)=f\left(y_{t}&plus;h&space;f\left(y_{t}&plus;\frac{h}{2}&space;k_{2},&space;t&plus;\frac{h}{2}\right),&space;t&plus;h\right)&space;\\&=f\left(y_{t}&plus;h&space;f\left(y_{t}&plus;\frac{h}{2}&space;f\left(y_{t}&plus;\frac{h}{2}&space;f\left(y_{t},&space;t\right),&space;t&plus;\frac{h}{2}\right),&space;t&plus;\frac{h}{2}\right),&space;t&plus;h\right)&space;\\&=f\left(y_{t},&space;t\right)&plus;h&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]\right]\end{aligned}" title="\begin{aligned}k_{2} &=f\left(y_{t+h / 2}^{1}, t+\frac{h}{2}\right)=f\left(y_{t}+\frac{h}{2} k_{1}, t+\frac{h}{2}\right) \\&=f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right) \\k_{3} &=f\left(y_{t+h / 2}^{2}, t+\frac{h}{2}\right)=f\left(y_{t}+\frac{h}{2} f\left(y_{t}+\frac{h}{2} k_{1}, t+\frac{h}{2}\right), t+\frac{h}{2}\right) \\&=f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right] \\k_{4} &=f\left(y_{t+h}^{3}, t+h\right)=f\left(y_{t}+h f\left(y_{t}+\frac{h}{2} k_{2}, t+\frac{h}{2}\right), t+h\right) \\&=f\left(y_{t}+h f\left(y_{t}+\frac{h}{2} f\left(y_{t}+\frac{h}{2} f\left(y_{t}, t\right), t+\frac{h}{2}\right), t+\frac{h}{2}\right), t+h\right) \\&=f\left(y_{t}, t\right)+h \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right]\right]\end{aligned}" /></a>

Hence, substituting *k* in *y* gives:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{aligned}y_{t&plus;h}=&&space;y_{t}&plus;h\left\{a&space;\cdot&space;f\left(y_{t},&space;t\right)&plus;b&space;\cdot\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]&plus;\right.\\&&plus;c&space;\cdot\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]\right]&plus;\\&\left.&plus;d&space;\cdot\left[f\left(y_{t},&space;t\right)&plus;h&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]\right]\right]\right\}&plus;\mathcal{O}\left(h^{5}\right)&space;\\=&&space;y_{t}&plus;a&space;\cdot&space;h&space;f_{t}&plus;b&space;\cdot&space;h&space;f_{t}&plus;b&space;\cdot&space;\frac{h^{2}}{2}&space;\frac{d&space;f_{t}}{d&space;t}&plus;c&space;\cdot&space;h&space;f_{t}&plus;c&space;\cdot&space;\frac{h^{2}}{2}&space;\frac{d&space;f_{t}}{d&space;t}&plus;\\&&plus;c&space;\cdot&space;\frac{h^{3}}{4}&space;\frac{d^{2}&space;f_{t}}{d&space;t^{2}}&plus;d&space;\cdot&space;h&space;f_{t}&plus;d&space;\cdot&space;h^{2}&space;\frac{d&space;f_{t}}{d&space;t}&plus;d&space;\cdot&space;\frac{h^{3}}{2}&space;\frac{d^{2}&space;f_{t}}{d&space;t^{2}}&plus;d&space;\cdot&space;\frac{h^{4}}{4}&space;\frac{d^{3}&space;f_{t}}{d&space;t^{3}}&plus;\mathcal{O}\left(h^{5}\right)\end{aligned}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{aligned}y_{t&plus;h}=&&space;y_{t}&plus;h\left\{a&space;\cdot&space;f\left(y_{t},&space;t\right)&plus;b&space;\cdot\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]&plus;\right.\\&&plus;c&space;\cdot\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]\right]&plus;\\&\left.&plus;d&space;\cdot\left[f\left(y_{t},&space;t\right)&plus;h&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}\left[f\left(y_{t},&space;t\right)&plus;\frac{h}{2}&space;\frac{d}{d&space;t}&space;f\left(y_{t},&space;t\right)\right]\right]\right]\right\}&plus;\mathcal{O}\left(h^{5}\right)&space;\\=&&space;y_{t}&plus;a&space;\cdot&space;h&space;f_{t}&plus;b&space;\cdot&space;h&space;f_{t}&plus;b&space;\cdot&space;\frac{h^{2}}{2}&space;\frac{d&space;f_{t}}{d&space;t}&plus;c&space;\cdot&space;h&space;f_{t}&plus;c&space;\cdot&space;\frac{h^{2}}{2}&space;\frac{d&space;f_{t}}{d&space;t}&plus;\\&&plus;c&space;\cdot&space;\frac{h^{3}}{4}&space;\frac{d^{2}&space;f_{t}}{d&space;t^{2}}&plus;d&space;\cdot&space;h&space;f_{t}&plus;d&space;\cdot&space;h^{2}&space;\frac{d&space;f_{t}}{d&space;t}&plus;d&space;\cdot&space;\frac{h^{3}}{2}&space;\frac{d^{2}&space;f_{t}}{d&space;t^{2}}&plus;d&space;\cdot&space;\frac{h^{4}}{4}&space;\frac{d^{3}&space;f_{t}}{d&space;t^{3}}&plus;\mathcal{O}\left(h^{5}\right)\end{aligned}" title="\begin{aligned}y_{t+h}=& y_{t}+h\left\{a \cdot f\left(y_{t}, t\right)+b \cdot\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right]+\right.\\&+c \cdot\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right]\right]+\\&\left.+d \cdot\left[f\left(y_{t}, t\right)+h \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t}\left[f\left(y_{t}, t\right)+\frac{h}{2} \frac{d}{d t} f\left(y_{t}, t\right)\right]\right]\right]\right\}+\mathcal{O}\left(h^{5}\right) \\=& y_{t}+a \cdot h f_{t}+b \cdot h f_{t}+b \cdot \frac{h^{2}}{2} \frac{d f_{t}}{d t}+c \cdot h f_{t}+c \cdot \frac{h^{2}}{2} \frac{d f_{t}}{d t}+\\&+c \cdot \frac{h^{3}}{4} \frac{d^{2} f_{t}}{d t^{2}}+d \cdot h f_{t}+d \cdot h^{2} \frac{d f_{t}}{d t}+d \cdot \frac{h^{3}}{2} \frac{d^{2} f_{t}}{d t^{2}}+d \cdot \frac{h^{4}}{4} \frac{d^{3} f_{t}}{d t^{3}}+\mathcal{O}\left(h^{5}\right)\end{aligned}" /></a>

Comparing the above equation to Taylor's series expansion for first four terms:

<a href="https://www.codecogs.com/eqnedit.php?latex=\left\{\begin{array}{l}a&plus;b&plus;c&plus;d=1&space;\\\frac{1}{2}&space;b&plus;\frac{1}{2}&space;c&plus;d=\frac{1}{2}&space;\\\frac{1}{4}&space;c&plus;\frac{1}{2}&space;d=\frac{1}{6}&space;\\\frac{1}{4}&space;d=\frac{1}{24}\end{array}\right." target="_blank"><img src="https://latex.codecogs.com/png.latex?\left\{\begin{array}{l}a&plus;b&plus;c&plus;d=1&space;\\\frac{1}{2}&space;b&plus;\frac{1}{2}&space;c&plus;d=\frac{1}{2}&space;\\\frac{1}{4}&space;c&plus;\frac{1}{2}&space;d=\frac{1}{6}&space;\\\frac{1}{4}&space;d=\frac{1}{24}\end{array}\right." title="\left\{\begin{array}{l}a+b+c+d=1 \\\frac{1}{2} b+\frac{1}{2} c+d=\frac{1}{2} \\\frac{1}{4} c+\frac{1}{2} d=\frac{1}{6} \\\frac{1}{4} d=\frac{1}{24}\end{array}\right." /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a=\frac{1}{6},&space;b=\frac{1}{3},&space;c=\frac{1}{3},&space;d=\frac{1}{6}" target="_blank"><img src="https://latex.codecogs.com/png.latex?a=\frac{1}{6},&space;b=\frac{1}{3},&space;c=\frac{1}{3},&space;d=\frac{1}{6}" title="a=\frac{1}{6}, b=\frac{1}{3}, c=\frac{1}{3}, d=\frac{1}{6}" /></a>

which gives the final result as:

<a href="https://www.codecogs.com/eqnedit.php?latex=y_{i&plus;1}=y_{i}&plus;\frac{1}{6}\left(k_{1}&plus;2&space;k_{2}&plus;2&space;k_{3}&plus;k_{4}\right)&space;h" target="_blank"><img src="https://latex.codecogs.com/png.latex?y_{i&plus;1}=y_{i}&plus;\frac{1}{6}\left(k_{1}&plus;2&space;k_{2}&plus;2&space;k_{3}&plus;k_{4}\right)&space;h" title="y_{i+1}=y_{i}+\frac{1}{6}\left(k_{1}+2 k_{2}+2 k_{3}+k_{4}\right) h" /></a>

where:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{aligned}k_{1}&space;&=f\left(x_{i},&space;y_{i}\right)&space;\\k_{2}&space;&=f\left(x_{i}&plus;\frac{1}{2},&space;y_{i}&plus;\frac{1}{2}&space;k_{1}&space;h\right)&space;\\k_{3}&space;&=f\left(x_{i}&plus;\frac{1}{2},&space;y_{i}&plus;\frac{1}{2}&space;k_{2}&space;h\right)&space;\\k_{4}&space;&=f\left(x_{i}&plus;h,&space;y_{i}&plus;k_{3}&space;h\right)\end{aligned}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{aligned}k_{1}&space;&=f\left(x_{i},&space;y_{i}\right)&space;\\k_{2}&space;&=f\left(x_{i}&plus;\frac{1}{2},&space;y_{i}&plus;\frac{1}{2}&space;k_{1}&space;h\right)&space;\\k_{3}&space;&=f\left(x_{i}&plus;\frac{1}{2},&space;y_{i}&plus;\frac{1}{2}&space;k_{2}&space;h\right)&space;\\k_{4}&space;&=f\left(x_{i}&plus;h,&space;y_{i}&plus;k_{3}&space;h\right)\end{aligned}" title="\begin{aligned}k_{1} &=f\left(x_{i}, y_{i}\right) \\k_{2} &=f\left(x_{i}+\frac{1}{2}, y_{i}+\frac{1}{2} k_{1} h\right) \\k_{3} &=f\left(x_{i}+\frac{1}{2}, y_{i}+\frac{1}{2} k_{2} h\right) \\k_{4} &=f\left(x_{i}+h, y_{i}+k_{3} h\right)\end{aligned}" /></a>

---

### **Numerical Analysis:**

- **Numerical Analysis of  Radial Schrodinger Equation:**

The final formulas for a fourth order Runge-Kutta equation are:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{aligned}\Delta&space;y^{(1)}&space;&=h&space;f\left(x_{i},&space;y_{i},&space;z_{i}\right)&space;\\\Delta&space;z^{(1)}&space;&=h&space;g\left(x_{i},&space;y_{i},&space;z_{i}\right)&space;\\\Delta&space;y^{(2)}&space;&=h&space;f\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{1}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{1}}{2}\right)&space;\\\Delta&space;z^{(2)}&space;&=h&space;g\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{1}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{1}}{2}\right)&space;\\\Delta&space;y^{(3)}&space;&=h&space;f\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{2}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{2}}{2}\right)&space;\\\Delta&space;z^{(3)}&space;&=h&space;g\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{2}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{2}}{2}\right)&space;\\\Delta&space;y^{(4)}&space;&=h&space;f\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{3}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{3}}{2}\right)&space;\\\Delta&space;z^{(4)}&space;&=h&space;g\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{3}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{3}}{2}\right)\end{aligned}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{aligned}\Delta&space;y^{(1)}&space;&=h&space;f\left(x_{i},&space;y_{i},&space;z_{i}\right)&space;\\\Delta&space;z^{(1)}&space;&=h&space;g\left(x_{i},&space;y_{i},&space;z_{i}\right)&space;\\\Delta&space;y^{(2)}&space;&=h&space;f\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{1}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{1}}{2}\right)&space;\\\Delta&space;z^{(2)}&space;&=h&space;g\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{1}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{1}}{2}\right)&space;\\\Delta&space;y^{(3)}&space;&=h&space;f\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{2}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{2}}{2}\right)&space;\\\Delta&space;z^{(3)}&space;&=h&space;g\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{2}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{2}}{2}\right)&space;\\\Delta&space;y^{(4)}&space;&=h&space;f\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{3}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{3}}{2}\right)&space;\\\Delta&space;z^{(4)}&space;&=h&space;g\left(x_{i}&plus;\frac{h}{2},&space;y_{i}&plus;\frac{\Delta&space;y^{3}}{2},&space;z_{i}&plus;\frac{\Delta&space;z^{3}}{2}\right)\end{aligned}" title="\begin{aligned}\Delta y^{(1)} &=h f\left(x_{i}, y_{i}, z_{i}\right) \\\Delta z^{(1)} &=h g\left(x_{i}, y_{i}, z_{i}\right) \\\Delta y^{(2)} &=h f\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{1}}{2}, z_{i}+\frac{\Delta z^{1}}{2}\right) \\\Delta z^{(2)} &=h g\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{1}}{2}, z_{i}+\frac{\Delta z^{1}}{2}\right) \\\Delta y^{(3)} &=h f\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{2}}{2}, z_{i}+\frac{\Delta z^{2}}{2}\right) \\\Delta z^{(3)} &=h g\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{2}}{2}, z_{i}+\frac{\Delta z^{2}}{2}\right) \\\Delta y^{(4)} &=h f\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{3}}{2}, z_{i}+\frac{\Delta z^{3}}{2}\right) \\\Delta z^{(4)} &=h g\left(x_{i}+\frac{h}{2}, y_{i}+\frac{\Delta y^{3}}{2}, z_{i}+\frac{\Delta z^{3}}{2}\right)\end{aligned}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\text&space;where,&space;h=\frac{x_{n}-x_{0}}{n}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\text&space;where,&space;h=\frac{x_{n}-x_{0}}{n}" title="\text where, h=\frac{x_{n}-x_{0}}{n}" /></a>

The incrementation done after  each iteration is as follows:

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{i}=a&plus;i&space;h" target="_blank"><img src="https://latex.codecogs.com/png.latex?x_{i}=a&plus;i&space;h" title="x_{i}=a+i h" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{l}y_{i&plus;1}=y_{i}&plus;\frac{1}{6}\left(\Delta&space;y^{(1)}&plus;2&space;\Delta&space;y^{(2)}&plus;2&space;\Delta&space;y^{(3)}&plus;\Delta&space;y^{(4)}\right)&space;&plus;O(h^{5})&space;\\z_{i&plus;1}=z_{i}&plus;\frac{1}{6}\left(\Delta&space;z^{(1)}&plus;2&space;\Delta&space;z^{(2)}&plus;2&space;\Delta&space;z^{(3)}&plus;\Delta&space;z^{(4)}\right)&plus;O(h^{5})\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{l}y_{i&plus;1}=y_{i}&plus;\frac{1}{6}\left(\Delta&space;y^{(1)}&plus;2&space;\Delta&space;y^{(2)}&plus;2&space;\Delta&space;y^{(3)}&plus;\Delta&space;y^{(4)}\right)&space;&plus;O(h^{5})&space;\\z_{i&plus;1}=z_{i}&plus;\frac{1}{6}\left(\Delta&space;z^{(1)}&plus;2&space;\Delta&space;z^{(2)}&plus;2&space;\Delta&space;z^{(3)}&plus;\Delta&space;z^{(4)}\right)&plus;O(h^{5})\end{array}" title="\begin{array}{l}y_{i+1}=y_{i}+\frac{1}{6}\left(\Delta y^{(1)}+2 \Delta y^{(2)}+2 \Delta y^{(3)}+\Delta y^{(4)}\right) +O(h^{5}) \\z_{i+1}=z_{i}+\frac{1}{6}\left(\Delta z^{(1)}+2 \Delta z^{(2)}+2 \Delta z^{(3)}+\Delta z^{(4)}\right)+O(h^{5})\end{array}" /></a>

The application of the above formulas in the Schrodinger equation is done as given below.

<a href="https://www.codecogs.com/eqnedit.php?latex=\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}&plus;\frac{2}{\mathrm{r}}&space;\frac{\mathrm{d}}{\mathrm{dr}}\right]&space;\mathrm{R}(\mathrm{r})&plus;\frac{2&space;\mu}{\hbar^{2}}\left[\mathrm{E}&plus;\mathrm{V}(\mathrm{r})-\frac{l(l&plus;1)&space;\hbar^{2}}{2&space;\mu&space;\mathrm{r}^{2}}\right]&space;\mathrm{R}(\mathrm{r})=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}&plus;\frac{2}{\mathrm{r}}&space;\frac{\mathrm{d}}{\mathrm{dr}}\right]&space;\mathrm{R}(\mathrm{r})&plus;\frac{2&space;\mu}{\hbar^{2}}\left[\mathrm{E}&plus;\mathrm{V}(\mathrm{r})-\frac{l(l&plus;1)&space;\hbar^{2}}{2&space;\mu&space;\mathrm{r}^{2}}\right]&space;\mathrm{R}(\mathrm{r})=0" title="\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}+\frac{2}{\mathrm{r}} \frac{\mathrm{d}}{\mathrm{dr}}\right] \mathrm{R}(\mathrm{r})+\frac{2 \mu}{\hbar^{2}}\left[\mathrm{E}+\mathrm{V}(\mathrm{r})-\frac{l(l+1) \hbar^{2}}{2 \mu \mathrm{r}^{2}}\right] \mathrm{R}(\mathrm{r})=0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d&space;R}{d&space;r}=z" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{d&space;R}{d&space;r}=z" title="\frac{d R}{d r}=z" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d&space;z}{d&space;r}=\frac{d^{2}&space;R}{d&space;r^{2}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{d&space;z}{d&space;r}=\frac{d^{2}&space;R}{d&space;r^{2}}" title="\frac{d z}{d r}=\frac{d^{2} R}{d r^{2}}" /></a>

The above equations are then simplified to:

<a href="https://www.codecogs.com/eqnedit.php?latex=\\r&space;=&space;x&space;\\R&space;=&space;y&space;\\\frac{d&space;R}{d&space;r}=z" target="_blank"><img src="https://latex.codecogs.com/png.latex?\\r&space;=&space;x&space;\\R&space;=&space;y&space;\\\frac{d&space;R}{d&space;r}=z" title="\\r = x \\R = y \\\frac{d R}{d r}=z" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d&space;y}{d&space;x}=z=f(x,&space;y,&space;z)&space;\\\frac{d&space;z}{d&space;x}=-\frac{2&space;z}{x}-\frac{2&space;A&space;\mu}{\hbar^{2}}&space;y=g(x,&space;y,&space;z)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{d&space;y}{d&space;x}=z=f(x,&space;y,&space;z)&space;\\\frac{d&space;z}{d&space;x}=-\frac{2&space;z}{x}-\frac{2&space;A&space;\mu}{\hbar^{2}}&space;y=g(x,&space;y,&space;z)" title="\frac{d y}{d x}=z=f(x, y, z) \\\frac{d z}{d x}=-\frac{2 z}{x}-\frac{2 A \mu}{\hbar^{2}} y=g(x, y, z)" /></a>

where  

<a href="https://www.codecogs.com/eqnedit.php?latex=A&space;=&space;\left[\mathrm{E}&plus;\mathrm{V}(\mathrm{r})-\frac{l(l&plus;1)&space;\hbar^{2}}{2&space;\mu&space;\mathrm{r}^{2}}\right]" target="_blank"><img src="https://latex.codecogs.com/png.latex?A&space;=&space;\left[\mathrm{E}&plus;\mathrm{V}(\mathrm{r})-\frac{l(l&plus;1)&space;\hbar^{2}}{2&space;\mu&space;\mathrm{r}^{2}}\right]" title="A = \left[\mathrm{E}+\mathrm{V}(\mathrm{r})-\frac{l(l+1) \hbar^{2}}{2 \mu \mathrm{r}^{2}}\right]" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{l}&space;k_{1}=h&space;f\left(x_{0},&space;y_{0},&space;z_{0}\right)&space;\\&space;l_{1}=h&space;g\left(x_{0},&space;y_{0},&space;z_{0}\right)&space;\\&space;k_{2}=h&space;f\left(x_{0}&plus;\frac{h}{2},&space;y_{0}&plus;\frac{k_{1}}{2},&space;z_{0}&plus;\frac{l_{1}}{2}\right)&space;\\&space;l_{2}=h&space;g\left(x_{0}&plus;\frac{h}{2},&space;y_{0}&plus;\frac{k_{1}}{2},&space;z_{0}&plus;\frac{l_{1}}{2}\right)&space;\\&space;k_{3}=hf\left(x_{0}&plus;\frac{h}{2},&space;y_{0}&plus;\frac{k_{2}}{2},&space;z_{0}&plus;\frac{l_{2}}{2}\right)&space;\\&space;l_{3}=hg&space;\left(x_{0}&plus;\frac{h}{2},&space;y_{0}&plus;\frac{k_{2}}{2},&space;z_{0}&plus;\frac{l_{2}}{2}\right)&space;\\&space;x_{4}=h&space;f\left(x_{0}&plus;h,&space;y_{0}&plus;k_{3},&space;z_{0}&plus;l_{3}\right)\\&space;l_{4}=hg&space;\left(x_{0}&plus;{h},&space;y_{0}&plus;k_{3},&space;z_{0}&plus;l_{3}\right)&space;\\&space;\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{l}&space;k_{1}=h&space;f\left(x_{0},&space;y_{0},&space;z_{0}\right)&space;\\&space;l_{1}=h&space;g\left(x_{0},&space;y_{0},&space;z_{0}\right)&space;\\&space;k_{2}=h&space;f\left(x_{0}&plus;\frac{h}{2},&space;y_{0}&plus;\frac{k_{1}}{2},&space;z_{0}&plus;\frac{l_{1}}{2}\right)&space;\\&space;l_{2}=h&space;g\left(x_{0}&plus;\frac{h}{2},&space;y_{0}&plus;\frac{k_{1}}{2},&space;z_{0}&plus;\frac{l_{1}}{2}\right)&space;\\&space;k_{3}=hf\left(x_{0}&plus;\frac{h}{2},&space;y_{0}&plus;\frac{k_{2}}{2},&space;z_{0}&plus;\frac{l_{2}}{2}\right)&space;\\&space;l_{3}=hg&space;\left(x_{0}&plus;\frac{h}{2},&space;y_{0}&plus;\frac{k_{2}}{2},&space;z_{0}&plus;\frac{l_{2}}{2}\right)&space;\\&space;x_{4}=h&space;f\left(x_{0}&plus;h,&space;y_{0}&plus;k_{3},&space;z_{0}&plus;l_{3}\right)\\&space;l_{4}=hg&space;\left(x_{0}&plus;{h},&space;y_{0}&plus;k_{3},&space;z_{0}&plus;l_{3}\right)&space;\\&space;\end{array}" title="\begin{array}{l} k_{1}=h f\left(x_{0}, y_{0}, z_{0}\right) \\ l_{1}=h g\left(x_{0}, y_{0}, z_{0}\right) \\ k_{2}=h f\left(x_{0}+\frac{h}{2}, y_{0}+\frac{k_{1}}{2}, z_{0}+\frac{l_{1}}{2}\right) \\ l_{2}=h g\left(x_{0}+\frac{h}{2}, y_{0}+\frac{k_{1}}{2}, z_{0}+\frac{l_{1}}{2}\right) \\ k_{3}=hf\left(x_{0}+\frac{h}{2}, y_{0}+\frac{k_{2}}{2}, z_{0}+\frac{l_{2}}{2}\right) \\ l_{3}=hg \left(x_{0}+\frac{h}{2}, y_{0}+\frac{k_{2}}{2}, z_{0}+\frac{l_{2}}{2}\right) \\ x_{4}=h f\left(x_{0}+h, y_{0}+k_{3}, z_{0}+l_{3}\right)\\ l_{4}=hg \left(x_{0}+{h}, y_{0}+k_{3}, z_{0}+l_{3}\right) \\ \end{array}" /></a>

The initial values taken are:

<a href="https://www.codecogs.com/eqnedit.php?latex=\left.R(r)\right|_{r=10^{-4}}=10^{-6},\left.\frac{d&space;R}{d&space;r}\right|_{r=10^{-4}}=-1000" target="_blank"><img src="https://latex.codecogs.com/png.latex?\left.R(r)\right|_{r=10^{-4}}=10^{-6},\left.\frac{d&space;R}{d&space;r}\right|_{r=10^{-4}}=-1000" title="\left.R(r)\right|_{r=10^{-4}}=10^{-6},\left.\frac{d R}{d r}\right|_{r=10^{-4}}=-1000" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\left.y\right|_{x=10^{-4}}=10^{-6},\left.z\right|_{x=10^{-4}}=-1000" target="_blank"><img src="https://latex.codecogs.com/png.latex?\left.y\right|_{x=10^{-4}}=10^{-6},\left.z\right|_{x=10^{-4}}=-1000" title="\left.y\right|_{x=10^{-4}}=10^{-6},\left.z\right|_{x=10^{-4}}=-1000" /></a>

The standard values taken were:

<a href="https://www.codecogs.com/eqnedit.php?latex=\hbar^{2}=7.6199682&space;\mathrm{~m}_{e}&space;\mathrm{eV}&space;.&space;\mathrm{A}^{\circ&space;2}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\hbar^{2}=7.6199682&space;\mathrm{~m}_{e}&space;\mathrm{eV}&space;.&space;\mathrm{A}^{\circ&space;2}" title="\hbar^{2}=7.6199682 \mathrm{~m}_{e} \mathrm{eV} . \mathrm{A}^{\circ 2}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathrm{V}(\mathrm{r})=\frac{\mathrm{e}^{2}}{4&space;\pi&space;\varepsilon_{\mathrm{o}}&space;\mathrm{r}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\mathrm{V}(\mathrm{r})=\frac{\mathrm{e}^{2}}{4&space;\pi&space;\varepsilon_{\mathrm{o}}&space;\mathrm{r}}" title="\mathrm{V}(\mathrm{r})=\frac{\mathrm{e}^{2}}{4 \pi \varepsilon_{\mathrm{o}} \mathrm{r}}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{e^{2}}{4&space;\pi&space;\varepsilon_{0}}=14.39998&space;\mathrm{eV}&space;\cdot&space;\mathrm{A}^{\circ}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{e^{2}}{4&space;\pi&space;\varepsilon_{0}}=14.39998&space;\mathrm{eV}&space;\cdot&space;\mathrm{A}^{\circ}" title="\frac{e^{2}}{4 \pi \varepsilon_{0}}=14.39998 \mathrm{eV} \cdot \mathrm{A}^{\circ}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\mu=\frac{\mathrm{m}_{\mathrm{p}}&space;\mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{p}}&plus;\mathrm{m}_{\mathrm{e}}}&space;\text&space;{&space;for&space;hydrogen&space;atom&space;}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\mu=\frac{\mathrm{m}_{\mathrm{p}}&space;\mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{p}}&plus;\mathrm{m}_{\mathrm{e}}}&space;\text&space;{&space;for&space;hydrogen&space;atom&space;}" title="\mu=\frac{\mathrm{m}_{\mathrm{p}} \mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{p}}+\mathrm{m}_{\mathrm{e}}} \text { for hydrogen atom }" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\mu=\frac{\mathrm{m}_{\mathrm{e}}&space;\mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{e}}&plus;\mathrm{m}_{\mathrm{e}}}=\frac{\mathrm{m}_{\mathrm{e}}}{2}&space;\text&space;{&space;for&space;positronium&space;atom&space;}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\mu=\frac{\mathrm{m}_{\mathrm{e}}&space;\mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{e}}&plus;\mathrm{m}_{\mathrm{e}}}=\frac{\mathrm{m}_{\mathrm{e}}}{2}&space;\text&space;{&space;for&space;positronium&space;atom&space;}" title="\mu=\frac{\mathrm{m}_{\mathrm{e}} \mathrm{m}_{\mathrm{e}}}{\mathrm{m}_{\mathrm{e}}+\mathrm{m}_{\mathrm{e}}}=\frac{\mathrm{m}_{\mathrm{e}}}{2} \text { for positronium atom }" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathrm{m}_{\mathrm{e}}&space;\mathrm{c}^{2}=0.51101&space;\times&space;10^{6}&space;\mathrm{eV}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\mathrm{m}_{\mathrm{e}}&space;\mathrm{c}^{2}=0.51101&space;\times&space;10^{6}&space;\mathrm{eV}" title="\mathrm{m}_{\mathrm{e}} \mathrm{c}^{2}=0.51101 \times 10^{6} \mathrm{eV}" /></a>

---

- **Numerical Analysis for Angular Schrodinger Equation:**

The Schrodinger wave equation can be further written as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\psi(r,&space;\theta,&space;\phi)=R(r)&space;\Theta(\theta)&space;\Phi(\phi)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\psi(r,&space;\theta,&space;\phi)=R(r)&space;\Theta(\theta)&space;\Phi(\phi)" title="\psi(r, \theta, \phi)=R(r) \Theta(\theta) \Phi(\phi)" /></a>

Substituting the above expression and the potential into the spherical polar representation of the wave equation, we find, after some manipulation:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\sin&space;^{2}&space;\theta}{R}&space;\frac{\partial}{\partial&space;r}\left(r^{2}&space;\frac{\partial&space;R}{\partial&space;r}\right)&plus;\frac{\sin&space;\theta}{\Theta}&space;\frac{\partial}{\partial&space;\theta}\left(\sin&space;\theta&space;\frac{\partial&space;\Theta}{\partial&space;\theta}\right)&plus;\frac{2&space;m&space;r^{2}&space;\sin&space;^{2}&space;\theta}{\hbar^{2}}\left(\frac{Z&space;e^{2}}{4&space;\pi&space;\epsilon_{0}&space;r}&plus;E\right)=-\frac{1}{\Phi}&space;\frac{\partial^{2}&space;\Phi}{\partial&space;\phi^{2}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{\sin&space;^{2}&space;\theta}{R}&space;\frac{\partial}{\partial&space;r}\left(r^{2}&space;\frac{\partial&space;R}{\partial&space;r}\right)&plus;\frac{\sin&space;\theta}{\Theta}&space;\frac{\partial}{\partial&space;\theta}\left(\sin&space;\theta&space;\frac{\partial&space;\Theta}{\partial&space;\theta}\right)&plus;\frac{2&space;m&space;r^{2}&space;\sin&space;^{2}&space;\theta}{\hbar^{2}}\left(\frac{Z&space;e^{2}}{4&space;\pi&space;\epsilon_{0}&space;r}&plus;E\right)=-\frac{1}{\Phi}&space;\frac{\partial^{2}&space;\Phi}{\partial&space;\phi^{2}}" title="\frac{\sin ^{2} \theta}{R} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial R}{\partial r}\right)+\frac{\sin \theta}{\Theta} \frac{\partial}{\partial \theta}\left(\sin \theta \frac{\partial \Theta}{\partial \theta}\right)+\frac{2 m r^{2} \sin ^{2} \theta}{\hbar^{2}}\left(\frac{Z e^{2}}{4 \pi \epsilon_{0} r}+E\right)=-\frac{1}{\Phi} \frac{\partial^{2} \Phi}{\partial \phi^{2}}" /></a>

which on further solving, can be reduced into equations dependent on theta and phi respectively as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{1}{\sin&space;\theta}&space;\frac{d}{d&space;\theta}\left(\sin&space;\theta&space;\frac{d&space;\Theta}{d&space;\theta}\right)&plus;\left[l(l&plus;1)-\frac{m_{l}^{2}}{\sin&space;^{2}&space;\theta}\right]&space;\Theta=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{1}{\sin&space;\theta}&space;\frac{d}{d&space;\theta}\left(\sin&space;\theta&space;\frac{d&space;\Theta}{d&space;\theta}\right)&plus;\left[l(l&plus;1)-\frac{m_{l}^{2}}{\sin&space;^{2}&space;\theta}\right]&space;\Theta=0" title="\frac{1}{\sin \theta} \frac{d}{d \theta}\left(\sin \theta \frac{d \Theta}{d \theta}\right)+\left[l(l+1)-\frac{m_{l}^{2}}{\sin ^{2} \theta}\right] \Theta=0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d^{2}&space;\Phi}{d&space;\phi^{2}}-m_{l}^{2}&space;\Phi=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{d^{2}&space;\Phi}{d&space;\phi^{2}}-m_{l}^{2}&space;\Phi=0" title="\frac{d^{2} \Phi}{d \phi^{2}}-m_{l}^{2} \Phi=0" /></a>

Solving these two equations analytically gives us the solution as shown below:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{lll}\ell&space;&&space;m_{\ell}&space;&&space;Y_{\ell&space;m_{l}}(\theta,&space;\phi)=\Theta_{\ell&space;m_{l}}(\theta)&space;\Phi_{m_{l}}(\phi)&space;\\0&space;&&space;0&space;&&space;(1&space;/&space;4&space;\pi)^{1&space;/&space;2}&space;\\1&space;&&space;0&space;&&space;(3&space;/&space;4&space;\pi)^{1&space;/&space;2}&space;\cos&space;\theta&space;\\1&space;&&space;\pm&space;1&space;&&space;\mp(3&space;/&space;8&space;\pi)^{1&space;/&space;2}&space;\sin&space;\theta&space;e^{\pm&space;i&space;\phi}&space;\\2&space;&&space;0&space;&&space;(5&space;/&space;16&space;\pi)^{1&space;/&space;2}\left(3&space;\cos&space;^{2}&space;\theta-1\right)&space;\\2&space;&&space;\pm&space;1&space;&&space;\mp(15&space;/&space;8&space;\pi)^{1&space;/&space;2}&space;\sin&space;\theta&space;\cos&space;\theta&space;e^{\pm&space;i&space;\phi}&space;\\2&space;&&space;\pm&space;2&space;&&space;(15&space;/&space;32&space;\pi)^{1&space;/&space;2}&space;\sin&space;^{2}&space;\theta&space;e^{\pm&space;2&space;i&space;\phi}\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{lll}\ell&space;&&space;m_{\ell}&space;&&space;Y_{\ell&space;m_{l}}(\theta,&space;\phi)=\Theta_{\ell&space;m_{l}}(\theta)&space;\Phi_{m_{l}}(\phi)&space;\\0&space;&&space;0&space;&&space;(1&space;/&space;4&space;\pi)^{1&space;/&space;2}&space;\\1&space;&&space;0&space;&&space;(3&space;/&space;4&space;\pi)^{1&space;/&space;2}&space;\cos&space;\theta&space;\\1&space;&&space;\pm&space;1&space;&&space;\mp(3&space;/&space;8&space;\pi)^{1&space;/&space;2}&space;\sin&space;\theta&space;e^{\pm&space;i&space;\phi}&space;\\2&space;&&space;0&space;&&space;(5&space;/&space;16&space;\pi)^{1&space;/&space;2}\left(3&space;\cos&space;^{2}&space;\theta-1\right)&space;\\2&space;&&space;\pm&space;1&space;&&space;\mp(15&space;/&space;8&space;\pi)^{1&space;/&space;2}&space;\sin&space;\theta&space;\cos&space;\theta&space;e^{\pm&space;i&space;\phi}&space;\\2&space;&&space;\pm&space;2&space;&&space;(15&space;/&space;32&space;\pi)^{1&space;/&space;2}&space;\sin&space;^{2}&space;\theta&space;e^{\pm&space;2&space;i&space;\phi}\end{array}" title="\begin{array}{lll}\ell & m_{\ell} & Y_{\ell m_{l}}(\theta, \phi)=\Theta_{\ell m_{l}}(\theta) \Phi_{m_{l}}(\phi) \\0 & 0 & (1 / 4 \pi)^{1 / 2} \\1 & 0 & (3 / 4 \pi)^{1 / 2} \cos \theta \\1 & \pm 1 & \mp(3 / 8 \pi)^{1 / 2} \sin \theta e^{\pm i \phi} \\2 & 0 & (5 / 16 \pi)^{1 / 2}\left(3 \cos ^{2} \theta-1\right) \\2 & \pm 1 & \mp(15 / 8 \pi)^{1 / 2} \sin \theta \cos \theta e^{\pm i \phi} \\2 & \pm 2 & (15 / 32 \pi)^{1 / 2} \sin ^{2} \theta e^{\pm 2 i \phi}\end{array}" /></a>

In this term paper, the angular part of the Schrodinger wave function is numerically calculated for the p(z) orbital, using the RK4 method. The IVP solved for such a system is :- 

<a href="https://www.codecogs.com/eqnedit.php?latex=\theta=x&space;\\\Theta=y" target="_blank"><img src="https://latex.codecogs.com/png.latex?\theta=x&space;\\\Theta=y" title="\theta=x \\\Theta=y" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{dy}{d&space;x}=z=f(x,&space;y,&space;z)&space;\\\frac{d&space;z}{dx}=-{2&space;y}-{z}*{cotx}&space;=g(x,&space;y,&space;z)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{dy}{d&space;x}=z=f(x,&space;y,&space;z)&space;\\\frac{d&space;z}{dx}=-{2&space;y}-{z}*{cotx}&space;=g(x,&space;y,&space;z)" title="\frac{dy}{d x}=z=f(x, y, z) \\\frac{d z}{dx}=-{2 y}-{z}*{cotx} =g(x, y, z)" /></a>

The  initial values taken were:

<a href="https://www.codecogs.com/eqnedit.php?latex=\theta=\pi/6\\\\\Theta=1.69929\\\\\frac{d&space;\Theta}{d&space;\theta}=0.97745" target="_blank"><img src="https://latex.codecogs.com/png.latex?\theta=\pi/6\\\\\Theta=1.69929\\\\\frac{d&space;\Theta}{d&space;\theta}=0.97745" title="\theta=\pi/6\\\\\Theta=1.69929\\\\\frac{d \Theta}{d \theta}=0.97745" /></a>

---

- **Numerical Analysis for Infinite Potential Well problem:**

A particle is trapped between two regions of infinite potential. The wave function outside the well is zero and it does not jump at it's boundaries.  The Schrodinger equation for such a system is as follows.:-

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d^{2}}{d&space;x}&space;\psi(x)=\frac{-2&space;m_{e}&space;E}{\hbar^{2}}&space;\cdot&space;\psi(x)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{d^{2}}{d&space;x}&space;\psi(x)=\frac{-2&space;m_{e}&space;E}{\hbar^{2}}&space;\cdot&space;\psi(x)" title="\frac{d^{2}}{d x} \psi(x)=\frac{-2 m_{e} E}{\hbar^{2}} \cdot \psi(x)" /></a>

For ease of calculations,

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{c}&space;\text&space;{&space;Let&space;}&space;\left.\left((\hbar^{2}&space;/&space;2&space;m\right)=1\right)&space;\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{c}&space;\text&space;{&space;Let&space;}&space;\left.\left((\hbar^{2}&space;/&space;2&space;m\right)=1\right)&space;\end{array}" title="\begin{array}{c} \text { Let } \left.\left((\hbar^{2} / 2 m\right)=1\right) \end{array}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d^{2}&space;\psi}{d&space;x^{2}}=-E&space;\psi" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{d^{2}&space;\psi}{d&space;x^{2}}=-E&space;\psi" title="\frac{d^{2} \psi}{d x^{2}}=-E \psi" /></a>

Boundary conditions:-

<a href="https://www.codecogs.com/eqnedit.php?latex=\psi(-L&space;/&space;2)=0,&space;\psi(&plus;L&space;/&space;2)=0,&space;E>0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\psi(-L&space;/&space;2)=0,&space;\psi(&plus;L&space;/&space;2)=0,&space;E>0" title="\psi(-L / 2)=0, \psi(+L / 2)=0, E>0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=V(x=-L/2)=\infty,&space;V(x=L/2)=\infty" target="_blank"><img src="https://latex.codecogs.com/png.latex?V(x=-L/2)=\infty,&space;V(x=L/2)=\infty" title="V(x=-L/2)=\infty, V(x=L/2)=\infty" /></a>

Since it is known that the solution to such a problem is symmetrical about the origin, it can be assumed that the wave functions assume the form of a sine or cosine curve, therefore 2 boundary conditions arise:

<a href="https://www.codecogs.com/eqnedit.php?latex=\psi(0)=1,&space;\frac{d&space;\psi(0)}{d&space;x}=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\psi(0)=1,&space;\frac{d&space;\psi(0)}{d&space;x}=0" title="\psi(0)=1, \frac{d \psi(0)}{d x}=0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\psi(0)=0,&space;\frac{d&space;\psi(0)}{d&space;x}=1" target="_blank"><img src="https://latex.codecogs.com/png.latex?\psi(0)=0,&space;\frac{d&space;\psi(0)}{d&space;x}=1" title="\psi(0)=0, \frac{d \psi(0)}{d x}=1" /></a>

---

- **Numerical Analysis for Quantum Harmonic Oscillator:**

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{c}\nu=\frac{\omega_{0}}{2&space;\pi}&space;\\E=\hbar&space;\omega_{0}\left(n&plus;\frac{1}{2}\right)&space;\\\omega=\sqrt{\frac{k}{m}}\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{c}\nu=\frac{\omega_{0}}{2&space;\pi}&space;\\E=\hbar&space;\omega_{0}\left(n&plus;\frac{1}{2}\right)&space;\\\omega=\sqrt{\frac{k}{m}}\end{array}" title="\begin{array}{c}\nu=\frac{\omega_{0}}{2 \pi} \\E=\hbar \omega_{0}\left(n+\frac{1}{2}\right) \\\omega=\sqrt{\frac{k}{m}}\end{array}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=V(x)=\frac{1}{2}&space;k&space;x^{2}=\frac{1}{2}&space;m(\omega&space;x)^{2}" target="_blank"><img src="https://latex.codecogs.com/png.latex?V(x)=\frac{1}{2}&space;k&space;x^{2}=\frac{1}{2}&space;m(\omega&space;x)^{2}" title="V(x)=\frac{1}{2} k x^{2}=\frac{1}{2} m(\omega x)^{2}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{-\hbar}{2&space;m}&space;\frac{d^{2}}{d&space;x^{2}}&space;\psi(x)&plus;\frac{m&space;\omega^{2}}{2}&space;x^{2}&space;\psi(x)=E&space;\psi(x)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{-\hbar}{2&space;m}&space;\frac{d^{2}}{d&space;x^{2}}&space;\psi(x)&plus;\frac{m&space;\omega^{2}}{2}&space;x^{2}&space;\psi(x)=E&space;\psi(x)" title="\frac{-\hbar}{2 m} \frac{d^{2}}{d x^{2}} \psi(x)+\frac{m \omega^{2}}{2} x^{2} \psi(x)=E \psi(x)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\psi(x&space;\rightarrow-\infty)=0,&space;\psi(x&space;\rightarrow&space;\infty)=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\psi(x&space;\rightarrow-\infty)=0,&space;\psi(x&space;\rightarrow&space;\infty)=0" title="\psi(x \rightarrow-\infty)=0, \psi(x \rightarrow \infty)=0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=E=\hbar&space;\omega_{0}\left(n&plus;\frac{1}{2}\right),&space;n=0,1,2&space;\ldots" target="_blank"><img src="https://latex.codecogs.com/png.latex?E=\hbar&space;\omega_{0}\left(n&plus;\frac{1}{2}\right),&space;n=0,1,2&space;\ldots" title="E=\hbar \omega_{0}\left(n+\frac{1}{2}\right), n=0,1,2 \ldots" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a=\sqrt{\frac{\hbar}{m_{e}&space;\omega}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?a=\sqrt{\frac{\hbar}{m_{e}&space;\omega}}" title="a=\sqrt{\frac{\hbar}{m_{e} \omega}}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=y=\frac{x}{a}=\frac{x}{\sqrt{\frac{\hbar}{m&space;\omega}}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?y=\frac{x}{a}=\frac{x}{\sqrt{\frac{\hbar}{m&space;\omega}}}" title="y=\frac{x}{a}=\frac{x}{\sqrt{\frac{\hbar}{m \omega}}}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{E}=\frac{2&space;E}{\hbar&space;\omega}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\hat{E}=\frac{2&space;E}{\hbar&space;\omega}" title="\hat{E}=\frac{2 E}{\hbar \omega}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d^{2}}{d&space;y^{2}}&space;\Psi(y)&plus;y^{2}&space;\Psi(y)=\hat{E}&space;\Psi(y)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\frac{d^{2}}{d&space;y^{2}}&space;\Psi(y)&plus;y^{2}&space;\Psi(y)=\hat{E}&space;\Psi(y)" title="\frac{d^{2}}{d y^{2}} \Psi(y)+y^{2} \Psi(y)=\hat{E} \Psi(y)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{l}\Psi^{\prime}(y)=\Phi&space;\\\Phi^{\prime}(y)=\left(\hat{E}-y^{2}\right)&space;\Psi\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{l}\Psi^{\prime}(y)=\Phi&space;\\\Phi^{\prime}(y)=\left(\hat{E}-y^{2}\right)&space;\Psi\end{array}" title="\begin{array}{l}\Psi^{\prime}(y)=\Phi \\\Phi^{\prime}(y)=\left(\hat{E}-y^{2}\right) \Psi\end{array}" /></a>

Solving the Schrodinger wave equation for simple harmonic oscillator, gives us the function that is proportional to x*e^-x^2, and the graph obtained by the RK4 method also shows such trend where it is 0 at x=0, and then it oscillates around it.  This graph which is obtained from the numerical method aligns with the analytical solution .

---

- **Numerical Analysis for Simple Harmonic Oscillator (Classical Model):**

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{l}m&space;y^{\prime&space;\prime}&plus;k&space;y=0&space;\\y(0)=0,&space;\quad&space;y^{\prime}(0)=1\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{l}m&space;y^{\prime&space;\prime}&plus;k&space;y=0&space;\\y(0)=0,&space;\quad&space;y^{\prime}(0)=1\end{array}" title="\begin{array}{l}m y^{\prime \prime}+k y=0 \\y(0)=0, \quad y^{\prime}(0)=1\end{array}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=y=A&space;\sin&space;\left(\omega_{0}&space;t&plus;\delta\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?y=A&space;\sin&space;\left(\omega_{0}&space;t&plus;\delta\right)" title="y=A \sin \left(\omega_{0} t+\delta\right)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=z^{\prime}(t)=f(t,&space;z(t))" target="_blank"><img src="https://latex.codecogs.com/png.latex?z^{\prime}(t)=f(t,&space;z(t))" title="z^{\prime}(t)=f(t, z(t))" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=z^{\prime}=\left[\begin{array}{l}z_{1}&space;\\z_{2}\end{array}\right]^{\prime}=\left[\begin{array}{c}z_{2}&space;\\\frac{-k}{m}&space;z_{1}\end{array}\right]=f(z)" target="_blank"><img src="https://latex.codecogs.com/png.latex?z^{\prime}=\left[\begin{array}{l}z_{1}&space;\\z_{2}\end{array}\right]^{\prime}=\left[\begin{array}{c}z_{2}&space;\\\frac{-k}{m}&space;z_{1}\end{array}\right]=f(z)" title="z^{\prime}=\left[\begin{array}{l}z_{1} \\z_{2}\end{array}\right]^{\prime}=\left[\begin{array}{c}z_{2} \\\frac{-k}{m} z_{1}\end{array}\right]=f(z)" /></a>

---

- **Numerical Analysis for Damped Harmonic Oscillator (Classical Model):**

Solving the equation for Damped Oscillation gives us:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{array}{l}m&space;y^{\prime&space;\prime}(t)&plus;\gamma&space;y^{\prime}(t)&plus;k&space;y(t)=0\\y(0)=1,&space;\quad&space;y^{\prime}(0)=-1\end{array}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{array}{l}m&space;y^{\prime&space;\prime}(t)&plus;\gamma&space;y^{\prime}(t)&plus;k&space;y(t)=0\\y(0)=1,&space;\quad&space;y^{\prime}(0)=-1\end{array}" title="\begin{array}{l}m y^{\prime \prime}(t)+\gamma y^{\prime}(t)+k y(t)=0\\y(0)=1, \quad y^{\prime}(0)=-1\end{array}" /></a>

The roots of the characteristic equation are:

<a href="https://www.codecogs.com/eqnedit.php?latex=r_{1},&space;r_{2}=\frac{-\gamma&space;\pm&space;\sqrt{\gamma^{2}-4&space;k&space;m}}{2&space;m}" target="_blank"><img src="https://latex.codecogs.com/png.latex?r_{1},&space;r_{2}=\frac{-\gamma&space;\pm&space;\sqrt{\gamma^{2}-4&space;k&space;m}}{2&space;m}" title="r_{1}, r_{2}=\frac{-\gamma \pm \sqrt{\gamma^{2}-4 k m}}{2 m}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=1.&space;\text&space;Over&space;Damped:&space;\&space;\&space;\&space;\gamma^{2}>4&space;k&space;m,&space;where\&space;\&space;\gamma&space;=&space;3\&space;\&space;for&space;\&space;\&space;m&space;=&space;1&space;kg" target="_blank"><img src="https://latex.codecogs.com/png.latex?1.&space;\text&space;Over&space;Damped:&space;\&space;\&space;\&space;\gamma^{2}>4&space;k&space;m,&space;where\&space;\&space;\gamma&space;=&space;3\&space;\&space;for&space;\&space;\&space;m&space;=&space;1&space;kg" title="1. \text Over Damped: \ \ \ \gamma^{2}>4 k m, where\ \ \gamma = 3\ \ for \ \ m = 1 kg" /></a>

where the general solution is:

<a href="https://www.codecogs.com/eqnedit.php?latex=y(t)=c_{1}&space;e^{r_{1}&space;t}&plus;c_{2}&space;e^{r_{2}&space;t}" target="_blank"><img src="https://latex.codecogs.com/png.latex?y(t)=c_{1}&space;e^{r_{1}&space;t}&plus;c_{2}&space;e^{r_{2}&space;t}" title="y(t)=c_{1} e^{r_{1} t}+c_{2} e^{r_{2} t}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=2.&space;Critically&space;Damped:&space;\&space;\&space;\&space;\gamma^{2}=4&space;k&space;m,&space;where\&space;\&space;\gamma&space;=&space;2&space;\&space;for&space;\&space;\&space;m&space;=&space;1&space;kg" target="_blank"><img src="https://latex.codecogs.com/png.latex?2.&space;Critically&space;Damped:&space;\&space;\&space;\&space;\gamma^{2}=4&space;k&space;m,&space;where\&space;\&space;\gamma&space;=&space;2&space;\&space;for&space;\&space;\&space;m&space;=&space;1&space;kg" title="2. Critically Damped: \ \ \ \gamma^{2}=4 k m, where\ \ \gamma = 2 \ for \ \ m = 1 kg" /></a>

where the general solution is:

<a href="https://www.codecogs.com/eqnedit.php?latex=y(t)=c_{1}&space;e^{\gamma&space;t&space;/&space;2&space;m}&plus;c_{2}&space;t&space;e^{\gamma&space;t&space;/&space;2&space;m}" target="_blank"><img src="https://latex.codecogs.com/png.latex?y(t)=c_{1}&space;e^{\gamma&space;t&space;/&space;2&space;m}&plus;c_{2}&space;t&space;e^{\gamma&space;t&space;/&space;2&space;m}" title="y(t)=c_{1} e^{\gamma t / 2 m}+c_{2} t e^{\gamma t / 2 m}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=3.&space;Under&space;Damped:&space;\&space;\&space;\&space;\gamma^{2}<&space;4&space;k&space;m,&space;where\&space;\&space;\gamma&space;=&space;1/2\&space;\&space;for&space;\&space;\&space;m&space;=&space;1&space;kg" target="_blank"><img src="https://latex.codecogs.com/png.latex?3.&space;Under&space;Damped:&space;\&space;\&space;\&space;\gamma^{2}<&space;4&space;k&space;m,&space;where\&space;\&space;\gamma&space;=&space;1/2\&space;\&space;for&space;\&space;\&space;m&space;=&space;1&space;kg" title="3. Under Damped: \ \ \ \gamma^{2}< 4 k m, where\ \ \gamma = 1/2\ \ for \ \ m = 1 kg" /></a>

where the general solution is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{aligned}y(t)&space;&=e^{-\gamma&space;t&space;/&space;2&space;m}\left[c_{1}&space;\cos&space;(\mu&space;t)&plus;c_{2}&space;\sin&space;(\mu&space;t)\right]&space;\\&=R&space;e^{-\gamma&space;t&space;/&space;2&space;m}&space;\sin&space;(\mu&space;t&plus;\delta)\end{aligned}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\begin{aligned}y(t)&space;&=e^{-\gamma&space;t&space;/&space;2&space;m}\left[c_{1}&space;\cos&space;(\mu&space;t)&plus;c_{2}&space;\sin&space;(\mu&space;t)\right]&space;\\&=R&space;e^{-\gamma&space;t&space;/&space;2&space;m}&space;\sin&space;(\mu&space;t&plus;\delta)\end{aligned}" title="\begin{aligned}y(t) &=e^{-\gamma t / 2 m}\left[c_{1} \cos (\mu t)+c_{2} \sin (\mu t)\right] \\&=R e^{-\gamma t / 2 m} \sin (\mu t+\delta)\end{aligned}" /></a>

---

### **Results:**

- **Result for  Radial Schrodinger Equation:**

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathrm{V}(\mathrm{r})=\frac{\mathrm{e}^{2}}{4&space;\pi&space;\varepsilon_{\mathrm{o}}&space;\mathrm{r}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\mathrm{V}(\mathrm{r})=\frac{\mathrm{e}^{2}}{4&space;\pi&space;\varepsilon_{\mathrm{o}}&space;\mathrm{r}}" title="\mathrm{V}(\mathrm{r})=\frac{\mathrm{e}^{2}}{4 \pi \varepsilon_{\mathrm{o}} \mathrm{r}}" /></a>

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

<a href="https://www.codecogs.com/eqnedit.php?latex=\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}&plus;\frac{2}{\mathrm{r}}&space;\frac{\mathrm{d}}{\mathrm{dr}}\right]&space;\mathrm{R}(\mathrm{r})&plus;\frac{2&space;\mu}{\hbar^{2}}\left[\mathrm{E}&plus;\mathrm{V}(\mathrm{r})-\frac{l(l&plus;1)&space;\hbar^{2}}{2&space;\mu&space;\mathrm{r}^{2}}\right]&space;\mathrm{R}(\mathrm{r})=0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}&plus;\frac{2}{\mathrm{r}}&space;\frac{\mathrm{d}}{\mathrm{dr}}\right]&space;\mathrm{R}(\mathrm{r})&plus;\frac{2&space;\mu}{\hbar^{2}}\left[\mathrm{E}&plus;\mathrm{V}(\mathrm{r})-\frac{l(l&plus;1)&space;\hbar^{2}}{2&space;\mu&space;\mathrm{r}^{2}}\right]&space;\mathrm{R}(\mathrm{r})=0" title="\left[\frac{\mathrm{d}^{2}}{\mathrm{dr}^{2}}+\frac{2}{\mathrm{r}} \frac{\mathrm{d}}{\mathrm{dr}}\right] \mathrm{R}(\mathrm{r})+\frac{2 \mu}{\hbar^{2}}\left[\mathrm{E}+\mathrm{V}(\mathrm{r})-\frac{l(l+1) \hbar^{2}}{2 \mu \mathrm{r}^{2}}\right] \mathrm{R}(\mathrm{r})=0" /></a>

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