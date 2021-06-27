# -*- coding: utf-8 -*-
from IPython.core.display import Markdown, display
from numpy import *
from matplotlib.pyplot import *
import os


def aff_md(file):
    print(os.getcwd())
    with open(file, 'r') as f:
        s = f.read()
        display(Markdown(s))



def etude_rc():
    """
    On commence par charger les données expérimentales dans une liste `temps`
    """
    filename = "datas/circuit_rc_auto.dat"
    with open(filename, 'r') as file:
        temps = loadtxt(file, delimiter=",", skiprows=1)
        n_mesures = temps.size
        temps = temps / 1000 # On passe les valeurs en millisecondes pour plus de lisibilité

    """ Tracé de l'histogramme des valeurs de tau"""
    f = figure(1)  # On crée une figure
    ax1 = f.add_subplot(1, 1, 1)  # Création des axes du graphiques
    ax1.hist(temps)  # Création de la courbe

    ax1.set_xlabel(r"$t(ms)$")  # Légende des axes

    tau = mean(temps)  # On calcule la valeur moyenne de l'échantillon
    utauA = std(temps, ddof = 1)  # On calcule l'écart-type de la distribution

    return f, tau, utauA


def simul_u(N):
    bins = 100
    m = 3.4
    s = 0.2
    x = linspace(2.5, 4.5, bins)
    fac = 2 * N / bins
    y = fac * 1 / (s * sqrt(2 * pi)) * exp(-1 / 2 * (x - m) ** 2 / s ** 2)
    echs = random.normal(m, s, N)

    f = figure(figsize=(9,6), dpi=100)
    ax = f.add_subplot(1, 1, 1)
    ax.hist(echs, bins)
    ax.plot(x, y, color="black")

    ax.set_xlabel("Valeurs mesurables")
    ax.set_ylabel("Fréquence")
    f.suptitle("Réalisation de N tirages aléatoires gaussiens")
    return f

def gaussienne(m, s):
    # Création des points pour le tracé
    N = 1000
    x = linspace(m - 3 * s, m + 3 * s, N)
    y = 1 / (s * sqrt(4 * pi)) * exp(-1 / 2 * (x - m) ** 2 / s ** 2)
    x2 = linspace(m - 2 * s, m + 2 * s, N)
    y2 = 1 / (s * sqrt(4 * pi)) * exp(-1 / 2 * (x2 - m) ** 2 / s ** 2)


    # Tracé de la figure
    f = figure(figsize=(9, 6), dpi=100)
    ax = f.add_subplot(1, 1, 1)
    ax.plot(x, y, color="blue", label="Loi gaussienne")

    ax.set_xlabel("Valeurs mesurables")
    ax.set_ylabel("Fréquence")
    f.suptitle("Loi gaussienne")

    # Ajouts d'informations
    ymin, ymax = ax.get_ylim()
    ax.plot([m, m], [ymin, ymax], color="black", label="Espérance")
    ax.plot([m - s, m - s, m + s, m + s], [ymax, ymin, ymin, ymax], color="green", label="m - s et m + s", linestyle="--")
    ax.plot([m - 2 * s, m - 2 * s, m + 2 * s, m + 2 * s], [ymax, ymin, ymin, ymax], color="green", label="m - 2s et m + 2s")
    ax.fill_between(x2, y2, color="red", label="Intervalle de confiance à 95%")

    ax.legend()
    return f


def trace_uniforme():
    N = 100000
    bins = 100
    m = -3
    s = 5
    echs = s * random.random(N) + (m - s / 2)

    f = figure()
    ax = f.add_subplot(1, 1, 1)
    ax.hist(echs, bins)

    ax.set_xlabel("Valeurs mesurables")
    ax.set_ylabel("Fréquence")
    f.suptitle("Réalisation de 10000 tirage aléatoires uniformes")
    return f


def combine_incert():
    N = 100000
    bins = 100
    amin = 1.454
    amax = 1.480
    s = (amax + amin) / 2 * 0.005
    echs1 = (amax - amin) * random.random(N) + amin
    echs2 = random.normal(0, s, N)
    echst = echs1 + echs2

    mt = mean(echst)
    st = std(echst, ddof=1)
    print("La distribution des mesures a pour moyenne {:.2f} V et pour écart-type {:.2f} V".format(mt, st))

    f, ax = subplots(1, 3, figsize=(12, 4), dpi=100)
    ax[0].hist(echs1, bins, density=True)
    ax[1].hist(echs2, bins, density=True)
    ax[2].hist(echst, bins, density=True)

    f.suptitle("Réalisation de 100000 tirages aléatoires uniformes")
    return f


def conc_soude():
    N = 1000000  # Nombre d'échantillons
    bins = 1000  # Nombre de batons dans l'histogramme

    # Création des échantillons pour les mesurandes directes.
    cHCl = random.normal(0.02, 0.001, N)
    VHCl = (14.2 - 13.1) * random.random(N) + 13.1
    VHO = random.normal(20, 0.03, N)

    # Simulation des concentrations en soude
    CHO = cHCl * VHCl / VHO

    # Tracé graphique
    f, ax = subplots(1, 1, figsize=(12, 8), dpi=100)
    f.suptitle("Simulation de Monte-Carlo sur le dosage de la soude")
    ax.set_xlabel('C0(mol/L)')
    ax.hist(CHO, bins, label="Concentration en soude")

    cHO = mean(CHO)
    ucHO = std(CHO, ddof=1)
    return f, cHO, ucHO
