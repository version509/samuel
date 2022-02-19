import random
import time

def main():
    lignes = [0,1,2,3,4,5,6]
    colonnes = [0,1,2,3,4,5,6]

    #Variable qui rend le jeu infini
    jeu = 1

    #position 
    users = [0,3]

    #Position ou les obsacles s placent
    obstacles = [[5, 1], [3, 4], [6, 2], [0, 4], [2, 3], [1, 6], [4, 6]]

    #Notre vitesse declare
    VITESSE = 3

    #Score du joueur
    SCORE = 0

    #commencement la de la boucle
    while jeu <= 1:
        # Debut de la boucle for i
        for i in range(0,6,1):
            # debut de la boucle for j
            for j in range(0,6,1):
                time.sleep(VITESSE)
                obstacles = [i,j]
                print(obstacles)
                y = random.randint(0,7)
                users = [0,y]
                # condition de collision entre le joueur et l'obstacle
                if(obstacles == users):
                    print("Game Over")
                else:
                    print("Jeu en cours")
                    SCORE = SCORE + 10
                    print("Votre score est", SCORE)
                    if (SCORE % 50 == 0):
                      VITESSE = VITESSE/10
    
if __name__ == '__main__':
    main()