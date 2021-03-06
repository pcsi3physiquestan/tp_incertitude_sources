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


filename2 = "../../../../../approche_numeriques/donnees_exp/lambert.dat"  # Lien vers le fichier de données

A, C, uC = np.loadtxt(filename2, skiprows=1, delimiter=",", unpack=True)  # Importation des données

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


# plt.show()


# Simulation des N tirages
N = 1000000
C_sim = rd.normal(C, uC, (N, n_mes))  # On génère directement un tableau où les colonnes correspondent à une mesure de C.

# Réalisation des régression linéaire. polyfit peut faire les N régressions, tant que les abscisses ne changent pas
# Ce qui est le cas ici
# On doit par contre transposer le tableau des valeurs de C (inverser lignes et colonnes)
p_sim = np.polyfit(A, C_sim.transpose(), 1)


pente_m = np.mean(p_sim[0])
ordo_m = np.mean(p_sim[1])
pente_u = np.std(p_sim[0], ddof=1)
ordo_u = np.std(p_sim[1], ddof=1)

print("-----------------------------")
print("Pente = {:.4f} +/- {:.4f} 10^-5 mol/L".format(pente_m, pente_u))
print("Ordonnée à l'origine = {:.4f} +/- {:.4f} 10^-5 mol/L".format(ordo_m, ordo_u))
print("-----------------------------")

"""
Histogrammes des valeurs simulées
"""
f, ax = plt.subplots(1, 2, figsize=(9, 6))
f.suptitle("Distribution des valeurs simulées")

# Pente
ax[0].set_xlabel('Pente(1e-5 mol/L)')
ax[0].hist(p_sim[0], bins='rice')

# Pente
ax[1].set_xlabel('Ordonnée(1e-5 mol/L)')
ax[1].hist(p_sim[1], bins='rice')

# plt.show()

"""
Vérification de l'ajustement par tracé graphique et calcul des écarts normalisés.
"""
f, ax = plt.subplots(2, 1, figsize=(9, 6), sharex='col')  # Tracé en partageant les abscisses sur les deux axes.
f.suptitle("Ajustement linéaire")

"""
Tracé de la droite d'ajustment
On va pousser plus loin l'analyse en estimant l'incertitude sur les points ajustés.
On s'en servira dans les écarts normalisés notamment.
"""

C_adj_sim = np.zeros((N, n_mes))
for i in range(n_mes):
    C_adj_sim[:, i] = p_sim[0] * A[i] + p_sim[1]  # Calcul des N valeurs ajustées pour chaque distance


C_adj_m = C_adj_sim.mean(axis=0)  # Moyenne sur les N valeurs (suivant les colonnes :  axis = 0)
C_adj_u = C_adj_sim.std(ddof=1, axis=0)  # Moyenne sur les N valeurs (suivant les colonnes :  axis = 0)

ax[0].set_xlabel("A")
ax[0].set_ylabel("C(1e-5 mol/L)")
ax[0].errorbar(A, C, yerr=uC, marker='+', markersize=2, linestyle='')
ax[0].plot(A, C_adj_m, linestyle=':', linewidth=1, color='red')


"""Tracé des écarts normalisés"""
en = (C - C_adj_m) / (np.sqrt(uC ** 2 + C_adj_u ** 2))


ax[1].set_xlabel("A")
ax[1].set_ylabel("EN")
ax[1].plot(A, en, linestyle='', marker='+', color='red')


# plt.show()


A_test = 0.523  # Distance en centimètre
C_sim = p_sim[0] * A_test + p_sim[1]  # Simulation des concentrations

C_m = np.mean(C_sim)  # Estimation de la concentration moyenne
C_u = np.std(C_sim, ddof=1)  # Estimation de l'écart-type

print("-----------------------------")
print("Concentration estimée = ({:.3f} +/- {:.3f}) 10^-5 mol/L".format(C_m, C_u))
print("-----------------------------")

NA = 100
A_courbe = np.linspace(min(A), max(A), NA)  # On trace les fuseaux pour la zone d'étude.

"""
On reprend la même méthode que précédemment mais pour chaque valeur de A. On va donc obtenir 
un vecteur de valeurs pour C et son incertitude
"""

C_courbe_sim = np.zeros((NA, N))  # Tableau de 0 où on va stocker les valeurs simulées de C pour chaque absorbance
for i in range(NA):
    C_courbe_sim[i] = p_sim[0] * A_courbe[i] + p_sim[1]  # Simulation des concentrations pour chaque valeur de A

C_courbe_m = np.mean(C_courbe_sim, axis=1)  # Estimation de la concentration moyenne pour chaque valeur de A (par colonne)
C_courbe_u = np.std(C_courbe_sim, ddof=1, axis=1)  # Estimation de l'écart-type pour chaque valeur de A (par colonne=)

C_mean = pente_m * A_courbe + ordo_m  # Droite ajustée
C_min = C_courbe_m - C_courbe_u # Limite basse des valeurs données par l'incertitude
C_max = C_courbe_m + C_courbe_u # Limite basse des valeurs données par l'incertitude

"""
Tracé graphique de la droite d'étalonnage avec le fuseau donnant les incertitudes
"""
f, ax = plt.subplots()
f.suptitle("Courbe d'étalonnage pour dosage par absorbance")
ax.set_xlabel("A")
ax.set_ylabel("C(10^-5 mol/L)")

ax.plot(A_courbe, C_mean, label="Droite étalon", color='black', linewidth=1)  # Droite d'ajustement

# Première méthode : on trace les deux courbes hautes et basses
ax.plot(A_courbe, C_min, color='blue', linewidth=.5)  # Cmes - u(C)
ax.plot(A_courbe, C_max, color='blue', linewidth=.5)  # Cmes + u(C)

# Deuxième méthode : la fonction fill_between, remplit de couleur l'espace entre 2 courbes
ax.fill_between(A_courbe, C_min, C_max, color='cyan', linewidth=1, label="Incertitudes sur la concentration")

ax.legend()
plt.show()