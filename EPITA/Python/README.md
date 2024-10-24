Dans ce dossier, il y quelques-uns de mes projets personnels et des programmes que j'ai conçu à l'EPITA.
J'ai pris soin de ne pas tout mettre, pour les droits et pour mettre seulement les plus cohérents.

# Multiplication par 11
Ne pas utiliser la multiplication par 11  
Ni ajouter le nombre 11 fois  
## Principe :
prenons 99.  
  -> on fait une addition avec retenues de chaque chiffre du nombre 2 à 2 voisins en  
  gardant les extremités en ajoutant la retenue pour l'extremité gauche.  
  
  Pour 99, cela se fait en 3 étapes :   
    - on écarte le 9 de droite  
    - 9+9 = 18 => retenue = 1 car 18>9   
    - donc on a pour le moment 89   
    - et du coup, puisque l'on a une retenue de 1, 9+1 = 10   
    => 99*11 = 1089  
  autre exemple : 243*11 = 2673, je vous laisse vérifier  
