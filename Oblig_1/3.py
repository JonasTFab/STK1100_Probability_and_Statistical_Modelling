import numpy as np, matplotlib.pyplot as plt

data = np.loadtxt("dodssannsynlighet-felles.txt",skiprows=1)
sorted = np.transpose(data)

alder = sorted[0]
dod = sorted[1]/1000


############ oppgave 3c) ############
def punktsannsynlighet(x,q):
    if x==0:
        return q[x]
    else:
        prod=(1-q[0])
        for y in range(x-1):
            prod *= (1-q[y+1])
        return q[x]*prod

pkt_san = np.zeros(len(alder))
for i in range(len(alder)):
    pkt_san[i] = punktsannsynlighet(int(alder[i]),dod)

# Sum av punktsannsynlighet skal vaere lik 1. Sjekker om det er
# sant i etterfolgende print
print("Sum over punktsannsynlighetene: ", sum(pkt_san))

plt.plot(alder[35:],pkt_san[35:]*1000)
plt.grid(); plt.xlabel("Alder i aar"); plt.ylabel(r"Sannsynlighet i promille")
plt.title("Punktsannsynlighet")
#plt.show()


############ oppgave 3e) ############
def h(X):
    if X<32:
        return 0
    else:
        return (100000/1.03**32) * (1-(1/1.03)**(X-31)) / (1-1/1.03)

E_h = 0
for i in range(72):
    E_h += h(i)*pkt_san[i+35]

print("Forventet naaverdi av pensjonsutbetaling: %.1f" % E_h)

############ oppgave 3g) ############
def g(X):
    if X<=31:
        return (1-(1/1.03)**(X+1)) / (1-1/1.03)
    else:
        return (1-(1/1.03)**(32)) / (1-1/1.03)

E_g = 0
for i in range(72):
    E_g += g(i)*pkt_san[i+35]

print("Forventet naaverdi av premieinnbetalingene: %.2f" % E_g)
plt.show()


"""
Utskrift fra terminal:
Sum over punktsannsynlighetene:  1.0
Forventet naaverdi av pensjonsutbetaling: 495929.1
Forventet naaverdi av premieinnbetalingene: 20.37
"""
