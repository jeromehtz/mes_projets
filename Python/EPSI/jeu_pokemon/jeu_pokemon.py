## ----- membres du groupe -----
# HERTZOG Jérôme
# NARDOT Noa
# MANIKAKIS Christian
# MAZERON Melvil


class Joueur :
    def __init__(self, nom, manche_gagnee, argent) :
        self.nom = nom
        self.manche_gagnee = manche_gagnee
        self.argent = argent
        self.pokemons = []
    
    def choisir_pokemon(self, liste_pokemons) :
        length_liste_pokemons = len(liste_pokemons)
        legendaire = False
        for i in range(3) :
            print(self.nom+" choisit un pokémon dans la liste ci-dessus : 0 à "+str(length_liste_pokemons-1))
            for i in range(length_liste_pokemons) :
                print("----------------- ["+str(i)+"]")
                liste_pokemons[i].afficher_pokemon()
            ind_pokemon = int(input())
            while ind_pokemon > length_liste_pokemons :
                print("Indice invalide!")
                ind_pokemon = int(input(self.nom+" choisit un pokémon : 0 à "+str(length_liste_pokemons-1)))
            pokemon = liste_pokemons[ind_pokemon]
            while (ind_pokemon > length_liste_pokemons or ind_pokemon<0) or pokemon.prix>=self.argent and legendaire :
                if ind_pokemon > length_liste_pokemons :
                    print("Indice invalide")
                if pokemon.prix>self.argent :
                    print("Vous n'avez pas assez d'argent.")
                elif pokemon.prix == 250 :
                    print("Vous ne pouvez avoir qu'un légendaire dans votre équipe.")
                ind_pokemon = int(input())
                pokemon = liste_pokemons[ind_pokemon]
            
            self.ajouter_pokemon(pokemon)
            liste_pokemons.remove(pokemon)
            self.argent -= pokemon.prix
            if pokemon.prix == 250 :
                legendaire = True
            length_liste_pokemons -= 1
    
    def ajouter_pokemon(self, pokemon) :
        self.pokemons.append(pokemon)
    
    def choisir_attaque(self, pokemon) :
        ind_attaque = int(input("Que doit faire "+pokemon.nom+" ? 0"+" "+str(len(pokemon.attaques)-1)+" "))
        attaque = pokemon.attaques[ind_attaque]
        length_attaques = len(pokemon.attaques)
        while (ind_attaque>length_attaques or ind_attaque<0) or attaque.pp == 0 :
            if attaque.pp == 0 :
                print(attaque+" n'a plus de PP.")
            else :
                print(pokemon.nom+" ne connaît pas cette attaque.")
            print("---")
            print("Attaques du pokémon :", pokemon.attaques)
            attaque = input("Choisissez une attaque parmi cette liste : ")
        return attaque
    
    def recuperer_pokemon(self, numero) :
        return self.pokemons[numero]
    
    def afficher_pokemons(self) :
        for i in range(len(self.pokemons)) :
            print("----------------- ["+str(i)+"]")
            self.pokemons[i].afficher_pokemon()
    
    def afficher_joueur(self) :
        print("--- Joueur ---")
        print("Nom :", self.nom)
        print("Manche(s) gagnée(s) :", self.manche_gagnee)
        print("Argent :", self.argent)

class Pokemon :
    def __init__(self, nom, prix, type, points_de_vie, niveau, attaques, \
                 attaque, defense, attaque_spe, defense_spe, vitesse) :
        self.nom = nom
        self.prix = prix
        self.type = type
        self.pts_vie = points_de_vie
        self.niveau = niveau
        self.attaques = attaques
        
        self.attaque = attaque
        self.defense = defense
        self.attaque_spe = attaque_spe
        self.defense_spe = defense_spe
        self.vitesse = vitesse

    def ajouter_attaque(self, attaque) :
        self.attaques.append(attaque)
    
    def attaquer(self, pokemon, attaque) :
        return attaque.calculer_degats(self, pokemon)
    
    def est_ko(self) :
        return self.pts_vie <= 0
    
    def afficher_attaques(self) :
        for i in range(len(self.attaques)) :
            print("["+str(i)+"]", end = " ")
            self.attaques[i].afficher_attaque()
    
    
    def afficher_pokemon(self) :
        print("Nom :", self.nom)
        print("Prix :", self.prix)
        print("Type :", self.type)
        print("Points de vie :", self.pts_vie)
        print("Niveau :", self.niveau)
        print("Attaque :", self.attaque)

class Attaque :
    def __init__(self, nom, type, categorie, precision, puissance, pp) :
        self.nom = nom
        self.type = type
        self.categorie = categorie
        self.precision = precision
        self.puissance = puissance
        self.pp = pp
    
    def calculer_degats(self, pokemon_attaquant, pokemon_attaque) :
        stab = 1
        if self.type == pokemon_attaquant.type :
            stab = 1.5
        cm = stab * (self.precision/100)
        parethese_1 = pokemon_attaquant.niveau * 0.4 + 2
        parenthese_2 = parethese_1 * pokemon_attaquant.attaque * self.puissance
        parenthese_3 = (pokemon_attaque.defense * 50)
        pv_perdus = (parenthese_2//parenthese_3 + 2) * cm
        print(pokemon_attaque.nom+" perd "+str(pv_perdus))
        return pv_perdus
    
    def afficher_attaque(self) :
        print("--- Attaque ---")
        print("Nom :", self.nom)
        print("Type :", self.type)
        print("Categorie :", self.categorie)
        print("Puissance :", self.puissance)

# Attaques Reshiram
flamme_bleue = Attaque("Flamme bleue", "Feu", "Spéciale", 8, 130, 5)
draco_meteor = Attaque("Draco Meteor", "Dragon", "Spéciale", 90, 130, 5)
extrasenseur = Attaque("Extrasenseur", "Psy", "Spéciale", 100, 80, 20)
machouille = Attaque("Machouille", "Ténèbres", "Physique", 100, 80, 20)
attaques_reshiram = [flamme_bleue, draco_meteor, extrasenseur, machouille]

# Attaques Zekrom
close_combat = Attaque("Close combat", "Combat", "Physique", 100, 120, 5)
#draco meteor
psycho_croc = Attaque("Psycho chroc", "Psy", "Physique", 100, 85, 10)
luminocanon = Attaque("Luminocanon", "Acier", "Spéciale", 100, 80, 20)
attaques_zekrom = [close_combat, draco_meteor, psycho_croc, luminocanon]

# Attaques Zacian
#close_combat
tranche = Attaque("Tranche", "Normal", "Physique", 100, 70, 20)
crocs_eclair = Attaque("Crocs éclair", "Electrik", "Physique", 95, 65, 20)
pouvoir_lunaire = Attaque("Pouvoir lunaire", "Fée", "Spéciale", 100, 95, 10)
attaques_zacian = [close_combat, tranche, crocs_eclair, pouvoir_lunaire]

# Attaques Palkia
hydrocanon = Attaque("Hydrocanon", "Eau", "Spéciale", 80, 110, 5)
spatio_rift = Attaque("Spatio rift", "Dragon", "Spéciale", 95, 100, 5)
tonnerre = Attaque("Tonnerre", "Electrik", "SPéciale", 100, 90, 10)
lance_flammes = Attaque("Lance flammes", "Feu", "Spéciale", 100, 90, 10)
attaques_palkia = [hydrocanon, spatio_rift, tonnerre, lance_flammes]

# Attaques Dracaufeu
deflagration = Attaque("Déflagration", "Feu", "Spéciale", 85, 110, 5)
lance_flammes = Attaque("Lance flammes", "Feu", "Spéciale", 100, 90, 10)
vent_violent = Attaque("Vent violent", "Vol", "Spéciale", 70, 110, 5)
draco_choc = Attaque("Draco choc", "Dragon", "Spéciale", 100, 85, 20)
attaques_dracaufeu = [deflagration, lance_flammes, vent_violent, draco_choc]

# Attaques Ekaiser
vibrecaille = Attaque("Vibrécaille", "Dragon", "Spéciale", 100, 110, 5)
#close combat
poing_glace = Attaque("Poing glace", "Glace", "Physique", 100, 75, 20)
seisme = Attaque("Séisme", "Sol", "Physique", 100, 100, 5)
attaques_ekaiser = [vibrecaille, close_combat, poing_glace, seisme]

# Attaques Rhinastoc
#seisme
lame_de_roc = Attaque("Lame de roc", "Roche", "Physique", 80, 100, 5)
megacorne = Attaque("Mégacorne", "Insecte", "Physique", 85, 120, 5)
#poing glace
attaques_rhinastoc = [seisme, lame_de_roc, megacorne, poing_glace]

# Attaques Oniglali
laser_glace = Attaque("Laser glace", "Glace", "Spéciale", 100, 90, 10)
#seisme
ball_ombre = Attaque("Ball'Ombre", "Spectre", "Spéciale", 100, 80, 20)
#machouille
attaques_oniglali = [laser_glace, seisme, ball_ombre, machouille]

# Attaques Pikachu
fatal_foudre = Attaque("Fatal foudre", "Electrik", "Spéciale", 70, 110, 5)
queue_de_fer = Attaque("Queue de fer", "Acier", "Physique", 75, 100, 5)
tonnerre = Attaque("Tonnerre", "Electrik", "Spéciale", 100, 90, 10)
# TODO : # vive attaque #
vive_attaque = Attaque("Vive attaque", "Normal", "Physique", 100, 40, 20)
attaques_pikachu = [fatal_foudre, queue_de_fer, tonnerre, vive_attaque]

# Attaques Nymphali
#pouvoir lunaire
calinerie = Attaque("Câlinerie", "Fée", "Physique", 90, 90, 10)
plenitude = Attaque("Plénitude", "Fée", "Statut", 100, 0, 20)
eclat_magique = Attaque("Eclat magique", "Fée", "Spéciale", 100, 80, 20)
attaques_nymphali = [pouvoir_lunaire, ball_ombre, calinerie, eclat_magique]


## TODO : pokemons
# 1) les légendaires
reshiram = Pokemon("Reshiram", 250, "Feu", 300, 50, attaques_reshiram, 20, 10, 50, 20, 90)
zekrom = Pokemon("Zekrom", 250, "Dragon", 300, 50, attaques_zekrom, 50, 20, 20, 10, 90)
zacian = Pokemon("Zacian", 250, "Acier", 300, 50, attaques_zacian, 50, 15, 40, 15, 148)
palkia = Pokemon("Palkia", 250, "Dragon", 300, 50, attaques_palkia, 20, 10, 50, 20, 100)

# 2) les pokémon "forts"
dracaufeu = Pokemon("Dracaufeu", 150, "Feu", 250, 50, attaques_dracaufeu, 42, 39, 10, 44, 100)
ekaiser = Pokemon("Ekaîser", 150, "Dragon", 250, 50, attaques_ekaiser, 11, 25, 100, 105, 85)
rhinastoc = Pokemon("Rhinsatoc", 150, "Roche", 250, 50, attaques_rhinastoc, 40, 30, 26, 55, 40)
oniglali = Pokemon("Oniglali", 150, "Glace", 250, 50, attaques_oniglali, 40, 40, 40, 40, 80)
# angoliath = Pokemon("Angoliath", 150, "Ténèbres", 170, 100, ["Attaques d'Angoliath"], 0, 0, 0, 0)
# leviator = Pokemon("Léviator", 150, "Eau", 160, 100, ["attaques de Léviator"], 0, 0, 0, 0)

# 3) les pokémon "moyens"
nymphali = Pokemon("Nymphali", 95, "Fée", 200, 50, attaques_nymphali, 32, 32, 11, 30, 60)
pikachu = Pokemon("Pikachu", 95, "Electrik", 200, 50, attaques_pikachu, 55, 40, 50, 50, 90)

# Les listes
liste_1 = [reshiram, zekrom, dracaufeu, ekaiser, nymphali]
liste_2 = [zacian, palkia, rhinastoc, oniglali, pikachu]

# TODO : classe Jeu
class Jeu :
    def __init__(self, liste_1 = liste_1, liste_2 = liste_2) :
        self.l1 = liste_1
        self.l2 = liste_2



    def jouer(self) :
        print("Chaque joueur doit saisir son nom.")
        nom_joueur_1 = input("Joueur 1 : ")
        nom_joueur_2 = input("Joueur 2 : ")

        joueur_1 = Joueur(nom_joueur_1, 0, 500)
        joueur_2 = Joueur(nom_joueur_2, 0, 500)

        joueur_1.choisir_pokemon(self.l1)
        joueur_2.choisir_pokemon(self.l2)
        print("-----------------------")
        joueur_1.afficher_pokemons()
        print("-----------------------")
        joueur_2.afficher_pokemons()

        length_pokemons_joueur_1 = len(joueur_1.pokemons)
        length_pokemons_joueur_2 = len(joueur_2.pokemons)
        i = 0
        pokemon_j1 = joueur_1.pokemons[i]
        pokemon_j2 = joueur_2.pokemons[i]
        while length_pokemons_joueur_1 >= 2 and length_pokemons_joueur_2 >= 2 :
            ind_pokemon_j1 = i
            ind_pokemon_j2 = i
            while not pokemon_j1.est_ko() and not pokemon_j2.est_ko() :
                print("-------------------------------------------")
                pokemon_j1.afficher_attaques()
                print(pokemon_j1.nom+" attaque "+pokemon_j2.nom)
                print(joueur_1.nom+" choisit une attaque")
                attaque_pokemon_joueur1 = joueur_1.choisir_attaque(pokemon_j1)
                print(pokemon_j2.nom+" attaque "+pokemon_j1.nom)
                print(joueur_2.nom+" choisit une attaque")
                pokemon_j2.afficher_attaques()
                attaque_pokemon_joueur2 = joueur_2.choisir_attaque(pokemon_j2)
                vive_attaque_j1 = (pokemon_j1.attaque == "Vive attaque")
                vive_attaque_j2 = (pokemon_j2.attaque == "Vive attaque")
                if pokemon_j1.vitesse > pokemon_j2.vitesse or (vive_attaque_j1 and not vive_attaque_j2 ) :
                    print(pokemon_j1.nom+" attaque "+pokemon_j2.nom)
                    pv = pokemon_j1.attaquer(pokemon_j2, attaque_pokemon_joueur1)
                    pokemon_j2.pts_vie -= pv
                    print(pokemon_j2.nom+" attaque "+pokemon_j1.nom)
                    pv = pokemon_j2.attaquer(pokemon_j1, attaque_pokemon_joueur2)
                    pokemon_j1.pts_vie -= pv
                elif pokemon_j2.vitesse > pokemon_j1.vitesse or (vive_attaque_j2 and not vive_attaque_j1 ) :
                    print(pokemon_j2.nom+" attaque "+pokemon_j1.nom)
                    pv = pokemon_j2.attaquer(pokemon_j1, attaque_pokemon_joueur2)
                    pokemon_j1.pts_vie -= pv
                    print(pokemon_j1.nom+" attaque "+pokemon_j2.nom)
                    pv = pokemon_j1.attaquer(pokemon_j2, attaque_pokemon_joueur1)
                    pokemon_j2.pts_vie -= pv
                print(pokemon_j1.pts_vie)
                print(pokemon_j2.pts_vie)
            if pokemon_j1.est_ko() :
                print(pokemon_j1.nom+" est KO")
                if ind_pokemon_j1<length_pokemons_joueur_1 :
                    pokemon = joueur_1.pokemons[ind_pokemon_j1+1]
                    ind_pokemon_j2 += 1
                    if ind_pokemon_j2<length_pokemons_joueur_2 :
                        pokemon_j2 = joueur_2.pokemons[ind_pokemon_j2]
                joueur_1.pokemons.remove(pokemon_j1)
                pokemon_j1 = pokemon
                ind_pokemon_j1 = ind_pokemon_j1+1
                length_pokemons_joueur_1 -= 1
                joueur_2.manche_gagnee += 1
            if pokemon_j2.est_ko() :
                print(pokemon_j2.nom+" est KO")
                if ind_pokemon_j2<length_pokemons_joueur_2 :
                    pokemon = joueur_2.pokemons[ind_pokemon_j2+1]
                    ind_pokemon_j1 += 1
                    if ind_pokemon_j1<length_pokemons_joueur_1 :
                        pokemon_j1 = joueur_1.pokemons[ind_pokemon_j1]
                joueur_2.pokemons.remove(pokemon_j2)
                pokemon_j2 = pokemon
                ind_pokemon_j2 = ind_pokemon_j2+1
                length_pokemons_joueur_2 -= 1
                joueur_1.manche_gagnee += 1
            i+=1
        if joueur_1.manche_gagnee >= 2 :
            print(joueur_2.nom+" a gagné.")
        else :
            print(joueur_1.nom+" a gagné.")



