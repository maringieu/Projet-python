
wordliste = ['Your sister', 'Your dad',
            'You',
            'Your mum', 
            'Your face',
            'Your nose',
            'Your cat',
            'looks like',
            'is like',
            'eats',
            'loves',
            'sniff',
            'is',
            'a fish',
            'a dog',
            'the floor',
            'big',
            'a trash',
            'an empty hole',
            'idiot',
            'hairless',
            'abandoned',
            'lost',
            'rotten',
            'so stupid',
            'so hard',
            'and',
            'also',
            'too',
            'moreover'
            ]
        
class Personnage:

    def __init__(self, nom):
        self.nom = nom
        self.vie = 10
    
    def diminueVie(self, vieEnMoins = 1):
        self.vie = max(0,self.vie - vieEnMoins)

    def attaque(self, unPersonnage):
        unPersonnage.diminueVie(2)
    
Players = list()
listP1 = []
listP2 = []

choix = "x"
while choix != "Q" :
    print("Créer un nouveau personnage, tapez : 1")
    print("Faire une attaque, tapez : 2")
    print("Quitter, tapez : Q")
    choix = input("votre choix : ")

    if choix == "1" :
        nom = input("Nom = ")
        nouveau = Personnage(nom)
        Players.append(nouveau)
    elif choix == "2" :
        for i, unPersonnage in enumerate(Players):
            print(i,":",unPersonnage.nom, "( vie : ",unPersonnage.vie,")")
        
        numAttaquant = int(input("n° du joueur 1 = "))
        numVictime = int(input("n° du joueur 2 = "))
        joueur1 = Players[numAttaquant]
        joueur2 = Players[numVictime]

        choix2 = "x"
        while choix2 != "Q":
            print("choisir une insulte, tapez : 1") 
            print("arretez la partie, tapez : 2")
            print("Quitter, tapez : Q")
            choix2 = input("votre choix : ")

            if choix2 == "1":
                print("le joueur 1 choisit une insulte: ")
                print("")
                print(wordliste)
                choix3 = input()
                for k in wordliste:
                    if k== choix3 :
                        listP1.append(choix3)
                        wordliste.remove(choix3)    
                    else:
                        print(wordliste)
            elif choix2 == "2":

                print(listP1)
                print(listP2)
                break 


            choix0 = "x"
            while choix0 != "Q":
                print("choisir une insulte, tapez : 1") 
                print("arretez la partie, tapez : 2")
                print("Quitter, tapez : Q")
                choix0 = input("votre choix : ")

                if choix0 == "1":
                    print("le joueur 2 choisit une insulte: ")
                    print("")
                    print(wordliste)
                    choix4 = input()
                    for k in wordliste:
                        if k == choix4 :
                            listP2.append(choix4)
                            wordliste.remove(choix4)       
                        else:
                            print(wordliste)        
                elif choix0 == "2":

                    print(listP1)
                    print(listP2)
                    break   
                break
              
        break   
        
        

                
