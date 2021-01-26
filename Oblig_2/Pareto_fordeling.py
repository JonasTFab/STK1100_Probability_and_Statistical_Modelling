import numpy as np, matplotlib.pyplot as plt, random as r


######### oppgave c) #########
# genererer et uniformt tilfeldig tall mellom 0 og 1
def U():
    return r.random()

kap = 4e5
theta = 3

N = int(1e5)
X = np.zeros(N)

# Regner ut verdier for x mellom kappa og 2e6
for i in range(len(X)):
    X[i] = kap / (1-U())**(1/theta)

med = np.median(np.sort(X))
snitt = sum(X)/len(X)
print("Median:          %i" % med)
print("Gjennomsnitt:    %i" % snitt)
print("")

"""
In [24]: run Pareto_fordeling.py
Median:          504570
Gjennomsnitt:    600880

Vi ser at verdiene vi faar er veldig naer de vi fant i oppgave 1c) som tilsvarer:
Median:          503968
Forventet:       600000
"""


######### oppgave d) #########
plt.xlim(int(3e5), int(2e6))
plt.hist(X, bins=200, normed=True, edgecolor="black", label="Pareto observasjon")
#plt.show()



######### oppgave e) #########
def f(x):
    return theta * kap**(theta) * x**(-theta-1)
x = np.linspace(kap,2e6,N)
plt.plot(x,f(x), label="Pareto tetthet")
plt.legend(); plt.grid(); plt.xscale("linear")
plt.show()
