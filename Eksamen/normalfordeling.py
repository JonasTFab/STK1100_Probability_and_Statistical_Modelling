import numpy as np, matplotlib.pyplot as plt

def normalfordeling(x, sigma, mu):
    return 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sigma**2))

def lognormalfordeling(x, sigma, mu):
    return 1/(sigma*x*np.sqrt(2*np.pi)) * np.exp(-(np.log(x)-mu)**2/(2*sigma**2))

n = 1000
x = np.linspace(0,10,n)
x2 = np.linspace(-5,5,n)

mu = 5
sigma = 1

I = int(x[-1]/2)
"""
for i in range(int(len(x)/2)):
    plt.plot([x[i],x[i]], [0,normalfordeling(x[i],sigma,mu)], color="blue")
    plt.plot([x[i]+I,x[i]+I], [0,normalfordeling(x[i]+I,sigma,mu)], color="green")

plt.plot(x, normalfordeling(x,sigma,mu), color="red", label="Normalfordeling")
plt.grid(); plt.legend()
plt.show()
"""

plt.plot(x,lognormalfordeling(x,1.2,0.7), label="Lognormalfordeling")
plt.grid(); plt.legend()
plt.show()
