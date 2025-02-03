"""

Michel BUI

Classe: TG6

Devoir à la Maison n°1 - Jeu des Allumettes (P.O.O)

"""

import random


class Joueur:

    # constructeur
    def __init__(self, nom, score = 0):
        """
        Modifications :
            Affecte le nom à la propriété Nom, et
            à la propriété score.
        """
        self.Nom = nom # Attribut : nom de l'objet
        self.Score = score # Attribut : score de l'objet


class JeuAllumettes:

    # constructeur
    def __init__(self, joueurs, NbAllumettes):
        """
        Modifications :
            Demande le nom au premier joueur, et au second joueur.
            Affecte à la propriété Joueurs une liste contenant deux
            instances d'objet Joueur avec les bons noms.
            Puis, exécute la méthode Lancer()
        """

        self.Joueurs = joueurs # Attribut : liste de tous les objets joueurs (ici il y en a 2)
        self.NbAllumettes = NbAllumettes # Attribut : Nombre total d'allumettes

    def afficherScores(self):
        """
        Modification :
            Affiche le score actuel des deux joueurs.
        """

        print("",
              "\nTableau des scores :")

        for num_joueur in range(1, len(self.Joueurs)+1): # On sélectionne chaque joueur à partir d'une boucle for

            print(f"    Le joueur {num_joueur}" + " " + f"({self.Joueurs[num_joueur-1].Nom}) a un score de : {self.Joueurs[num_joueur-1].Score} pts") # On affiche le score du joueur selectionné par la boucle

    def gagnant(self, n):
        """
        Paramètres :
            n est le numéro du joueur gagnant (0 ou 1)
        Modification :
            Affiche le joueur gagnant, augmente son score, et affiche
            l'ensemble des scores
        """
        print(f"Le joueur gagnant est {self.Joueurs[n].Nom} ! GG ") # Affiche le joueur gagnant de la partie

        self.Joueurs[n].Score += 1 # Augmente le score du joueur gagnant de 1

        self.afficherScores() # Affiche le score total des joueurs dans le jeu

    def faireJouer(self, n):
        """
        Paramètres :
            n est le numéro du joueur gagnant (0 ou 1)
        Modification :
            Demande au joueur en question le nombre d'allumettes à prendre.
            Celui-ci doit être entre 1 et 3, et ne pas dépasser le nombre
            d'allumettes encore en jeu.

            Affiche le nombre d'allumettes effectivement retirées
            Affiche le nombre d'allumettes restantes
        """
        nbAllumettes_retirees = int(input(f"{self.Joueurs[n].Nom} , combien d'allumettes souhaitez-vous prendre ? Sélectionnez un chiffre entre 1 et 3 !")) # Demande au joueur le nombre d'allumettes qu'il souhaite retirer entre 1 et 3

        if nbAllumettes_retirees > 3 or nbAllumettes_retirees < 1: # Si ce n'est pas entre 1 et 3 allumettes

            while nbAllumettes_retirees > 3 or nbAllumettes_retirees < 1: # Boucle while qui redemande dans le cas où le joueur souhaite retirer plus que 3 allumettes ou un nombre inexistant d'allumettes...

                nbAllumettes_retirees = int(input(f"{self.Joueurs[n].Nom} , combien d'allumettes souhaitez-vous prendre ? SELECTIONNEZ UN CHIFFRE ENTRE 1 ET 3 !!!"))

        if self.NbAllumettes == 2: # Si le nombre d'allumettes restantes sur la table est égal à 2, le joueur doit retirer au maximum 2 allumettes dans la logique.

            while nbAllumettes_retirees > 2 or nbAllumettes_retirees < 1: # Tant que le joueur n'a pas souhaiter retirer 1 ou 2 allumettes

                nbAllumettes_retirees = int(input(f"{self.Joueurs[n].Nom} , combien d'allumettes souhaitez-vous prendre ? SELECTIONNEZ UN CHIFFRE ENTRE 1 ET 2 !!!")) # Demande au joueur le nombre d'allumettes qu'il souhaite retirer entre 1 et 2



        self.NbAllumettes = self.NbAllumettes - nbAllumettes_retirees # Le joueur retire le nombre d'allumettes du tas d'allumettes  totales disposées sur la table.

        print(f"    {self.Joueurs[n].Nom} retire {nbAllumettes_retirees} allumettes",
              f"\n    Il reste {self.NbAllumettes} allumettes en jeu.")

    def Lancer(self):
        """
        Modifications :
            Lance la partie, en commençant de manière aléatoire entre l'un
            ou l'autre joueur.
            Fait jouer chaque joueur alternativement et contrôle le gagnant.
            Si la partie est finie, propose une nouvelle partie.
        """

        n = random.randint(0,1) # variable n contenant le chiffre aléatoire (entre 0 et 1) qui permet de déterminer le joueur qui commence dès le début de la partie

        self.faireJouer(n) # Le joueur n joue son tour

        if self.NbAllumettes > 1: # S'il reste plus qu'une seule allumette sur la table, on poursuit la partie.

            while self.NbAllumettes > 1:

                if n == 0: # Si le joueur 0 a déjà joué, c'est au tour du joueur 1
                    n = 1
                    self.faireJouer(n) # On fait jouer le joueur 1

                else: # Sinon, si le joueur 1 a déjà joué, c'est au tour du joueur 2
                    n = 0
                    self.faireJouer(n) # Le joueur 2 joue son tour

        self.gagnant(n) # Le joueur n a gagné

        relancer_partie = str(input(" Une autre partie ? (o pour oui) (n pour non)")) # proposition à l'utilisateur de relancer une nouvelle partie

        if relancer_partie == "o": # Si le joueur répond par 'o', une nouvelle partie commence

            self.NbAllumettes = int(input("Combien d'allumettes pour cette partie ?")) # Demande le nombre d'allumettes disposées sur la table pour la nouvelle partie

            self.Lancer() # La partie se lance

        else:
            print("GAME OVER") # Affiche "GAME OVER" si l'utilisateur ne veut pas relancer une nouvelle partie.





# Tests

NbAllumettes = int(input("Combien d'allumettes pour cette partie ?")) # Demande le nombre d'allumettes qu'on veut dans la partie.

joueurs = [] # Liste des joueurs

for num_joueur in range(1, 3): # Boucle for qui rajoute dans la liste des joueurs, chaque nom des joueurs. Ici il y en a 2 dans la partie

    nom = str(input(f"Donnez le nom du joueur {num_joueur}:")) # Demande le nom de l'utilisateur

    joueurs.append(Joueur(nom)) # Ajoute le nom du joueur dans la liste des joueurs

print(f"    Il y a initialement {NbAllumettes} allumettes en jeu.")

JeuAllumettes(joueurs, NbAllumettes).Lancer() # Permet de lancer la partie du jeu des allumettes