import numpy as np


#############################
######## oppgave 3g) ########
#############################
print("###### Oppgave 3g) ######")

mu = 0.7
sigma = 1.2
B = 10000

def y(n, M, S):
    y = np.zeros(n)
    for i in range(n):
        y[i] = np.random.normal(loc=M,scale=S)
    return y

def mu_hat(y_list):
    n = len(y_list)
    return (1/n) * np.sum(y_list)

def s_sqrd(y_list):
    n = len(y_list)
    y_mean = mu_hat(y_list)
    s_sqrd = np.sum((y_list-y_mean)**2) / (n-1)
    return s_sqrd

def eta_star(y_list):
    return np.exp(mu_hat(y_list))

def eta_tilde(y_list):
    n = len(y_list)
    return np.exp(mu_hat(y_list) - s_sqrd(y_list)/(2*n))

n1 = 10
n2 = 30

eta_star_1 = np.zeros(B)
eta_star_2 = np.zeros(B)
eta_tilde_1 = np.zeros(B)
eta_tilde_2 = np.zeros(B)

for i in range(B):
    y1 = y(n1, mu, sigma)
    y2 = y(n2, mu, sigma)
    eta_star_1[i] = eta_star(y1)
    eta_star_2[i] = eta_star(y2)
    eta_tilde_1[i] = eta_tilde(y1)
    eta_tilde_2[i] = eta_tilde(y2)

eta_star_1_mean = np.sum(eta_star_1) / B
eta_star_2_mean = np.sum(eta_star_2) / B
eta_tilde_1_mean = np.sum(eta_tilde_1) / B
eta_tilde_2_mean = np.sum(eta_tilde_2) / B

print("eta = e^mu =                 %.3f" % np.exp(mu))
print("eta* snitt for n=10:         %.3f" % eta_star_1_mean, \
                            "      Relativ feil:   %.2f %%" % \
                            (100*abs(eta_star_1_mean-np.exp(mu))/np.exp(mu)))
print("eta~ snitt for n=10:         %.3f" % eta_tilde_1_mean, \
                            "      Relativ feil:   %.2f %%" % \
                            (100*abs(eta_tilde_1_mean-np.exp(mu))/np.exp(mu)))
print("eta* snitt for n=30:         %.3f" % eta_star_2_mean, \
                            "      Relativ feil:   %.2f %%" % \
                            (100*abs(eta_star_2_mean-np.exp(mu))/np.exp(mu)))
print("eta~ snitt for n=30:         %.3f" % eta_tilde_2_mean, \
                            "      Relativ feil:   %.2f %%" % \
                            (100*abs(eta_tilde_2_mean-np.exp(mu))/np.exp(mu)))





#############################
######## oppgave 4c) ########
#############################
print("")
print("###### Oppgave 4c) ######")

forbruk = np.array([1.0, 3.4, 5.0, 14.4, 11.5, 8.2, 0.6, 2.7, 26.8, 3.0,
                    1.3, 20.2, 4.0, 14.0, 3.3, 1.8, 1.7, 4.6, 7.4, 7.1,
                    5.2, 23.6, 1.6, 1.1, 15.5, 3.0, 1.9, 4.2, 27.4, 1.5])
ln_forbruk = np.log(forbruk)
N = len(forbruk)

median_estimat = eta_tilde(ln_forbruk)
print("Estimert median:                         %.2f" % median_estimat)

y_snitt = mu_hat(ln_forbruk)
s = np.sqrt(s_sqrd(ln_forbruk))

nedre_ki_median = np.exp(y_snitt - 1.96*s/np.sqrt(N))
ovre_ki_median = np.exp(y_snitt + 1.96*s/np.sqrt(N))
print("Konfidensintervall for medianen:         [%.2f, %.2f]" % \
                                        (nedre_ki_median, ovre_ki_median))


forv_estimat = median_estimat * np.exp(s**2/2)
print("Estimert forventning:                    %.2f" % forv_estimat)

nedre_ki_forv = np.exp(y_snitt - 1.96*s/np.sqrt(N) + s**2/2)
ovre_ki_forv = np.exp(y_snitt + 1.96*s/np.sqrt(N) + s**2/2)
print("Konfidensintervall for forventningen:    [%.2f, %.2f]" % \
                                        (nedre_ki_forv, ovre_ki_forv))





#############################
######## oppgave 4d) ########
#############################
print("")
print("###### Oppgave 4d) ######")

median_boot = np.zeros(B)
forv_boot = np.zeros(B)

for i in range(B):
    y_boot = y(N, y_snitt, s)
    s_boot = np.sqrt(s_sqrd(y_boot))
    median_boot[i] = eta_tilde(y_boot)
    forv_boot[i] = median_boot[i] * np.exp(s_boot**2/2)

median_boot_mean = mu_hat(median_boot)
median_std = np.sqrt(1/(B-1) * np.sum((median_boot - median_boot_mean)**2))
forv_boot_mean = mu_hat(forv_boot)
forv_std = np.sqrt(1/(B-1) * np.sum((forv_boot - forv_boot_mean)**2))

print("Standardfeil til median:                 %.2f" % median_std)
print("Standardfeil til forventning:            %.2f" % forv_std)



"""
Resultater:
###### Oppgave 3g) ######
eta = e^mu =                 2.014
eta* snitt for n=10:         2.160       Relativ feil:   7.28 %
eta~ snitt for n=10:         2.012       Relativ feil:   0.09 %
eta* snitt for n=30:         2.051       Relativ feil:   1.86 %
eta~ snitt for n=30:         2.002       Relativ feil:   0.56 %

###### Oppgave 4c) ######
Estimert median:                         4.40
Konfidensintervall for medianen:         [3.07, 6.56]
Estimert forventning:                    7.74
Konfidensintervall for forventningen:    [5.39, 11.55]

###### Oppgave 4d) ######
Standardfeil til median:                 0.88
Standardfeil til forventning:            1.97
"""
