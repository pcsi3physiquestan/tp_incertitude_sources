---
jupytext:
  formats: ipynb,md:myst
  split_at_heading: true
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

Nous avons déjà commencé à voir comment rendre compte d'une mesure unique avec son incertitude, nous allons maintenant voir comment rendre compte d'un groupe de résultat.

+++

# Rendre compte et exploiter

+++

## Résultat unique
Pour rappel, __un résultat de mesure unique avec incertitude doit s'écrire sous la forme :__

$$
G = (G_{mes} \pm u(G)) Unités
$$

```{margin}
Vous pouvez utiliser des puissances de 10 en facteur si c'est nécessaire.
```
Vous devez respectez les contraintes suivantes :
* L'incertitude de mesure doit avoir 2 chiffres significatifs
* La valeur mesure doit avoir la même précision que l'incertitude ne mesure.


+++

## Ensemble de résultats
Pour rendre compte (afficher proprement) d'un ensemble de résultats, on peut utiliser plusieurs moyens techniques:
```{margin}
Dans les premiers TP, l'utilisation des notebook vous obligera à surtout utiliser numpy pour manipuler un ensemble de résultat.
Les méthodes de compte-rendu seront alors souvent guidées. Etudiez ces méthodes pour pouvoir les reproduire.
```
* tableau markdown dans un notebook (_très verbeux et ne permet pas directement de manipuler les résultats_)
* __tableur (LibreOffice Calc, Excel...) : pratique pour l'affichage ET la manipulation des résultats__

Dans tous les cas, plusieurs points sont à respecter :
* Bien préciser le contenu des colonnes et les __unités__ des grandeurs (en-tête c'est plus simple).
* Si la détermination des __incertitudes de mesure__ est importante, réservez une colonne pour ces dernières.
* Pour un tableur, utilisez les __formules de calcul du logiciel__ plutôt que tout calculer "à la main".

__Dans tous les cas, préfèrez un système (tableur ou numpy) qui permet d'automatiser les calculs à faire sur les résultats.__


+++

## Représentation graphique
Les représentations graphiques sont très utiles pour :
* Faire une synthèse rapide et visuelle des résultats. Possiblement des comparaisons.
* Tester visuellement une relation possible entre deux mesurandes.

````{topic} Moyens techniques
```{margin}
L'utilisation de `matplotlib` n'impose pas l'utilisation de `numpy` mais c'est fortement recommandé.
```
Vous disposerez principalement de trois méthodes pour obtenir des représentations graphiques :
* Logiciel métier associé à un instrument de mesure (console d'acquisition, oscilloscope, spectromètre...)
* Tableur (LibreOffice, Excel)
* __matplotlib__

La bibliothèque `matplotlib.pyplot` sera utilisée en priorité dans un premier temps, c'est pourquoi les exemples d'applications seront présentés avec ce moyen.
````

### Consignes de tracés
Se reporter au [document sur Python](https://pcsi3physiquestan.github.io/intro_python/notebook/plt_presentation.html#methode-generale) pour revoir la structure pour créer un graphique sous Python.

__On se rappellera l'utilisation de `errorbar` pour créer des croix d'incertitudes.__