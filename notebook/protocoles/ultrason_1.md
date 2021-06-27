1. Réaliser le montage :
    * Placement de la source, du récepteur et du réglet
    * Branchement du générateur sur la source au moyen de cables adaptés
    * Branchement du récepteur et du générateur à la console d'acquisition au moyen de cables adaptés.
2. Préparer l'acquisition (_Conseil : décocher l'option "Fermer au lancement de l'acquisition" pour garder cette fenere de réglage durant le TP_):
    * Choisir les voies à acquérir (_icone rouge et noir à droite du graphique_)
        1. Les placer (glisser-déplacer) sur l'axe des ordonnées du petit graphique.
        2. Les nommer clairement (onglet `Grandeur` sous le petit graphique)
        3. Choisir le calibre de chaque voie (le signal ne dépassera pas 10V).
    * Régler la base de temps de l'acquisition
        1. Choisir d'acquérir en fonction du temps (Horloge à placer sur l'axe des abscisses)
        2. Régler la durée d'acquisition (dans `Fonction du temps`) en cohérence avec la manipulation (Comment choisir ce temps ?)
        3. Régler le nombre de points à 10000 (on apprendra plus tard à réfléchir à ce choix).
        4. Cocher `Acquisition continue` de manière à ne pas avoir besoin de relancer l'acquisition à chaque fois.
    * Régler la synchronisation : il faut choisir à quelle valeur démarrera l'affichage des signaux pour observer un signal stable.
        1. Dans `Synchronisation` choisir la `Voie de synchro` correspondant au signal émis.
        2. Choisir une `Niveau` de 1(V) `Croissant`.
    * Vous pouvez maintenant lancer l'acquisition !
3. Alimenter correctement l'émetteur.
    *  Un émetteur ultrasons n'émet un signal d'amplitude importante qu'autour d'une fréquence précise (phénomène de __résonance__).
        1. Régler le générateur pour qu'il délivre en continu (`CONT`) un signal sinusoïdal (`sine`) d'amplitude 10 (__soit 20V pp__), de valeur moyenne (`OFFSET`) nulle et de fréquence autour de 40kHz.
        2. Délivrez le signal en appuyant sur  `On` (la led rouge doit être allumée)
        3. Coller le récepteur à l'émetteur (réception optimale) et observer le signal affiché sur la console.
        4. Modifier lègèrement la fréquence (molette) jusqu'à obtenir un signal d'amplitude maximale : on est à la résonance. Le signal reçu sera maximal.
    * Il faut ensuite arrêter d'émettre en continu.
        1. Passer en mode `gated` pour émettre de manière discontinue (par salve)
        2. Dans `setup` associé, choisir une `source` `manual` et régler `int period` à 1ms.
        3. A chaque fois que vous voudrez déclencher une émission, il suffira d'appuyer sur la touche `MAN TRIG`

_Note :_ __L'utilisation pratique de la console d'acquisition et du générateur Basse Fréquence sont à connaître, on les utilisera beaucoup à l'avenir.__