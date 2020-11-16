""" Variables """
from random import randint



fenetre_hauteur = 639
fenetre_largeur = 959

fond1_x = 0
fond2_x = fenetre_largeur
perso_x = 0
perso_y = 243
cactus_x = fenetre_largeur + 1
cactus_y = 270
oiseau_x = fenetre_largeur + 1
oiseau_y = randint(180,206)
pouvoir_x = fenetre_largeur + 1
pouvoir_y = 200



MCB_x = 50
MCB_y = 400
MrSchneider_x = 320
MrSchneider_y = 400
Andy_x = 590
Andy_y = 400
Julien_x = 860
Julien_y = 400



saut = 0
double_saut = 0
mouvement_recul = 0
score = 0
vie = 3
invulnerabilite = 0
temps_invulnerabilite = 0
musique = "Sons/son_perso.ogg"
volume = 0.8


acceleration = 0.05
acceleration_supplementaire = 0.4
vitesse_fond = 5
vitesse_bonus_reelle = 7
vitesse_bonus = vitesse_bonus_reelle


temps_bonus = 0
temps_apparition_cactus = 5000
temps_apparition_oiseau = 7500
temps_apparition_pouvoir = 10000
temps_clignotement = 0



BLANC = [255,255,255]
NOIR = [0,0,0]


jeu = True
game_over = True
bonus = False
ecran_de_fin = False
collisions = True
selection_perso = True