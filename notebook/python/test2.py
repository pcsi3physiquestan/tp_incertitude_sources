import numpy as np  # Calcul sur les vecteurs numpy
import numpy.random as rd  # Tirages alératoires
import matplotlib.pyplot as plt  # Tracés graphiques


# """
# On rentre les données brutes
# """
# L = 4  # Longueur du tuyau (en cm pour obtenir des cm^3 soit des mL)
# uL = 0.2  # Incertitude sur L
# d = 0.1  # Diamètre

# Vser = np.array([18, 24, 30, 34, 40, 50, 60])  # Volume de la seringue
# uVser = 1  # Demi-largeur de la distribution

# Umin = np.array([5.67, 4.36, 3.58, 3.22, 2.85, 2.34, 2.02])  # Tension min
# Umax = np.array([5.74, 4.46, 3.75, 3.34, 2.91, 2.48, 2.18])  # Tension max
# Umoy = (Umax + Umin) / 2  # Valeur moyenne des tensions
# dU = (Umax - Umin) / 2  # Demi-largeur de la distribution uniforme

# """Coefficient de la relation P = aU + b"""
# a = 218.5  
# b = -107.3

# """Simulation de Monte-Carlo"""

# Vs = []  # On va stocker les vecteurs de valeurs simulées de V dans une liste (une liste de vecteurs donc)
# V_moy = []  # On va stocker les valeurs moyennes des volumes
# V_inc = []  # On va stocker les écart-types des volumes
# invVs = []  # On va stocker les vecteurs de valeurs simulées de 1/V dans une liste (une liste de vecteurs donc)
# invV_moy = []  # On va stocker les valeurs moyennes des 1/V
# invV_inc = []  # On va stocker les écart-types des 1/V

# Ps = []  # On va stocker les vecteurs de valeurs simulées de P dans une liste (une liste de vecteurs donc)
# P_moy = []  # On va stocker les valeurs moyennes des pressions
# P_inc = []  # On va stocker les écart-types des pressions
# Nmes = len(Vser)  # Nombre de mesures réalisées.
# N = 10000  # Nombre de simulations

# for i in range(Nmes):  # Parcours des valeurs mesurées.
#   L_sim = rd.uniform(-uL, uL, N)  # Valeurs simulées de L
#   Vser_sim = rd.uniform(-uVser, uVser, N) + Vser[i]  # Valeurs simulées de Vser

#   V_sim = Vser_sim + np.pi * d ** 2 / 4 * L_sim  # Calcul des valeurs simulées de V
#   Vs.append(V_sim)  # Ajout des valeurs au tableau
#   V_moy.append(np.mean(V_sim))
#   V_inc.append(np.std(V_sim, ddof=1))
    
#   invV_sim = 1 / V_sim  # Calcul des valeurs simulées de 1/V
#   invVs.append(invV_sim)  # Ajout des valeurs au tableau
#   invV_moy.append(np.mean(invV_sim))
#   invV_inc.append(np.std(invV_sim, ddof=1))

#   U_sim = rd.uniform(-dU[i], dU[i], N) + Umoy[i]  # Calcul des valeurs simulées de U
#   P_sim = a * U_sim + b  #Calcul des valeurs simulées
#   Ps.append(P_sim)
#   P_moy.append(np.mean(P_sim))
#   P_inc.append(np.std(P_sim, ddof=1))

# """Tracé de P=f(1/V)"""
# f, ax = plt.subplots()
# f.suptitle("Test de la loi de Mariotte")
# ax.set_xlabel("1/V (mL^-1)")
# ax.set_ylabel("P(hPa)")

# ax.errorbar(invV_moy, P_moy, xerr=invV_inc, yerr=P_inc, label="P(1/V)", marker='+', linestyle='') # Tracé sans relier les points

# ax.legend()
# # plt.show()

# import pandas as pd

# def get_rang(inc):
#   return int(-(np.ceil(np.log10(inc)) - 2))


# def get_aff(mes, inc):
#   nmes = len(mes)
#   return [round(mes[i], get_rang(inc[i])) for i in range(nmes)]

# P_aff = get_aff(P_moy,P_inc)
# V_aff = get_aff(V_moy,V_inc)
# invV_aff = get_aff(invV_moy,invV_inc)

# uP_aff = get_aff(P_inc,P_inc)
# uV_aff = get_aff(V_inc,V_inc)
# uinvV_aff = get_aff(invV_inc,invV_inc)

# donnees2 = pd.DataFrame(
#     {
#         "V(mL)": V_aff,
#         "u(V)(mL)": uV_aff,
#         "1/V(mL^-1)": invV_aff,
#         "u(1/V)(mL^-1)": uinvV_aff,
#         "P(hPa)": P_aff,
#         "u(P)(hPa)": uP_aff,
#     }
# )

# donnees2.style

# """On réalise maintenant l'ajustement linéaire pour chaque groupe d'échantillons simulés."""
# nRTs = []  # On va stocker les pentes
# ordo = []  # On av stocker les ordonnées à l'origine
# for i in range(N):
#   invV = [x[i] for x in invVs]  # On utilise la compréhension de liste pour sélectionner le ième élément pour chaque volume.
#   P = [x[i] for x in Ps]  # On utilise la compréhension de liste pour sélectionner le ième élément pour chaque pression.
#   par = np.polyfit(invV, P, 1)  # Régression linéaire
#   nRTs.append(par[0])  # Stockage de la pente
#   ordo.append(par[1])  # Stockage de l'ordonnée à l'origine

# """Calcul de la moyenne et écart-type"""
# nRT_moy = np.mean(nRTs)  # Moyenne (Estimation de nRT)
# nRT_inc = np.std(nRTs, ddof=1)  # Ecart-type (Estimation de l'incertitude sur nRT)
# ordo_moy = np.mean(ordo)
# ordo_inc = np.std(ordo, ddof=1)

# print("L'ordonnée à l'origine est {:.1f} +/- {:.1f} hPa".format(ordo_moy, ordo_inc))

# P_adj = nRT_moy * np.array(invV_moy) + ordo_moy  # Estimation des valeurs ajustés pour le tracé
# """Remarque : On doit transformer invV_moy en un vecteur numpy pour appliquer une opération à chaque élément."""
# en = (P_moy - P_adj) / P_inc

# """Tracé de P=f(1/V)"""
# f, ax = plt.subplots(1, 2)  # On trace deux graphiques : P(1/V) avec le modèle ajusté et les écarts normalisés
# f.suptitle("Test de la loi de Mariotte")
# ax[0].set_xlabel("1/V (mL^-1)")
# ax[0].set_ylabel("P(hPa)")

# ax[0].errorbar(invV_moy, P_moy, xerr=invV_inc, yerr=P_inc, label="P(1/V)", marker='+', linestyle='', color='red') # Tracé sans relier les points
# ax[0].plot(invV_moy, P_adj, label="Ajustement", linestyle=':', color='blue') # Tracé sans relier les points
# ax[0].legend()

# ax[1].plot(invV_moy, en, label="EN", marker="+", linestyle='')
# ax[1].legend()
# # plt.show()

# R = 8.314  # Constante des gaz parfaits
# T_mes = 30.1
# uT = 1.5
# T_sim = rd.uniform(-uT, uT, N) + T_mes - 273.5  # On simule T en Kelvin

# """On va modifier les unités :
# nRT = PV
# - ici P est en hPa : on multiplie par 10^2
# - V est en mL : on multiplie par 10^-6
# """
# n_sim = nRTs / (R * T_sim) * 1e-4

# n_moy = np.mean(n_sim)
# n_inc = np.std(n_sim, ddof=1)

# print("Nombre de mole. n = {:.2e} +/- {:.1e} mol".format(n_moy, n_inc))


import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd


filename2 = "https://github.com/pcsi3physiquestan/donnees_exp/blob/main/sf6.dat?raw=true"  # Lien vers le fichier de données
datas = np.loadtxt(filename2, skiprows=10, delimiter=",")  # Importation des données
print(datas)

A, C, uC = np.loadtxt(filename, skiprows=1, delimiter=",", usecols=(0, 1, 2))  # Importation des données

"""
Détermination des moyennes et écart-type pour la simulation de Monte-Carlo puis création des N échantillons
"""
n_mes = A.shape[0]  # Nombre de mesures réalisées


"""
Vérification visuelle de l'alignement (approximatifs) des points de mesure.
"""
f, ax = plt.subplots()
f.suptitle("Test visuel de l'alignement des points")
ax.set_xlabel("A(SI)")
ax.set_ylabel("C(10^-5 mol/L)")

ax.errorbar(A, C, yerr=uC, marker='+', markersize=2, linestyle='')


plt.show()
