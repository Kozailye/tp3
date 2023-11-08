#cree par Elie Kozaily
#cree en 2022
#tp3

import random

niveau_vie = 20
victoire = 0
defaite = 0
victoire_consecutive = 0
numero_combat = 0
force_adversaire = random.randint(1,5)


def menu() :
    print("Le niveau du monstre est :",force_adversaire)
    print("Que voulez-vous faire ? \n "
                      "1- Combattre cet adversaire \n "
                      "2- Contourner cet adversaire et aller ouvrir une autre porte \n"
                      "3- Afficher les règles du jeu \n "
                      "4- Quitter la partie "
                        " \n :")


def regle() : print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n" 
                     "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \n" 
                     "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire." 
                     "  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \n" 
                     "La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n" 
                     "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. ")


choix = int(input(menu()))


if choix == 1 :
    print("Vous avez decider de combatre le monstre.")
    score_dé = random.randint(1, 6)
    print("Vous avez roulez :", score_dé )

    if score_dé == force_adversaire :

        niveau_vie = niveau_vie - force_adversaire

        print("Vous avez perdu, Votre vie est maintenant de:",niveau_vie)

    elif score_dé < force_adversaire :

        niveau_vie = niveau_vie - force_adversaire

        print("Vous avez perdu,Votre vie est maintenant de :", niveau_vie)

    else :

        niveau_vie = niveau_vie + force_adversaire

        print("Vous avez gagner, Votre vie est maintenant de :", niveau_vie)

elif choix == 2 :
    print("Vous avez decider de contourner le monstre vous prenez, donc une penaliter de une vie")
    niveau_vie = niveau_vie - 1
    print("Votre vie est maintenant de : ", niveau_vie)

elif choix == 3:
    regle()

else :
    print("quitter")

