import numpy as np
import matplotlib.pyplot as plt
import math as mt

def cond_check(m):
    p=np.array([4,7])
    return np.matmul(p,m)**2 >=(np.linalg.norm(p)**2-9)

num=0
radius=3
p=np.array([4,7])
norm_p=np.linalg.norm(p)
m_lim1=p/mt.sqrt(norm_p**2-9)
m_lim2=-p/mt.sqrt(norm_p**2-9)
theta_line=np.linspace(0,mt.pi/2,20)

for theta in theta_line:
    m=np.array([mt.cos(theta),mt.sin(theta)])
    if cond_check(m):
        lambda_1=-np.matmul(p,m)+mt.sqrt((np.matmul(p,m)**2)+9-norm_p**2)
        lambda_2=-np.matmul(p,m)-mt.sqrt((np.matmul(p,m)**2)+9-norm_p**2)
        A=p+lambda_1*m
        B=p+lambda_2*m
        PA_PB=np.linalg.norm(p-A)*np.linalg.norm(p-B)
        print('m=',m,'   '+'PA.PB=',PA_PB)
        plt.plot(np.array([p[0],A[0],B[0]]),np.array([p[1],A[1],B[1]]))
        plt.text(A[0]*(1+0.1),A[1]*(1-0.1),'A'+str(num))
        plt.text(B[0]*(1+0.1),B[1]*(1-0.1),'B'+str(num))
        num=num+1
theta=np.linspace(0,2*mt.pi,100)        
plt.plot(radius*np.cos(theta),radius*np.sin(theta))
plt.plot(p[0],p[1])
plt.text(p[0],p[1],'P')
plt.grid()
plt.show()
