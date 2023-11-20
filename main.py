
#cree par Elie Kozaily
#cree en 2023
#tp3

import random
import sys

#toute les variables utiliser toute au long du jeu

niveau_vie = 20
victoire = 0
defaite = 0
victoire_consecutive = 0
numero_combat = 0
Valeurduchoix3 = 0
ValeurduchoixInitial = 0
vie_boss = random.randint(6,7)

#le menu du jeu
def menu() :
 print("Que voulez-vous faire ? \n "
                   "1- Combattre cet adversaire \n "
                   "2- Contourner cet adversaire et aller ouvrir une autre porte \n"
                   " 3- Afficher les règles du jeu \n "
                   "4- Quitter la partie: "
                     " \n ")

#regle du jeu
def regle() : print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
                  "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \n"
                  "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire."
                  "  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \n"
                  "La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n"
                  "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. ")


#boucle du jeu (avec les combats)

#combat boss apres 3 vicoires consecutives
while niveau_vie > 0 :
  score_dé = random.randint(1, 6)
  score_dé2 = random.randint(1,6)
  total_dé = score_dé + score_dé2
  if victoire_consecutive == 3:
      print("Ce niveau est un boss !!!: \n A cause du fait que vous avez eu 3 victoires consecutives ", )
      print("Vous etes maintenant face a un boss qui as plus de vie et qui est plus difficile a vaincre!Il a un nombre de vie de: \n", vie_boss)
      print("Vous avez roulez :", total_dé)
      vie_boss = random.randint(10, 11)


      if total_dé == vie_boss:

          niveau_vie = niveau_vie - vie_boss

          print("Vous avez perdu, Votre vie est maintenant de:", niveau_vie)
          defaite = defaite + 1
          print('defaite : ', defaite)
          print('victoire :', victoire)
          print("\n")
          victoire_consecutive = 0
          print('victoire_consecutive :', victoire_consecutive)
          print("\n")


      elif total_dé < vie_boss:

          niveau_vie = niveau_vie - vie_boss

          print("Vous avez perdu,Votre vie est maintenant de :", niveau_vie)
          defaite = defaite + 1
          print('defaite :', defaite)
          print('victoire :', victoire)
          print("\n")
          victoire_consecutive = 0
          print('victoire_consecutive :', victoire_consecutive)
          print("\n")

      else:

          niveau_vie = niveau_vie + vie_boss

          print("Vous avez gagner, Votre vie est maintenant de :", niveau_vie)
          victoire = victoire + 1
          print('defaite :', defaite)
          print('victoire :', victoire)
          print("\n")
          victoire_consecutive = victoire_consecutive + 1
          print('victoire_consecutive :', victoire_consecutive)
          print("\n")


  if Valeurduchoix3 == 0:
      force_adversaire = random.randint(1, 11)
      print("Le niveau du prochain monstre est : \n " , force_adversaire )
  else:
      print("Le niveau du prochain monstre est : \n ", force_adversaire)
  Valeurduchoix3 = 0
  choix = int(input(menu()))

#combat contre monstre normal

  if choix == 1 :
         print("Vous avez decider de combatre le monstre.")

         print("Vous avez roulez :", total_dé )

         if total_dé == force_adversaire :

             niveau_vie = niveau_vie - force_adversaire

             print("Vous avez perdu, Votre vie est maintenant de:",niveau_vie)
             defaite = defaite + 1
             print('defaite :', defaite)
             print('victoire :', victoire)
             print("\n")
             victoire_consecutive = 0
             print('victoire_consecutive :', victoire_consecutive)
             print("\n")




         elif total_dé < force_adversaire :

             niveau_vie = niveau_vie - force_adversaire

             print("Vous avez perdu,Votre vie est maintenant de :", niveau_vie)
             defaite = defaite + 1
             print('defaite :', defaite)
             print('victoire :', victoire)
             print("\n")
             victoire_consecutive = 0
             print('victoire_consecutive :', victoire_consecutive)
             print("\n")



         else:

             niveau_vie = niveau_vie + force_adversaire

             print("Vous avez gagner, Votre vie est maintenant de :", niveau_vie)
             victoire = victoire + 1
             print('defaite :', defaite)
             print('victoire :', victoire)
             print("\n")
             victoire_consecutive = victoire_consecutive + 1
             print('victoire_consecutive :', victoire_consecutive)
             print("\n")

#contourner adversaire

  elif choix == 2 :

      print("Vous avez decider de contourner le monstre vous prenez, donc une penaliter de une vie")
      niveau_vie = niveau_vie - 1
      print("Votre vie est maintenant de : ", niveau_vie)

#afficher les regles

  elif choix == 3:
         regle()
         Valeurduchoix3 = Valeurduchoix3 + 1

#sortir du programme

  else :
         sys.exit()


