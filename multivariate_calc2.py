# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:39:44 2019

@author: Owner
"""
print('Exercise 1')
print('(a)')
print()
#Part A
from numpy import *
from matplotlib.pylab import *
#define function for application of trapezium rule
def f(x):
    return 1/(3+x**2)
#define the trapezium rule function with four arguments
def trap_rule(f,a,b,n):
#calculate step size from limits a,b and n trapezoids
    h=(b-a)/n
#can start by summing two end terms
    integral=(f(b)+f(a))/2
#can create loop for summation of all remaining function values 
    for i in range(1,n):
        integral=integral + f(a+h*i)
# now must multiply through by h 
    integral = h*integral
    return integral

#calculate approximation to I between -3,3 with 8 trapezoids
Iapprox=trap_rule(f,-3,3,8)
#calculation of exact value for integral
Iexact=(1/sqrt(3))*(arctan(sqrt(3))-arctan(-sqrt(3)))
#calculation of absolute error in approximation
error=abs(Iexact - Iapprox)
print('Exact Value:',Iexact, 'Approx Value:', Iapprox, 'Absolute Error:', error )
print()

#Part B
print('(b)')
print()
print('Since the error is proportional to h^p, we can express the error E as: E=kh^p.')
print('For two approximations of step size h1 and h2 respectively, the corresponding errors E1 and E2 can be calculated')
print('As such E1=k(h1)^p and E2=k(h2)^p, dividing these two expressions yields: (E1/E2)=(h1/h2)^p')
print('Taking logs and rearranging for p yields p=ln(E1/E2)/ln(h1/h2)')
print('So using python to find the two step widths and corresponding errors, and applying the above equation gives.')
print()
#applying this method we need two step sizes h1 and h2, using the case of 8 and 16 trapezoids:
h1=(3-(-3))/8
h2=(3-(-3))/16
#the error and approximation values for 8 trapezoids is calculated earlier so only need to calculate for 16 trapezoids
I2=trap_rule(f,-3,3,16)
E2=abs(Iexact-I2)
#applying the derived formula
p=log(error/E2)/log(h1/h2)
print('The value for p is', round(p,0), '. Which indicates that the error in the trapezium rule is proportional to the square of the strip width.')
print()
print('We can confirm that the error is proportional the square of the strip width using a for loop to decrease step width, h by factor of 10, and inspect the corresponding errors.')
print()
#As can be seen the error is proportional to the square of the interval width. With a simple for loop to decrease step width we can confirm the order of the method.
#define intital value for number of trapezoids
n=1
#set up loop with sufficient iterations to observe effect of decreasing step size
for i in range(1,6):
#increase number of traezoids by a factor of 10
    n=n*10
    h=(3+3)/n
    I=trap_rule(f,-3,3,n)
    Error=Iexact -I
    print('For an interval width of',h,'the corresponding error in the trapezium rule approximation is', Error )
print()
print('As can be observed decreasing the step width (h) by a factor of 10 sucessively , results in a decrease in the error by a factor of a 100. Which confirms that the error is proportional to the square of the step width, such that p = 2.')

#Part C

print('(c)')
print()
#define function for application of trapezium rule
def f(x):
    return exp(-(cos(x))**2)
print('In order to calculate the integral J correct to 4d.p., a while loop can be used. This will successively calculate approximations with decreasing step width h, and will stop when the difference between two successive approximations is less than 0.00005. Such that the approximations agree to 4d.p. and subsequently the value for the integral is obtained to 4d.p. '  )
print()
#can employ a while loop to increase the number of trapezoids and compare approximations until agreement to 4d.p.
n=1
while error >=0.00005:#an error of less than 0.00005 means agreement to 4d.p. so need while loop to continue calculating approximations whilst the difference to  next approximation is greater than this.
#increase the number of trapezoids by a factor of 10 in each successive iteration
    n=n*10
#command for the calculation of two successive aprroximations
    Jnext=trap_rule(f,0,2,int(n*10))
    J=trap_rule(f,0,2,int(n))
#define error as the difference between successive approximations
    error=abs(Jnext-J)
print('The value of the integral J correct to 4d.p. is ', round(J,4))
print()
print()
print('(d)')
    
    
   
#(d)
#command to produce array of x-values in the interval specified, with sufficient grid points to ensure the fucntion is modelled smoothly
x=linspace(0,5*pi,201)
#define array to store the integral values , calculated using trapezium rule
K=zeros(201)
#set up loop, to add integral values to array
for i in range(0,201,1):
#in the previous exercise agreement to 4d.p. was reached for the approximation using 100 trapezoids, so this seems a sensible number to use for the following calculations.
    K[i]=trap_rule(f,0,x[i],100)
#command to produce plot of the integral against corresponding x-value
plot(x,K)
xlabel('x')
ylabel('K(x)')
title('Integral of exp^(-(cosx)^2) plotted against x, using trapezium rule')
plt.show()
    

#Question 2
print()
print('Exercise 2')
#we need to define a function that implements two successive iterations of the trapezium rule, to approximate a double integral
def double_trap(f,a,b,c,d,nx,ny):#define arguments required: limits for x and y, function f and number of trapezoids: nx and ny.
#define strip width over x and y intervals
    hx = (b-a)/nx
    hy=(d-c)/ny
#we need to define a function in terms of x that computes the inner integral w.r.t y, which we can then apply to the outer integral w.r.t x.
    def g(x):
#sum function values at end points
        g=(f(x,c)+f(x,d))/2
#create loop to successively add function values
        for i in range(1,ny):
            g=g+f(x,c + hy*i)
#multiply through by strip width, 
        g=hy*g
        return g
#we now have a function explicitly in terms of x and we can apply the same trapezium rule formula from the previous exercise.
#sum function values at end points
    Integralg=(g(a)+g(b))/2
#create loop to successively add function values
    for i in range(1,nx):
        Integralg=Integralg+g(a + hx*i)
#multiply through by strip width
    Integralg=hx*Integralg
    return Integralg
print('In order to test the double trapezium rule function that has been written. We can take a double integral with a known analytical solution, and compare this to successive values given by the double trapezium rule function as the step size h is decreased. This will allow us to determine whether the trapezium rule function converges on the correct value and if the function works as expected .')
print()
print('Let us take the double integral of f(x,y) = x^3 + 5y^3, between 0=< x <=2 and 2=< y <=4. This has a known analytical solution of 608.')
print()
print('Creating a loop to decrease the step width hy and hx we can observe the behaviour of the double trap function approximations') 
#define functions of interest with known analytical solution 
def f(x,y):
    return x**3 + 5*(y**3)
#loop to decrease step widths hy and hx and calculate corresponding trapezium rule approximations
n=1
for i in range(1,5):
#increase n by a factor of 5
    n=n*5
#calculate resulting strip widths and double_trap function values
    hy=2/n
    hx=2/n
#calculate successive approximations given by double trap function
    I=double_trap(f,0,2,2,4, n ,n)
    error=608-I
    print( 'Step size (hx,hy):',hy, 'Approximation:', I, 'Error', error)
print()
print('As can be observed the inital approximation to the integral is has a fairly large error. As step size is decreased the error in each output from the double trap function subsequently decreases. Such that we have convergence of the double trap function output towards the exact value. So using this function we can calculate a double integral to the required degree of accuracy by neccessarily reducing the strip width. As such it can be concluded that the function is operating as expected and the double trapezium rule has been implemented correctly in this code.')

      

    
    
    
    
    
    
    