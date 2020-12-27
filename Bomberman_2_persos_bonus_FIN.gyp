#import os
#os.chdir("C:\\Users\\goran\\Documents\\Sacha travail CPES\\Python Scripts\\")
import pygame, time, sys, random
pygame.init()
horloge = pygame.time.Clock()

ecran=pygame.display.set_mode((1088,832))
dirt = pygame.image.load("/Users/oscar/Desktop/Bomberman/terrain:dirt.png").convert_alpha()
box = pygame.image.load("/Users/oscar/Desktop/Bomberman/terrain:box.png").convert_alpha()
bloc = pygame.image.load("/Users/oscar/Desktop/Bomberman/bloc.png").convert_alpha()
logo = pygame.image.load("/Users/oscar/Desktop/Bomberman/logo.png").convert_alpha()
#redimension de la taille du logo
logo = pygame.transform.scale(logo, (640,450))
#importation du bouton play
bouton_play = pygame.image.load("/Users/oscar/Desktop/Bomberman/play.png").convert_alpha()
bouton_play = pygame.transform.scale(bouton_play, (146,57))
bouton_play_rectangle = bouton_play.get_rect()
bouton_play_rectangle.x = 320
bouton_play_rectangle.y = 350
imagebombe = pygame.image.load("/Users/oscar/Desktop/Bomberman/bombes.png").convert_alpha()
imagebombe = pygame.transform.scale(imagebombe, (64,64))
#images des bonus:
Imbonusbombe = pygame.image.load("/Users/oscar/Desktop/Bomberman/bonus_bombe.png").convert_alpha()
Imbonusvitesse = pygame.image.load("/Users/oscar/Desktop/Bomberman/bonus_vitesse.png").convert_alpha()
Imbonustranspercer = pygame.image.load("/Users/oscar/Desktop/Bomberman/bonus_transpercer.png").convert_alpha()
Imbonusportée = pygame.image.load("/Users/oscar/Desktop/Bomberman/bonus_portée.png").convert_alpha()
Imbonusdétonation = pygame.image.load("/Users/oscar/Desktop/Bomberman/bonus_détonation.png").convert_alpha()
Imbonusvie = pygame.image.load("/Users/oscar/Desktop/Bomberman/bonus_vie.png").convert_alpha()

#création d'une classe qui correspond au jeu
class Game:

    def __init__(self):
        #savoir si le jeu a commencé
        self.is_playing = False
        #chargement du personnage
        perso0 = Perso(64, 11*64, pygame.image.load("/Users/oscar/Desktop/Bomberman/pinguin.png").convert_alpha())
        perso1 = Perso(15*64, 64, pygame.image.load("/Users/oscar/Desktop/Bomberman/fox.png").convert_alpha())
        if numcarte == 2:
            perso0.rectangle.x = 64*7
            perso0.rectangle.y = 64*6
            perso1.rectangle.x = 64*9
            perso1.rectangle.y = 64*6
        self.persos = [perso0, perso1]

    def collision0(self):
            possible = True
            for objet in solides :
                if game.persos[0].rectangle.colliderect(objet) == True :
                    possible = False
            return possible

    def collision1(self):
            possible = True
            for objet in solides :
                if game.persos[1].rectangle.colliderect(objet) == True :
                    possible = False
            return possible

    def collisionbonus(self):
        for objet in listebonus:
            for perso in self.persos:
                if perso.rectangle.colliderect(objet.bonusrect) == True :
                    perso.getbonus(objet.type)
                    objet.deletebonus()

    def demarrer(self):

        #déplacements du perso 1
        touches = pygame.key.get_pressed()
        if touches[pygame.K_d] == 1 :
            game.persos[0].deplacement_droite()
            #gestion des collisions
            if game.collision0() == False:
                game.persos[0].deplacement_gauche()
        if touches[pygame.K_q] == 1 :
            game.persos[0].deplacement_gauche()
            #gestion des collisions
            if game.collision0() == False:
                game.persos[0].deplacement_droite()
        if touches[pygame.K_z] == 1 :
            game.persos[0].deplacement_haut()
            #gestion des collisions
            if game.collision0() == False:
                game.persos[0].deplacement_bas()
        if touches[pygame.K_s] == 1 :
            game.persos[0].deplacement_bas()
            #gestion des collisions
            if game.collision0() == False:
                game.persos[0].deplacement_haut()
        #poser une bombe
        if touches[pygame.K_b] == 1 :
            game.persos[0].poser_bombe()

        #déplacements du perso 2
        touches = pygame.key.get_pressed()
        if touches[pygame.K_RIGHT] == 1 :
            game.persos[1].deplacement_droite()
            #gestion des collisions
            if game.collision1() == False:
                game.persos[1].deplacement_gauche()
        if touches[pygame.K_LEFT] == 1 :
            game.persos[1].deplacement_gauche()
            #gestion des collisions
            if game.collision1() == False:
                game.persos[1].deplacement_droite()
        if touches[pygame.K_UP] == 1 :
            game.persos[1].deplacement_haut()
            #gestion des collisions
            if game.collision1() == False:
                game.persos[1].deplacement_bas()
        if touches[pygame.K_DOWN] == 1 :
            game.persos[1].deplacement_bas()
            #gestion des collisions
            if game.collision1() == False:
                game.persos[1].deplacement_haut()
        #poser une bombe
        if touches[pygame.K_m] == 1 :
            game.persos[1].poser_bombe()
        if touches[pygame.K_k] == 1 and game.persos[0].détonation == True:
            game.persos[0].faitpetertouteslesbombes()
        if touches[pygame.K_k] == 1 and game.persos[1].détonation == True:
            game.persos[1].faitpetertouteslesbombes()

        #mise à jour des bombes solides en fonction de la position des persos
        i=0
        while i < (len(bombepassolide)):
            if game.persos[0].rectangle.colliderect(bombepassolide[i]) == False and game.persos[1].rectangle.colliderect(bombepassolide[i]) == False:
                solides.append(bombepassolide[i])
                del bombepassolide[i]
            else:
                i+=1

        #vérification des comptes à rebours
        j = True
        while j == True and listebombe != []:
            if listebombe[0].compte_rebours() < 0:
                #trigger l'explosion
                listebombe[0].exploser()
            else:
                #si la première bombe n'explose pas, on sort de la boucle comme elles sont classés par ordre d'apparition
                j = False

        #récolte des bonus:
        self.collisionbonus()

        #affichage de l'image des personnages, le deuxième argument spécifie les coordonnées par rapport à l'écran (ici l'image se positionne par rapport à rectangle)
        ecran.blit(game.persos[0].image, game.persos[0].rectangle)
        ecran.blit(game.persos[1].image, game.persos[1].rectangle)

#création des classes de personnage
class Perso(pygame.sprite.Sprite):

    def __init__(self, x, y, image, n=1, s=1, p=1, r=3, h=1, t=False, d=False, v=1):
        super().__init__()
        #intitiation super classe Sprite
        #super().__init__()
        self.health = h
        self.nbbombemax = n
        self.nbbombeleft = s
        self.portée = p
        self.rebours = r
        self.transpercer = t
        self.détonation = d
        self.vitesse = v
        self.image = image
        #chargement de l'image associée au personnage
        self.rectangle = self.image.get_rect()
        #coordonnées du personnage sur l'écran
        self.rectangle.x = x
        self.rectangle.y = y

    #coordonnées du perso sur la carte
    def positioncarte_x(self):
        return self.rectangle.x // 64

    def positioncarte_y(self):
        return self.rectangle.y // 64

    #création des méthodes de déplacement
    def deplacement_droite(self):
        self.rectangle.x += self.vitesse
    def deplacement_gauche(self):
            self.rectangle.x -= self.vitesse
    def deplacement_haut(self):
        self.rectangle.y -= self.vitesse
    def deplacement_bas(self):
        self.rectangle.y += self.vitesse

    #méthode pour poser les bombes
    def poser_bombe(self):
        xbombe = self.positioncarte_x()
        ybombe = self.positioncarte_y()
        if self.possibombe(xbombe, ybombe) == True:
            self.nbbombeleft -= 1
            #mettre la bombe sur la carte
            cartebombe[ybombe][xbombe]=1
            #création de l'objet de classe bombe
            bomb = bombe(self.portée, self.rebours, self.transpercer, xbombe, ybombe, self)
            #pour la gestion des collisions avec les bombes
            bombepassolide.append(bomb.bomberect)
            #màj liste des bombes
            listebombe.append(bomb)

    #savoir si on peut poser des bombes
    def possibombe(self, x, y):
        possibombe = True
        #bombes restantes
        if self.nbbombeleft == 0:
            possibombe = False
        #savoir si il y a pas déjà une bombe sur la position
        if cartebombe[y][x] == 1:
            possibombe = False
        return possibombe

    #si le perso prend un bonus:
    def getbonus(self, type):
        if type == "bombe":
            self.nbbombeleft += 1
            self.nbbombemax += 1
        if type == "portée":
            self.portée += 1
        #if type == "vitesse":
           # self.vitesse += 1
        if type == "transpercer":
            self.transpercer = True
        if type == "détonation":
            self.détonation = True

    def faitpetertouteslesbombes(self):
        for bombes in listebombe:
            if bombes.perso == self:
                bombes.exploser()

class bombe:
        def __init__(self, p, r, t, x, y, perso):
            self.portée = p
            self.rebours = r
            self.transpercer = t
            self.x = x
            self.y = y
            self.bomberect = pygame.Rect(self.x*64, self.y*64, 64, 64)
            self.settingtime = time.time()
            self.perso = perso

        def compte_rebours(self):
            return self.rebours - (time.time() - self.settingtime)

        def exploser(self):
            #suppression de la liste des (non)solides
            if self.bomberect in solides:
                solides.remove(self.bomberect)
            else:
                bombepassolide.remove(self.bomberect)
            #supression sur la carte
            cartebombe[self.y][self.x] = 0
            #suppression de la liste des bombes
            listebombe.remove(self)
            #gestion de l'explosion
            self.explosion()
            #augmentation du nombre de bombe restant du personnage
            self.perso.nbbombeleft += 1

        #gère les dégâts de l'explosion
        def explosion(self):
            #gère chaque direction de l'explosion
            self.explosion_haut(self.portée, self.transpercer, self.x, self.y)
            self.explosion_droite(self.portée, self.transpercer, self.x, self.y)
            self.explosion_bas(self.portée, self.transpercer, self.x, self.y)
            self.explosion_gauche(self.portée, self.transpercer, self.x, self.y)

        def explosion_haut(self, portée, trans, x, y):
            i = 1
            while i <= portée:
                #terrain indestructible
                if carte[y-i][x] == 3:
                    #permet de sortir de la boucle:
                    i += portée
                #terrain destructible (mais qui stoppe l'explosion sauf si bonus transpercer)
                elif carte[y-i][x] == 2:
                    carte[y-i][x] = 1
                    solides.remove(pygame.Rect(x*64, (y-i)*64, 64, 64))
                    #bonus potentiel:
                    popbonus(x, y-i)
                    if trans == False:
                        i += portée
                    else:
                        i += 1
                elif carte[y-i][x] == 1:
                    for perso in game.persos :
                        if perso.rectangle.colliderect(pygame.Rect(x*64, (y-i)*64, 64, 64)) == True :
                            perso.health -= 1
                    #déclenche l'explosion d'une autre bombe
                    if cartebombe[y-i][x] == 1:
                        #recherche de la bombe correspondante dans la liste des bombes
                        j=0
                        findbomb = False
                        while findbomb == False:
                            if listebombe[j].x == x and listebombe[j].y == y-i:
                                listebombe[j].exploser()
                                findbomb = True
                            else:
                                j += 1
                    i += 1

        def explosion_droite(self, portée, trans, x, y):
            i = 1
            while i <= portée:
                #terrain indestructible
                if carte[y][x+i] == 3:
                    #permet de sortir de la boucle:
                    i += portée
                #terrain destructible (mais qui stoppe l'explosion sauf si bonus transpercer)
                elif carte[y][x+i] == 2:
                    carte[y][x+i] = 1
                    solides.remove(pygame.Rect((x+i)*64, y*64, 64, 64))
                    #bonus potentiel:
                    popbonus(x+i, y)
                    if trans == False:
                        i += portée
                    else:
                        i += 1
                elif carte[y][x+i] == 1:
                    for perso in game.persos :
                        if perso.rectangle.colliderect(pygame.Rect((x+i)*64, (y)*64, 64, 64)) == True :
                            perso.health -= 1
                    #déclenche l'explosion d'une autre bombe
                    if cartebombe[y][x+i] == 1:
                        #recherche de la bombe correspondante dans la liste des bombes
                        j=0
                        findbomb = False
                        while findbomb == False:
                            if listebombe[j].x == x+i and listebombe[j].y == y:
                                listebombe[j].exploser()
                                findbomb = True
                            else:
                                j += 1
                    i += 1

        def explosion_gauche(self, portée, trans, x, y):
            i = 1
            while i <= portée:
                #terrain indestructible
                if carte[y][x-i] == 3:
                    #permet de sortir de la boucle:
                    i += portée
                #terrain destructible (mais qui stoppe l'explosion sauf si bonus transpercer)
                elif carte[y][x-i] == 2:
                    carte[y][x-i] = 1
                    solides.remove(pygame.Rect((x-i)*64, y*64, 64, 64))
                    #bonus potentiel:
                    popbonus(x-i, y)
                    if trans == False:
                        i += portée
                    else:
                        i += 1
                elif carte[y][x-i] == 1:
                    for perso in game.persos :
                        if perso.rectangle.colliderect(pygame.Rect((x-i)*64, (y)*64, 64, 64)) == True :
                           perso.health -= 1
                    #déclenche l'explosion d'une autre bombe
                    if cartebombe[y][x-i] == 1:
                        #recherche de la bombe correspondante dans la liste des bombes
                        j=0
                        findbomb = False
                        while findbomb == False:
                            if listebombe[j].x == x-i and listebombe[j].y == y:
                                listebombe[j].exploser()
                                findbomb = True
                            else:
                                j += 1
                    i += 1

        def explosion_bas(self, portée, trans, x, y):
            i = 1
            while i <= portée:
                #terrain indestructible
                if carte[y+i][x] == 3:
                    #permet de sortir de la boucle:
                    i += portée
                #terrain destructible (mais qui stoppe l'explosion sauf si bonus transpercer)
                elif carte[y+i][x] == 2:
                    carte[y+i][x] = 1
                    solides.remove(pygame.Rect(x*64, (y+i)*64, 64, 64))
                    #bonus potentiel:
                    popbonus(x, y+i)
                    if trans == False:
                        i += portée
                    else:
                        i += 1
                elif carte[y+i][x] == 1:
                    for perso in game.persos :
                        if perso.rectangle.colliderect(pygame.Rect(x*64, (y+i)*64, 64, 64)) == True :
                            perso.health -= 1
                    #déclenche l'explosion d'une autre bombe
                    if cartebombe[y+i][x] == 1:
                        #recherche de la bombe correspondante dans la liste des bombes
                        j=0
                        findbomb = False
                        while findbomb == False:
                            if listebombe[j].x == x and listebombe[j].y == y+i:
                                listebombe[j].exploser()
                                findbomb = True
                            else:
                                j += 1
                    i += 1

def popbonus(x,y):
    if cartebonus[y][x] != 0:
        listebonus.append(Bonus(x, y, cartebonus[y][x]))
        listebonussolide.append(Bonus(x, y, cartebonus[y][x]).bonusrect)
        cartebonus[y][x] = 0

#dictionnaire des bonus:
dictbonus = {0:None, 1:"bombe", 2:"vitesse", 3:"portée", 4:"transpercer", 5:"détonation", 6:"vie"}
dictimagebonus = {"bombe":Imbonusbombe, "vitesse":Imbonusvitesse, "portée":Imbonusportée, "transpercer":Imbonustranspercer, "détonation":Imbonusdétonation, "vie":Imbonusvie}

#classe des bonus
class Bonus:

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = dictbonus[type]
        self.bonusrect = pygame.Rect(self.x*64, self.y*64, 64, 64)
        self.image = dictimagebonus[self.type]

    def deletebonus(self):
        listebonus.remove(self)
        listebonussolide.remove(self.bonusrect)


listebonus = []
listebonussolide = []

#chargement du jeu
#game = Game()
#création de la map du jeu
carte1 = [[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,3],
[3,2,3,2,2,2,3,2,2,2,3,2,2,2,3,1,3],
[3,2,2,2,2,2,1,1,3,1,1,2,2,2,2,2,3],
[3,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,3],
[3,2,2,2,2,2,1,1,3,1,1,2,2,2,2,2,3],
[3,2,2,2,2,3,1,1,2,1,1,3,2,2,3,2,3],
[3,2,2,2,2,2,1,1,3,1,1,2,2,2,2,2,3],
[3,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,3],
[3,2,2,2,2,2,1,1,3,1,1,2,2,2,2,2,3],
[3,1,3,2,2,2,3,2,2,2,3,2,2,2,3,2,3],
[3,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]

carte2 = [[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,3,2,2,3,2,1,2,3,2,2,3,3,2,3],
[3,2,3,3,2,2,2,2,1,2,2,2,2,3,3,2,3],
[3,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,3],
[3,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,3],
[3,2,1,1,1,1,1,1,3,1,1,1,1,1,1,2,3],
[3,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,3],
[3,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,3],
[3,2,3,3,2,2,2,2,1,2,2,2,2,3,3,2,3],
[3,2,3,3,2,2,3,2,1,2,3,2,2,3,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]

#choix aléatoire de la carte
numcarte = random.randint(1,2)
if numcarte == 1:
    carte = carte1
else:
    carte = carte2

#création de la carte des bombes
cartebombe=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

cartebonus = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


indicebonus1 = 0
for ligne in carte:
    indicebonus2 = 0
    for j in ligne:
        if j == 2 :
            if random.randint(0,1) == 1:
                cartebonus[indicebonus1][indicebonus2] = random.randint(1,3)
        indicebonus2 += 1
    indicebonus1 += 1
#variation en fonction de la carte:
if numcarte == 1:
    cartebonus[6][8] = random.randint(5,6)
if numcarte == 2:
    listebonusforts = [0, 4, 5, 6]
    random.shuffle(listebonusforts)
    cartebonus[1][8] = listebonusforts[0]
    cartebonus[11][8] = listebonusforts[1]
    cartebonus[6][1] = listebonusforts[2]
    cartebonus[6][15] = listebonusforts[3]

#liste des solides que le personnage ne doit pas pouvoir traverser
solides = []
indice1 = 0
for ligne in carte:
    indice2 = 0
    for j in ligne:
        if j == 3 or j == 2 :
            solides += [pygame.Rect(indice2*64, indice1*64, 64, 64)]
        indice2 += 1
    indice1 += 1

#liste des bombes en attente d'être solide
bombepassolide = []

#liste des bombes
listebombe=[]

#liste des bonus
listebonus = []

#liste des rect de bonus dispos
listebonussolide = []

#chargement du jeu
game = Game()

#boucle de jeu
while True:
    #affichage de la map du jeu
    indice1 = 0
    ecran.fill(pygame.Color("#ae7640"))
    ecran.fill(pygame.Color("#bd8958"))
    for ligne in carte:
        indice2 = 0
        for j in ligne:
            if j == 1:
                terre = dirt.get_rect()
                terre.x = indice2*64
                terre.y = indice1*64
                ecran.blit(dirt, terre)
            if j == 2:
                boite = box.get_rect()
                boite.x = indice2*64
                boite.y = indice1*64
                ecran.blit(box, boite)
            if j == 3:
                bord=bloc.get_rect()
                bord.x = indice2*64
                bord.y = indice1*64
                ecran.blit(bloc, bord)
            indice2 += 1
        indice1 += 1
    #affichage bonus
    for bonus in listebonus:
        ecran.blit(bonus.image, bonus.bonusrect)

    #affichage bombes
    indicebombe1 = 0
    for ligne in cartebombe:
        indicebombe2 = 0
        for j in ligne:
            if j == 1:
                rectanglebombe = imagebombe.get_rect()
                rectanglebombe.x = indicebombe2*64
                rectanglebombe.y = indicebombe1*64
                ecran.blit(imagebombe, rectanglebombe)
            indicebombe2 += 1
        indicebombe1 += 1

        #on vérifie si le jeu a commencé ou pas
        if game.is_playing:
            #démarrer le jeu
            game.demarrer()
        else:
            #afficher le l'écran de bienvenue
            ecran.blit(logo, (65,0))
            ecran.blit(bouton_play, bouton_play_rectangle)

    pygame.display.update()

    if perso0.health == 0 :
        perso0.remove()
    if perso1.health == 0 :
        perso1.remove()
    
    for evenement in pygame.event.get():
        #si clic de souris
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            #savoir si la positiopn de la souris se trouve sur le bouton play
            if bouton_play_rectangle.collidepoint(evenement.pos):
                #lancer le jeu
                game.is_playing = True
        #fermer la fenêtre quand le joueur appuie sur la croix rouge
        if evenement.type == pygame.QUIT:
            sys.exit(0)
    #limiter le nombre de tours de boucles à 60
    horloge.tick(60)
