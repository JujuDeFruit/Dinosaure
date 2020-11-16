"""Main"""
#Créé par Andy Valla et Julien Raynal dans le cadre du projet final du bac d'ISN

# Importation des bibliothèques et des autres pages python nécessaires
import pygame
from pygame.locals import *
from variable import *
from random import randint

pygame.init()   # initiliser le module python (point de départ)


fenetre = pygame.display.set_mode((fenetre_largeur,fenetre_hauteur))     # création de la fenêtre
pygame.display.set_caption("DINO-DINO  !!")     #set_caption pour le nom de la fenêtre

icone = pygame.image.load('image/dinosaure.png')     #charger l'image du dino
pygame.display.set_icon(icone)      #set_icon pour mettre l'image du dino à côté du titre de la fenêtre


#Chargemnt de toutes les images
mascotte = pygame.image.load('image/dinosaure.png').convert_alpha()     #convert_alpha permet à la partie de l'image non désirée de devenir invisible
mascotte2 = pygame.image.load('image/dinosaure2.png').convert_alpha()
licence = pygame.image.load('image/LicenceISN.png').convert()
fond1 = pygame.image.load("image/fond1.jpeg").convert()
fond2 = pygame.image.load("image/fond1.jpeg").convert()
perso = pygame.image.load('image/transparence.png')
cactus = pygame.image.load('image/cactus.png').convert_alpha()
piaf = pygame.image.load('image/piaf.png').convert_alpha()
ecran_score = pygame.image.load('image/game_over.png').convert()
pouvoir = pygame.image.load('image/pouvoir.png').convert_alpha()
bouclier = pygame.image.load('image/bouclier.png')
coeur1 = pygame.image.load('image/coeur.png').convert_alpha()
coeur2 = pygame.image.load('image/coeur.png').convert_alpha()
coeur3 = pygame.image.load('image/coeur.png').convert_alpha()
fond_perso = pygame.image.load('image/selection perso.png').convert()
MmeCornetBerry = pygame.image.load('image/MmeCornetBerry.png').convert_alpha()
MrSchneider = pygame.image.load('image/MrSchneider.png').convert_alpha()
Andy = pygame.image.load('image/Andy.png').convert_alpha()
Julien = pygame.image.load('image/JuJu.png').convert_alpha()



largeur_fond1 = fond1.get_width()       #récuperer la largeur de l'image de fond
largeur_cactus = cactus.get_width()     #récuperer la largeur de l'image du cactus
largeur_oiseau = piaf.get_width()       #récuperer la largeur de l'image de l'oiseau



aleatoire_cactus = randint(1,3)         #récupération d'un nombre aléatoire entre 1 et 3 qui permettra de faire apparaître un cactus
aleatoire_oiseau = randint(1,3)         #récupération d'un nombre aléatoire entre 1 et 3 qui permettra de faire apparaitre un oiseau



pygame.time.set_timer(USEREVENT, temps_apparition_cactus)     #Evenements générant les obstacles continuellement avec un intervalle de temps donné
pygame.time.set_timer(USEREVENT + 1, temps_apparition_oiseau)
pygame.time.set_timer(USEREVENT + 2, temps_apparition_pouvoir)


pygame.display.flip()       #recharge la fenêtre de jeu


pygame.mixer.music.load(musique)        #Chargement de la musique
pygame.mixer.music.play(-1, 0.0)        #La musique est jouée infiniment sans délai

while jeu == True :     # Tant que le jeu est actif, création du boléen

    if game_over == False :         #Si l'utilisateur lance le jeu, la musique de jeu se lance
        musique = "Sons/son_jeu.ogg"
        pygame.mixer.music.load(musique)    #Chargement de la musique
        pygame.mixer.music.play(-1, 0.0)    #Musique jouée indéfiniment sans délai


    while game_over == False :   # Tant que l'utilisateur n'a pas perdu

            score +=0.05        #la variable score augmente

            #défilement du paysage
            if fond1_x > 0 or fond2_x >= 0 :
                fond1_x -= vitesse_fond     #L'abscisse du fond 1 diminue
                fond2_x -= vitesse_fond     #L'abscisse du fond 2 diminue
                pygame.time.delay(5)        #limitation des rafraîchissements de la page de 5 milliseconde

            if fond1_x <= -(largeur_fond1) :    #si jamais l'image sort de la fenêtre elle retourne à sa position intiale
                fond1_x = largeur_fond1

            if fond2_x <= -(largeur_fond1) :    #si jamais l'image sort de la fenêtre elle retourne à sa position intiale
                fond2_x = largeur_fond1


            #Apparition des obstacles

            if aleatoire_cactus == 1 or aleatoire_cactus == 2 :
                if cactus_x > -(largeur_cactus) :
                    cactus_x -= vitesse_fond        #faire avancer le cactus

            if cactus_x <= -(largeur_cactus) :
                cactus_x = fenetre_largeur + 1
                aleatoire_cactus = 3                 #si le cactus sort de la fenêtre alors il retourne à sa position intitiale, et son abscisse ne diminue plus

            if aleatoire_oiseau == 1 or aleatoire_oiseau == 2 :
                if oiseau_x > -(largeur_oiseau)  :
                    oiseau_x -= vitesse_fond + 2    #l'oiseaux va plus vite que le cactus de 2 pixels

            if oiseau_x <= -(largeur_oiseau) :
                oiseau_x = fenetre_largeur + 1
                aleatoire_oiseau = 3                #L'abscisse de l'oiseau ne diminue plus

            #boucle qui traite les évenements dans le jeu

            for event in pygame.event.get() :
                if event.type == QUIT :
                    jeu = False             #on vérifie les boléens
                    game_over = True
                    selection_perso = False
                    ecran_de_fin = False

                if event.type == KEYDOWN :           #si l'évenement est une touche appuyé
                    if event.key == K_ESCAPE :
                        jeu = True          #On ouvre ou on ferme les boucles
                        game_over = True
                        selection_perso = True
                        ecran_de_fin = False
                        pygame.mixer.music.stop()       #Arrêt de la musique précédente
                        musique = "Sons/son_perso.ogg"
                        pygame.mixer.music.load(musique)    #Lancement de la nouvelle musique
                        pygame.mixer.music.play(-1, 0.0)




                if event.type == USEREVENT :   #defilement obstacles
                    if cactus_x == fenetre_largeur + 1 :
                        aleatoire_cactus = randint(1,3) # création nombre aléatoire pour l'apparition du cactus



                if event.type == USEREVENT + 1 : # création nombre aléatoire pour l'apparition de l'oiseau
                    if oiseau_x == fenetre_largeur +1 :
                        oiseau_y = randint(180,206)     #la hauteur aléatoire où sera placé l'oiseau
                        aleatoire_oiseau = randint(1,3)


                if event.type == USEREVENT + 2 :
                    if pouvoir_x == fenetre_largeur + 1 :
                        aleatoire_pouvoir = randint(1,3)



            tkey = pygame.key.get_pressed() #Lors d'un appui sur un évènement (Touche du clavier ou clic de la souris)

            if mouvement_recul == 0 :   # Création du recul, si aucune touche n'est enfoncée, le perso recul avec une vitesse égale a celle du fond défilant
                perso_x -= vitesse_fond


            if tkey[K_UP]: #Déplacement vers le haut
                if saut < 1 :       #Personnage limité à 2 sauts
                    perso_y -= 50   #L'abscisse du personnage diminue à chaque rafraîchissement
                    saut += 1


            if tkey[K_DOWN] : #Deplacement vers le bas
                    perso_y += 10

            if tkey[K_RIGHT] :  #Déplacement vers la droite
                    perso_x += (10 + vitesse_fond)
                    if tkey[K_UP] : # Deplacement en haut à droite
                            if saut < 2 :
                                perso_y -= 50
                                saut +=1

            if tkey[K_LEFT] : #Deplacement à gauche
                    perso_x -= (10 + vitesse_fond)
                    if tkey[K_UP] : # Déplacement en haut à gauche
                        if saut < 2 :
                            perso_y -= 50
                            saut += 1


            # Coordonnées pour que le perso ne sorte pas du cadre
            limite_droite_cadre = largeur_fond1 - perso.get_width()     #Largeur de l'image de fond moins la largeur de l'image du personnage
            if perso_y > 243 :      #Limite inférieure
                perso_y = 243
            if perso_y < 120 :      #Limite supérieure
                perso_y = 120
            if perso_x < 0 :        #Limite gauche
                perso_x = 0
            if perso_x > limite_droite_cadre :      #Limite droite
                perso_x = limite_droite_cadre

            if perso_y == 243 : # réinitialisation de la variable saut pour que le perso ne puisse sauter que 2 fois
                saut = 0  #Réinitialisation du saut lorsque le perso touche le sol
                acceleration = 0.0005
            if perso_y != 243:      #Si le personnage est en l'air
                if saut != 0 :      #lorsque le perso redescend, il redescend de plus en plus vite
                    perso_y += acceleration
                    acceleration += acceleration_supplementaire # Augmentation de l'accélération


                #Collisions
            if bonus == False and collisions == True :      #lorsque le perso redescend, il redescend de plus en plus vite

                if  oiseau_x < perso_x < oiseau_x + piaf.get_width() : #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if  oiseau_y < perso_y < oiseau_y + piaf.get_height() :
                                vie -= 1        #on perd un coeur
                                invulnerabilite += 1    #pour éviter de se prendre 2 obstacles en même temps, si invulnérable = 1, alors le personnage ne peut pas rencontrer d'autres obstacles pendant un certain temps
                                oiseau_x = fenetre_largeur + 1      #si un obstacle est touché il revient au début
                                aleatoire_oiseau = 3                # et n'avance plus

                if  oiseau_x < perso_x + (perso.get_width())/2 < oiseau_x + piaf.get_width() : #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if  oiseau_y < perso_y < oiseau_y + piaf.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                oiseau_x = fenetre_largeur + 1
                                aleatoire_oiseau = 3

                if  oiseau_x < perso_x + (perso.get_width())*0.75 < oiseau_x + piaf.get_width() : #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if  oiseau_y < perso_y < oiseau_y + piaf.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                oiseau_x = fenetre_largeur + 1
                                aleatoire_oiseau = 3

                if oiseau_x < perso_x + perso.get_width() < oiseau_x + piaf.get_width() : #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if oiseau_y < perso_y < oiseau_y + piaf.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                oiseau_x = fenetre_largeur + 1
                                aleatoire_oiseau = 3

                if oiseau_x < perso_x + perso.get_width()/2 < oiseau_x + piaf.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if oiseau_y < perso_y + perso.get_height() < oiseau_y + piaf.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                oiseau_x = fenetre_largeur + 1
                                aleatoire_oiseau = 3

                if oiseau_x < perso_x + perso.get_width() < oiseau_x + piaf.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if oiseau_y < perso_y + (perso.get_height())/2 < oiseau_y + piaf.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                oiseau_x = fenetre_largeur + 1
                                aleatoire_oiseau = 3

                if oiseau_x < perso_x + perso.get_width() < oiseau_x + piaf.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if oiseau_y < perso_y + perso.get_height() < oiseau_y + piaf.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                oiseau_x = fenetre_largeur + 1
                                aleatoire_oiseau = 3

                if oiseau_x < perso_x < oiseau_x + piaf.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if oiseau_y < perso_y + perso.get_height()/2 < oiseau_y + piaf.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                oiseau_x = fenetre_largeur + 1
                                aleatoire_oiseau = 3

                if oiseau_x < perso_x < oiseau_x + piaf.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if oiseau_y < perso_y + perso.get_height()*0.75 < oiseau_y + piaf.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                oiseau_x = fenetre_largeur + 1
                                aleatoire_oiseau = 3

                if oiseau_x < perso_x < oiseau_x + piaf.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées de l'oiseau, il y a game over
                        if oiseau_y < perso_y + perso.get_height() < oiseau_y + piaf.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                oiseau_x = fenetre_largeur + 1
                                aleatoire_oiseau = 3

                if cactus_x < perso_x < cactus_x + cactus.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées du cactus, il y a game over
                        if cactus_y < perso_y + perso.get_height() <= cactus_y + cactus.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                cactus_x = fenetre_largeur + 1
                                aleatoire_cactus = 3

                if cactus_x < perso_x + perso.get_width() < cactus_x + cactus.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées du cactus, il y a game over
                        if cactus_y < perso_y + perso.get_height() <= cactus_y + cactus.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                cactus_x = fenetre_largeur + 1
                                aleatoire_cactus = 3

                if cactus_x < perso_x + perso.get_width() < cactus_x + cactus.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées du cactus, il y a game over
                        if cactus_y < perso_y <= cactus_y + cactus.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                cactus_x = fenetre_largeur + 1
                                aleatoire_cactus = 3

                if cactus_x < perso_x < cactus_x + cactus.get_width() :  #Si les coordonnées du perso se retrouvent dans les coordonnées du cactus, il y a game over
                        if cactus_y < perso_y <= cactus_y + cactus.get_height() :
                                vie -= 1
                                invulnerabilite += 1
                                cactus_x = fenetre_largeur + 1
                                aleatoire_cactus = 3

            #Réglage de l'imunité pour éviter le bug de la double collision
            if invulnerabilite == 0 :
                temps_invulnerabilite = 0       #Remise à zéro de la variable temps de l'invulnérabilité

            if  invulnerabilite == 1  :     #Si le personnage est rentré en collision avec un obstacle
                temps_invulnerabilite += 0.05
                collisions = False          #Le personnage perd pas deux coeurs

            if temps_invulnerabilite >= 3 :     #Limite du temps de l'invulnérabilité
                collisions = True
                invulnerabilite = 0

            if bonus == False :
                if aleatoire_pouvoir == 1 :                                     #Création du bonus, si le nombre aléatoire sorti est 1, le bonus apparait a l'écran
                    if pouvoir_x > -(pouvoir.get_width()) :                     # Si le bonus est dans l'écran
                        vitesse_bonus = vitesse_bonus_reelle                    #Réinitialisation de la vitesse du bonus
                        pouvoir_x -= vitesse_bonus                              #Déplacement du bonus par diminution de l'abscisse de l'image


                #Collisions avec le bonus
                if pouvoir_x <= -(pouvoir.get_width()) :            # Si le bonus sort de l'écran, il est réinitialisé à sa position initiale avec une vitesse de 0
                    pouvoir_x = fenetre_largeur + 1
                    aleatoire_pouvoir = 2

                if pouvoir_x < perso_x < pouvoir_x + pouvoir.get_width():      # Colisions entre le bonus et le perso. Si il y a collisions, la vitesse du bonus est de 0 et sa position est
                    if pouvoir_y < perso_y < pouvoir_y + pouvoir.get_height() :#réinitialisée. De plus, le bonus a été ramassé, donc la boucle if bonus == True, est vraie
                        bonus = True
                        pouvoir_x = fenetre_largeur + 1
                        aleatoire_pouvoir = 2
                        vitesse_bonus = 0

                if pouvoir_x < perso_x + perso.get_width() < pouvoir_x + pouvoir.get_width() :
                    if pouvoir_y < perso_y < pouvoir_y + pouvoir.get_height() :
                        bonus = True
                        pouvoir_x = fenetre_largeur + 1
                        aleatoire_pouvoir = 2
                        vitesse_bonus = 0

                if pouvoir_x < perso_x + perso.get_width()/2 < pouvoir_x + pouvoir.get_width() :
                    if pouvoir_y < perso_y < pouvoir_y + pouvoir.get_height() :
                        bonus = True
                        pouvoir_x = fenetre_largeur + 1
                        aleatoire_pouvoir = 2
                        vitesse_bonus = 0

                if pouvoir_x < perso_x + perso.get_width()*0.75 < pouvoir_x + pouvoir.get_width() :     # 0.75 pour voir plusieurs pixels pour les collisions et pas que les coins
                    if pouvoir_y < perso_y < pouvoir_y + pouvoir.get_height() :
                        bonus = True
                        pouvoir_x = fenetre_largeur + 1
                        aleatoire_pouvoir = 2
                        vitesse_bonus = 0

                if pouvoir_x < perso_x < pouvoir_x + pouvoir.get_width() :
                    if pouvoir_y < perso_y + perso.get_height() < pouvoir_y + pouvoir.get_height() :
                        bonus = True
                        pouvoir_x = fenetre_largeur + 1
                        aleatoire_pouvoir = 2
                        vitesse_bonus = 0

                if pouvoir_x < perso_x < pouvoir_x + pouvoir.get_width() :
                    if pouvoir_y < perso_y + perso.get_height()/2 < pouvoir_y + pouvoir.get_height() :
                        bonus = True
                        pouvoir_x = fenetre_largeur + 1
                        aleatoire_pouvoir = 2
                        vitesse_bonus = 0

                if pouvoir_x < perso_x < pouvoir_x + pouvoir.get_width() :
                    if pouvoir_y < perso_y + perso.get_height()*0.75 < pouvoir_y + pouvoir.get_height() :
                        bonus = True
                        pouvoir_x = fenetre_largeur + 1
                        aleatoire_pouvoir = 2
                        vitesse_bonus = 0

                if pouvoir_x < perso_x + perso.get_width() < pouvoir_x + pouvoir.get_width() :
                    if pouvoir_y < perso_y + perso.get_height() < pouvoir_y + pouvoir.get_height() :
                        bonus = True
                        pouvoir_x = fenetre_largeur + 1
                        aleatoire_pouvoir = 2
                        vitesse_bonus = 0



            if vie == 0 :                       #Si le personnage n'a plus de coeur
                game_over = True                #Fermeture de la boucle
                pygame.mixer.music.stop()
                musique = "Sons/bruit game over.ogg"    #Lancement du son de game over
                pygame.mixer.music.load(musique)
                pygame.mixer.music.play(1, 0.0)         #Son joué une seule fois sans délai
                jeu = True
                selection_perso = False                 #L'utilisateur est ammené à l'écran de fin
                ecran_de_fin = True

            if bonus == True :               #Si le personnage attrape le bonus, cela ouvre la boucle bonus


                temps_bonus += 1             #Temps durant lequel le bonus est actif
                if temps_bonus > 500 :     # Si le temps du bonus est supérieur à 500, le personnage ne possède plus le bonus
                    bonus = False           # Lorsque le temps est fini, la boucle bonus == True n'est plus d'actualité et le bonus peut réapparaitre
                    temps_bonus = 0         # Le temps du bonus se remet à 0

                if  oiseau_x < perso_x < oiseau_x + piaf.get_width() :      #Si le coin en haut à gauche de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oideau
                    if  oiseau_y < perso_y < oiseau_y + piaf.get_height() : # Si le coin en haut à gauche de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1                      # Alors l'oiseau est remis à son abscisse d'origine
                        oiseau_y = randint(180,206)                         #Le bonus se met à une hauteur aléatoire accessible au personnage
                        aleatoire_oiseau = 3                                # Le nombre aléatoire est égal à 3 pour que le bonus ne bouge plus
                        score += 10                                         # l'oiseau est remis à sa position initiale
                        game_over = False                                   #Lorsque l'oiseau rentre encollisions avec l'obstacle l'utilisateur ne perds pas

                if oiseau_x < perso_x + perso.get_width() < oiseau_x + piaf.get_width() :    #Si le coin en haut à droite de l'image du personnage rentre dans les coorsdonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y < oiseau_y + piaf.get_height() :                   #Si le coin en haut à droite de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if oiseau_x < perso_x + (perso.get_width())/2 < oiseau_x + piaf.get_width() :   #Si la moitié de la largeur en haut de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y < oiseau_y + piaf.get_height() :                      #Si la moitié de la largeur en haut de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if oiseau_x < perso_x + (perso.get_width())*0.75 < oiseau_x + piaf.get_width() :   #Si la partie droite en haut de l'image du personnage rentre dans les coorcdonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y < oiseau_y + piaf.get_height() :                         #Si la partie droite en haut de l'image du personnage rentre dans les coorcdonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if oiseau_x < perso_x < oiseau_x + piaf.get_width() :                               #Si le coin en bas à gauche de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y + perso.get_height() < oiseau_y + piaf.get_height() :     #Si le coin en bas à gauche de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if oiseau_x < perso_x < oiseau_x + piaf.get_width() :                                   #Si la partie gauche en bas de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y + (perso.get_height())*0.75 < oiseau_y + piaf.get_height() :  #Si la partie gauche en bas de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if oiseau_x < perso_x < oiseau_x + piaf.get_width() :                                   #Si la partie gauche en haut de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y + (perso.get_height())/0.25 < oiseau_y + piaf.get_height() :  #Si la partie gauche en haut de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if oiseau_x < perso_x + perso.get_width() < oiseau_x + piaf.get_width() :       #Si le coin en bas à droite de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y + perso.get_height() < oiseau_y + piaf.get_height() : #Si le coin en bas à droite de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if oiseau_x < perso_x + perso.get_width()/2 < oiseau_x + piaf.get_width() :     #Si la partie basse de la moitié de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y + perso.get_height() < oiseau_y + piaf.get_height() : #Si la partie basse de la moitié de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if oiseau_x < perso_x + perso.get_width() < oiseau_x + piaf.get_width() :           #Si la partie gauche de la moitié de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y + perso.get_height()/2 < oiseau_y + piaf.get_height() :   #Si la partie gauche de la moitié de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if oiseau_x < perso_x + perso.get_width() < oiseau_x + piaf.get_width() :               #Si la partie gauche et basse de l'image du personnage rentre dans les coordonnées de l'axe des abscisses de l'oiseau
                    if oiseau_y < perso_y + perso.get_height()*0.75 < oiseau_y + piaf.get_height() :    #Si la partie gauche et basse de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées de l'oiseau
                        oiseau_x = fenetre_largeur + 1
                        oiseau_y = randint(180,206)
                        aleatoire_oiseau = 3
                        score += 10
                        game_over = False

                if cactus_x < perso_x < cactus_x + cactus.get_width() :                                 #Si le coin gauche en bas de l'image du personnage rentre dans les coordonnées de l'axe des abscisses du cactus
                    if cactus_y < perso_y + perso.get_height() <= cactus_y + cactus.get_height() :      #Si le coin gauche en bas de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées du cactus
                        cactus_x = fenetre_largeur + 1
                        cactus_y = 270
                        aleatoire_cactus = 3
                        score += 10
                        game_over = False

                if cactus_x < perso_x + perso.get_width() < cactus_x + cactus.get_width() :         #Si le coin droite en bas de l'image du personnage rentre dans les coordonnées de l'axe des abscisses du cactus
                    if cactus_y < perso_y + perso.get_height() <= cactus_y + cactus.get_height() :  #Si le coin droite en bas de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées du cactus
                        cactus_x = fenetre_largeur + 1
                        cactus_y = 270
                        aleatoire_cactus = 3
                        score += 10
                        game_over = False

                if cactus_x < perso_x < cactus_x + cactus.get_width() :         #Si le coin en haut à gauche de l'image du personnage rentre dans les coordonnées de l'axe des abscisses du cactus
                    if cactus_y < perso_y <= cactus_y + cactus.get_height() :   #Si le coin en haut à gauche de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées du cactus
                        cactus_x = fenetre_largeur + 1
                        cactus_y = 270
                        aleatoire_cactus = 3
                        score += 10
                        game_over = False

                if cactus_x < perso_x + perso.get_width() < cactus_x + cactus.get_width() :     #Si le coin en haut à droite de l'image du personnage rentre dans les coordonnées de l'axe des abscisses du cactus
                    if cactus_y < perso_y <= cactus_y + cactus.get_height() :                   #Si le coin en haut à droite de l'image du personnage rentre dans les coordonnées de l'axe des ordonnées du cactus
                        cactus_x = fenetre_largeur + 1
                        cactus_y = 270
                        aleatoire_cactus = 3
                        score += 10
                        game_over = False

            fichier_meilleur_score = open('Fichier/high_score.txt', 'r')        #On ouvre le fichier nommé "high_score.txt"
            high_score = fichier_meilleur_score.read()                          #La variable high_score prend la valeur présente dans le fichier
            fichier_meilleur_score.close()                                      #On ferme le fichier obligatoirement après utilisation car sinon le fichier n'est pas enregistré

            if int(high_score) <= score :                   #A chaque fois que le score dépasse le meilleur score, le meilleur score est égal au score. De ce fait, il ne peut y avoir un score meilleur que le meilleur score affiché
                high_score = score

            #Augmentation de la difficulté. Plus le score est élevé, plus le jeu est difficile
            if 200 <= score < 400 :                 # Si le score est entre 200 et 400 points :
                temps_apparition_cactus = 4500      #Les temps d'apparition des obstacle diminuent de 500 millisecondes
                temps_apparition_oiseau = 7000
                vitesse_fond = 11                   #La vitesse du fond d'écran accélère, elle augmente de 1 pixel par rafraichissment. La vitesse des obstacles est liée à la vitesse du fond d'écran, ainsi, la vitesse des obstacles augmentent proportionnellement.

            if 400 <= score < 600 :                 #Si le score est compris entre 400 points et 600 points :
                temps_apparition_cactus = 4000      #Les temps d'apparition des obstacles diminuent de 500 millisecondes
                temps_apparition_oiseau = 6500
                vitesse_fond = 11.5                 #La vitesse du fond d'écran et des obstracles augmente de 0.5 pixels par rafraichissement

            if 600 <= score < 800 :                 #Si le score est compris entre 600 et 800 points :
                temps_apparition_cactus = 3500      #Les temps d'apparition des obstacles diminuent de 500 millisecondes
                temps_apparition_oiseau = 6000
                vitesse_fond = 12                   #Les vitesses augmentent de 0.5 pixels par rafraichissement

            if 800 <= score < 1000 :                #Si le score est compris entre 800 et 1000 points :
                temps_apparition_cactus = 3000      #Les temps d'apparition des obstacles diminuent de 500 millisecondes
                temps_apparition_oiseau = 5500
                vitesse_fond = 12.5                 #Les vitesses augmentent de 0.5 pixels par rafraichissement

            if 1000 < score :                       #Si le score est supérieur à 1000 :
                temps_apparition_cactus = 2000      #Les temps d'apparition des obstacles diminuent de 1000 millisecondes
                temps_apparition_oiseau = 4500
                vitesse_fond = 13.5                 #Les vitesses augmentent de 1 pixels par rafraichissement


            #Rafraichissement des images et des textes pour pouvoir les voir à l'écran
            fenetre.blit(fond1, (fond1_x,0))                #Affichage du 1er fond d'écran
            fenetre.blit(fond2, (fond2_x,0))                #Affichage du 2ème fond d'écran
            fenetre.blit(perso, (perso_x,perso_y))          #Affichage du personnage
            fenetre.blit(pouvoir, (pouvoir_x,pouvoir_y))    #Affichage de l'étoile
            fenetre.blit(cactus, (cactus_x,cactus_y))       #Affichage du cactus qui sert d'obstacle
            fenetre.blit(piaf, (oiseau_x,oiseau_y))         #Affichage de l'oiseau qui sert d'obstacle
            fenetre.blit(pygame.font.SysFont("Police/FSEX300.ttf", 45).render("Points : " + str(int(score)), True,BLANC), (10,fenetre_hauteur - 55))      #Affichage du score
            fenetre.blit(pygame.font.SysFont(None, 45).render("Meilleur score : " + str(int(high_score)), False, BLANC), (fenetre_largeur - 320,fenetre_hauteur - 55))      #Affichage du meilleur score
            fenetre.blit(pygame.font.SysFont(None, 35).render("Echap = Retour à la Sélection des perso", True, BLANC), (0,0))       #Affichage du texte : "Retour à la sélection des perso"
            if vie == 1 or vie == 2 or vie == 3 :           #Si le personnage a au moins 1 vie, le premier coeur en haut à gauche est affiché
                fenetre.blit(coeur1, (0,35))
            if vie == 2 or vie == 3 :                       #Si le personnage a 2 ou 3 vies au moins 2 vies, le deuxième coeur en haut à gauche est affiché
                fenetre.blit(coeur2, (coeur1.get_width(),35))
            if vie == 3 :                                   #Si le personnage a 3 vies, le troisième coeur en haut à gauche est affiché
                fenetre.blit(coeur3, ((coeur1.get_width()+coeur2.get_width()),35))
            if invulnerabilite == 1 :                       #Si le personnage vient de perdre une vie, il est invulnérable, alors le texte "Invulnérable" est affiché
                fenetre.blit(pygame.font.SysFont(None, 70).render("Invulnérable !!", True, BLANC), (360,150))

            if bonus == True :                              #Si le perso à attraper le bonus, une bulle rose apparait pour indiquer à l'utilisateur qu'il a le bonus
                if 0 < temps_bonus < 400 or 410 < temps_bonus < 420 or 430 < temps_bonus < 440 or 450 < temps_bonus < 460 or 470 < temps_bonus < 480 or 490 < temps_bonus <= 500 :  #La bulle rose est affichée que dans différents intervalles, ce qui donne une impression de clignotement
                    bouclier.convert_alpha()
                    fenetre.blit(bouclier, (perso_x, perso_y))         #L'image en question est superposée au personnage
            fenetre.blit(licence, ((fenetre_largeur - licence.get_width()),0))      #Affichage de la licence ISN
            pygame.display.flip()       #Rafraichissement de toute la boucle


    while ecran_de_fin == True :      #L'utilisateur a perdu, la page "Game Over" s'affiche

        #Affichage du meilleur score sur l'écran de fin
        high_score = str(int(high_score))           #Il faut convertir la variable high_score en chaîne de carctères, car on ne peut écrire qu'une chaîne de caractère dans un fichier
        fichier_meilleur_score = open("Fichier/high_score.txt", "r")    #Ouverture du fichier pour le lire
        contenu = fichier_meilleur_score.read()                         #création de la variable contenu qui est la valeur indiquée dans le fichier
        fichier_meilleur_score.close()                                  #Fermeture du fichier


        if int(high_score) > int(contenu) :                                 #Conversion en valeur entière les variables high_score et contenu pour pouvoir comparer leur valeur car leur valeur sont des chiffres
                                                                            #Si la variable high_score est inférieure à la valeur du fichier,
            fichier_meilleur_score = open('Fichier/high_score.txt', "w")    #Ouverture du fichier meilleur score pour pouvoir le modifier
            fichier_meilleur_score.write(high_score)                        #La valeur du fichier est écrasée et est remplacée par la valeur de la variable high_score
            fichier_meilleur_score.close()                                  #fermeture du fichier

        fichier_meilleur_score = open('Fichier/high_score.txt', 'r')        #Ouverture du fichier meilleur score pour pouvoir le lire
        high_score = fichier_meilleur_score.read()                          #La valeur de la variable high_score est la valeur dans le fichier
        fichier_meilleur_score.close()                                      #Fermeture du fichier


        for event in pygame.event.get() :
            if event.type == QUIT :                     #Si l'utilisateur quitte le jeu, toutes les boucles sont fermées et la fenêtre de jeu se ferme
                jeu = False
                game_over = True
                selection_perso = False
                ecran_de_fin = False


            if event.type == KEYDOWN :
                if event.key == K_SPACE :               #Si il y a une pression sur la barre espace, le jeu est relancé
                    selection_perso = False
                    jeu = True
                    game_over = False
                    ecran_de_fin = False
                    bonus = False
                    collisions = True

                    #Remise à zéro de toutes les variables
                    score = 0
                    perso_x = 0
                    perso_y = 243
                    cactus_x = fenetre_largeur + 1
                    oiseau_x = fenetre_largeur + 1
                    pouvoir_x = fenetre_largeur + 1
                    fond1_x = 0
                    fond2_x = fond1.get_width()
                    perso_x = 0
                    vie = 3
                    invulnerabilite = 0

                    aleatoire_cactus = randint(1,3)
                    aleatoire_oiseau = randint(1,3)
                    aleatoire_pouvoir = randint(1,3)



                if event.key == K_RETURN :              #Si l'utilisateur appuie sur la touche entrée :
                    selection_perso = True              #Il y a un retour à la sélection des personnages
                    jeu = True
                    game_over = True
                    ecran_de_fin = False
                    musique = "Sons/son_perso.ogg"      #Lancement de la musique de la page de la sélection des personnage
                    pygame.mixer.music.load(musique)    #Chargement de la musique
                    pygame.mixer.music.play(-1, 0.0)    #Lancement de la musique sans délai sans arrêt

                if event.key == K_ESCAPE :              #Si l'utilisateur appuie sur échap, les boucles se ferment et la fenêtre se ferme
                    jeu = False
                    game_over = True
                    selection_perso = False
                    ecran_de_fin = False


        temps_clignotement += 0.05          #Lancement de la variable temps liée au clignotemement des textes
        pygame.time.delay(10)               #Limite le rafraichissement des images à 10 millisecondes


        fenetre.blit(ecran_score, (0,0))            #Affichage de l'écran de fin
        fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ton Score : ' + str(int(score)), True, NOIR), (270,0))              #Affichage du score
        fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ton Meilleur Score : ' + str(high_score), True, NOIR), (200,65))    #Affichage du meilleur score
        if int(temps_clignotement)%2 == 0 :         #Si le reste de la division de la variable temps est égal à zéro :
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 80).render('GAME OVER', True, NOIR), (290,150))     #Il y a un affichage du texte "Game Over"
            fenetre.blit(mascotte, (15,140))                                                                        #Il y a affichage de la première mascotte
            fenetre.blit(mascotte2, (fenetre_largeur - mascotte2.get_width() - 15,140))                             #Il y a affichage de la deuxième mascotte
        #En fonction du score, il y a un message différent à la fin
        if 0 <= score <= 100 :                      #Si le score final est compris entre 0 et 100 :
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Tu es nul !!', True, NOIR), (290,250))                      #Affichage du message
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ton Rang : F', True, NOIR), (290,350))                      #Affichage du rang
        if 100 < score <= 200 :                     #Si le score est compris entre 100 et 200 :
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Tu es nul !!', True, NOIR), (290,250))                      #Affichage du message
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ton Rang : E', True, NOIR), (290,350))                      #Affichage du rang
        if 200 < score <= 300 :                     #Si le score est compris entre 200 et 300 :
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Tu progresses !!', True, NOIR), (290,250))                  #Affichage du message
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ton Rang : D', True, NOIR), (290,350))                      #Affichage du rang
        if 300 < score <= 400 :                     #Si le score est compris entre 300 et 400 :
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Tu progresses !!', True, NOIR), (290,250))                  #Affichage du message
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ton Rang : C', True, NOIR), (290,350))                      #Affichage du rang
        if 400 < score <= 500 :                     #Si le score est compris entre 400 et 500 :
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Peux mieux faire !!', True, NOIR), (290,250))               #Affichage du message
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ton Rang : B', True, NOIR), (290,350))                      #Affichage du rang
        if 500 < score <= 1000 :                    #Si le score est compris entre 500 et 1000 :
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Peux mieux faire !!', True, NOIR), (290,250))               #Affichage du message
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ton Rang : A', True, NOIR), (290,350))                      #Affichage du rang
        if 1000 < score :                           #Si le score est supérieur à 1000 :
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ce jeu est trop simple pour toi !!', True, NOIR), (20,250)) #Affichage du message
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 55).render('Ton Rang : S', True, NOIR), (290,350))                      #Affcihage du rang


        fenetre.blit(licence, (fenetre_largeur - licence.get_width(),0))            #Affichage de la licence ISN
        pygame.display.flip()           #Rafraichissement totale

    while selection_perso == True:


        #Remise à zéro de toutes les variables
        jeu = True
        game_over = False
        ecran_de_fin = False
        bonus = False
        collisions = True

        perso_x = 0
        perso_y = 243
        cactus_x = fenetre_largeur + 1
        oiseau_x = fenetre_largeur + 1
        pouvoir_x = fenetre_largeur + 1
        fond1_x = 0
        fond2_x = fond1.get_width()
        perso_x = 0
        score = 0
        vie = 3
        invulnerabilite = 0

        aleatoire_cactus = randint(1,3)
        aleatoire_oiseau = randint(1,3)
        aleatoire_pouvoir = randint(1,3)




        perso = pygame.image.load('image/transparence.png')         #Chargement d'une image transparente qui ne doit pas être vu par l'utilisateur(image quelconque)

        temps_clignotement += 0.05                                  #Prolongement de la variable temps de clignotement
        pygame.time.delay(10)

        for event in pygame.event.get() :
            if event.type == QUIT :                                 #Si l'utilisateur ferme la fenetre, tout le programme se ferme
                jeu = False
                game_over = True
                selection_perso = False
                ecran_de_fin = False
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :                          #Si l'utilisateur appuie sur la touche échap, tout le programme et la fenêtre se ferment
                    jeu = False
                    game_over = True
                    selection_perso = False
                    ecran_de_fin = False

            if event.type == MOUSEBUTTONDOWN :                      #Evènement suite à un clique de la souris
                souris = pygame.mouse.get_pos()                     #Coordonnées de la souris
                souris_x = souris[0]                                #Valeur des abscisses de la souris
                souris_y = souris[1]                                #Valeur des ordonnées de la souris

                if MCB_x < souris_x < MCB_x + MmeCornetBerry.get_width() and MCB_y < souris_y < MCB_y + MmeCornetBerry.get_height() :           #Si l'utilisateur clique sur l'image de Mme Cornet-Berry
                    selection_perso = False             #Il y a ouverture de la boucle game_over et fermeture de la boucle de la séléction des personnages
                    game_over = False
                    jeu = True
                    ecran_de_fin = False
                    perso = pygame.image.load('image/MmeCornetBerry.png').convert_alpha()           #Le personnage est l'image de Mme Cornet-Berry

                if MrSchneider_x < souris_x < MrSchneider_x + MrSchneider.get_width() and MrSchneider_y < souris_y < MrSchneider_y + MrSchneider.get_height() :     #Si l'utilisateur clique sur l'image de Mr Schneider
                    selection_perso = False
                    game_over = False
                    jeu = True
                    ecran_de_fin = False
                    perso = pygame.image.load('image/MrSchneider.png').convert_alpha()              #Le personnage est l'image de Mr Schneider

                if Andy_x < souris_x < Andy_x + Andy.get_width() and Andy_y < souris_y < Andy_y + Andy.get_height() :       #Si l'utilisateur clique sur l'image d'Andy
                    selection_perso = False
                    game_over = False
                    jeu = True
                    ecran_de_fin = False
                    perso = pygame.image.load('image/Andy.png').convert_alpha()                     #Le personnage est l'image d'Andy

                if Julien_x < souris_x < Julien_x + Julien.get_width() and Julien_y < souris_y < Julien_y + Julien.get_height() :           #Si l'utilisateur clique sur l'image de Julien
                    selection_perso = False
                    game_over = False
                    jeu = True
                    ecran_de_fin = False
                    perso = pygame.image.load('image/JuJu.png').convert_alpha()                     #Le personnage est l'image de Julien


        fenetre.blit(fond_perso, (0,0))                                 #Affichage de l'image de fond
        fenetre.blit(MmeCornetBerry, (MCB_x,MCB_y))                     #Affichage de l'image de Mme Cornet-Berry
        fenetre.blit(MrSchneider, (MrSchneider_x,MrSchneider_y))        #Affichage de l'image de Mr Scnheider
        fenetre.blit(Andy, (Andy_x,Andy_y))                             #Affichage de l'image d'Andy
        fenetre.blit(Julien, (Julien_x,Julien_y))
        fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 30).render('WonderBerry', True, NOIR), ((MCB_x - 50),(MCB_y + MmeCornetBerry.get_height() + 10)))                   #Affichage du texte de Mme Cornet-Berry
        fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 30).render('SuperSchneider', True, NOIR), ((MrSchneider_x - 50),(MrSchneider_y + MrSchneider.get_height() + 10)))   #Affichage du texte de Mr Schneider
        fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 30).render('Captain Valla', True, NOIR),((Andy_x - 50),(Andy_y + Andy.get_height() + 10)))                          #Affichage du texte d'Andy
        fenetre.blit(pygame.font.Font('Police/FSEX300.ttf', 30).render('Julien-Man', True, NOIR), ((Julien_x - 50), (Julien_y + Julien.get_height() + 10)))                     #Affichage du texte de Julien
        fenetre.blit(mascotte, ((fenetre_largeur/2),115))                           #Affichage de la 1ère mascotte
        fenetre.blit(mascotte2, ((fenetre_largeur/2 - mascotte2.get_width()),115))  #Affichage de la seconde mascotte
        fenetre.blit(licence, ((fenetre_largeur - licence.get_width()),0))          #Affichage de la licence ISN
        if int(temps_clignotement)%2 == 0 :                 #Si le reste du temps divisé par 2 est égal à zéro :
            fenetre.blit(pygame.font.Font('Police/FSEX300.ttf',55).render("SELECTIONNE UN PERSONNAGE :", False, NOIR), (150,250)) #Il y a affichage du texte, ce qui crée un clignotement
        pygame.display.flip()       #Rafraichissement de tout


pygame.quit()
quit()              #Fermeture du programme