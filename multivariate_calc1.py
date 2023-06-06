# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:51:15 2019

@author: Owner
"""
from numpy import *
from matplotlib.pylab import*
print('Exercise 1 - Forward Difference Method')
print('(a)')
#define function for which forward difference method shall be applied
def f(x):
    return exp(-x**2)
#define number of points for method over given interval
n=100
a=-2
b=2
#define array for x-values, and corresponding function values over interval [a,b]
x=linspace(a,b,n+1)
y=zeros(n+1)
for i in range(n+1):
    y[i]=f(x[i])
#define array of zeros to store derivative values
dydx=zeros(n+1)
#calculate step size for points over interval [a,b]
h=(b-a)/n
#calculate derivative at each point employing forward difference method, and assign to array
for i in range(n):
    dydx[i]=(y[i+1]-y[i])/h
#must use alternative form of expression for derivative at end point since we do not have a value for y[n+1]
dydx[n]=(y[n]-y[n-1])/h
#can define an array to store error values for derivatives
error=zeros(n+1)
#calculate error at each point and store to array 
for i in range(n+1):
    error[i]=(-2*x[i]*exp(-x[i]**2))-dydx[i]
#create command for plotting error against corresponding x-values  
plot(x,error)
xlabel('x')
ylabel('Error')
title('Error in the forward difference method for e^(-x^2)')
plt.show()
#create loop to find maximum error and corresponding x-value
maxerror=0
for i in range(n+1):
    if abs(error[i])>maxerror:
        maxerror=abs(error[i])
        xmax=x[i]
print('The maximum absolute error in the forward difference method across the interval investigated is', maxerror,'and this occurs at an x-value of xmax=',xmax )
print()
print('(b)')
#can create loop to decrease step size as specified and calculate subsequent derivative and corresponding error.
for i in range(1,13,1):
    h=(10)**(-i)
    derivxmax=(f(xmax+h)-f(xmax))/h
    errorxmax=((-2*xmax*exp(-xmax**2))-derivxmax)
    print('For a step size of', h, 'the corresponding error is', errorxmax)
print()
print('It can be observed that as step size h is decreased by a factor of 10 in each subsequent approximation, the error in the approximations is also seen to decrease by roughly a factor of 10. Which is to be expected as the error in the forward difference method is proportional to the step size.')
print()



print('Exercise 2 - Centred Difference Method')
#Exercise 2 - Centred Difference Method
print('(a)')
#define function 
def g(x):
    return tan(x*sin(x))
#can define interval and suitable number of steps 
a=-1
b=1
n=50
#define array of x-values, and functions values
x=linspace(a,b,n+1)
y=zeros(n+1)
for i in range(n+1):
    y[i]=g(x[i])
#define array for storage of derivative values
dydx=zeros(n+1)
#calculate step size h over the interval [a,b]
h=(b-a)/n
#create loop to calculate derivative and assign to array
for i in range(n):
    dydx[i]=(y[i+1]-y[i-1])/(2*h)
#need to define the derivative differently at the end points since we have no value for y[n+1]and y[-1]
dydx[0]=(y[1]-y[0])/(h)
dydx[n]=(y[n]-y[n-1])/(h)
#can create command to produce plot for function values and derivatives
plot(x,dydx,'r')
plot(x,y,'b')
xlabel('x')
ylabel('y')
title('Plot showing g(x)=tan(xsinx) and gdash(x) using central difference method')
legend(['gdash(x)','g(x)'])
plt.show()
print('(b)')
#define x-value of interest
x=-0.5
#can produce an array to store derivative values for each decreasing step size
derivx=[]
#create loop with sufficient step decreases to calculate derivatives for agreement to 4d.p.
for i in range(1,11,1):
    h=10**(-i)
    deriv=(g(x+h)-g(x-h))/(2*h)
    derivx.append(deriv)
# create loop to find successive approximations that agree to 4d.p and print output. This is achieved by comparing differences between successive values in array.
for i in range(1,10,1):
    h=10**(-i)
    if abs(derivx[i]-derivx[i-1])<=0.00005:
        print('The value of the derivative at x=-0.5 correct to four decimal places is',round(derivx[i],4), 'which occurs at a step size of', h )
        break
print()
print('The required step size needed to achieve agreement to 4d.p. and as such reduce the error to 0.00005 using the central difference method is 0.01. Using the forward difference to reduce the error to below 0.00005 and achieve agreement to 4d.p., a step size of less than 0.0001 was needed. It can be seen that the step size using the forward difference for a given accuracy is roughly the square of the step size using the central difference. Which is expected given one method is first order and one method is second order.' )       
print()




#Exercise 3 - Partial Derivatives
print('Exercise 3 - Partial Derivatives')
print('(a)')
print('My scheme is partialdfdx=(f(x[i+1],y[i])-f(x[i-1],y[i]))/2h')
print('My scheme is partialdfdy=(f(x[i],y[i+1])-f(x[i],y[i-1]))/2h')
print()
#can define function of two variables
def f(x,y):
    return sin(x*arccos(y))
#define x and y values for subsequent approximations
x=1
y=0.5
#can define arrays to store partial derivative values as step size is reduced
partialdfdx=[]
partialdfdy=[]
#define loop to reduce step size and calculate subsequent partial derivatives, which are stored to array. Sufficient iterations are specified to ensure agreement of values to 4d.p.
for i in range(1,13,1):
    h=10**(-i)
    partdfdx=(f(x+h,y)-f(x-h,y))/(2*h)
    partdfdy=(f(x,y+h)-f(x,y-h))/(2*h)
    partialdfdx.append(partdfdx)
    partialdfdy.append(partdfdy)
#define loop to cycle through derivative values, which prints value when agreement to 4d.p. is reached
for i in range(1,12,1):
    if abs(partialdfdx[i]-partialdfdx[i-1]) and abs(partialdfdy[i]-partialdfdy[i-1]) <=0.00005:
        print('The partial derivative of f w.r.t x correct to 4d.p. is',round(partialdfdx[i],4))
        print('The partial derivative of f w.r.t y correct to 4d.p. is',round(partialdfdy[i],4))
        break
print()
#to analyse the order of the method we can analyse the error in the approximations. For this we need the exact derivative value which are defined as follows.
dfdxexact=arccos(y)*cos(x*arccos(y))
dfdyexact=(-x/(sqrt(1-y**2)))*cos(x*arccos(y))
#define loop to calculate error with decreasing step size, for approximated partial derivatives
for i in range(1,5,1):
    h=10**(-i)
    approxdfdx=(f(x+h,y)-f(x-h,y))/(2*h)
    approxdfdy=(f(x,y+h)-f(x,y-h))/(2*h)
    errorx=dfdxexact-approxdfdx
    errory=dfdyexact-approxdfdy
    print('Step size',h,'Error Partial dfdx:', errorx, 'Error Partial dfdy:', errory)
print()
print('As can be seen above, reducing the step size by a factor of 10 reduces the error in both approximations by a factor of 100. As such the the error in the approximations is proportional to the square of the step size, which confirms the method is second order accurate')
#to calculate the directional derivative we need the unit vector in the direction v=2i-j, for this we need the magnitude of v.
magv=sqrt((2**2)+(1**2))
#calculation for the directional derivative
dd=(1/magv)*(partialdfdx[i]*2+(-partialdfdy[i]))
print()
print('The value for the directional derivative correct to 4 d.p. is', round(dd,4))
    

    
    


