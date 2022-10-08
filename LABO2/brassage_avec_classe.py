from random import sample

class Card:


    def __init__(self, num, suite):
        self.num = num 
        self.suite = suite

    def __str__(self):

        #Formatte le chiffre/la lettre de la carte pour 
        #qu'elle prenne toujours 3 espaces et ajoutes la suite
        return f"{self.num:3}{self.suite}"


class Deck:

    def __init__(self):

        NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "  V", "  D", "  R"]
        SUITES = ["♦", "♣", "♥", "♠"]
        self.card_deck = []

        #Créé les 13 cartes de chaque suite en ordre
        for s in SUITES:
            for n in NUMBERS:
                self.card_deck.append(Card(n, s))

    #Permet de faire un brassage inter-coupé parfait
    def riffle_shuffle(self):
        #trouve le point milieu du paquet (Ex: 26 pour un paquet de 52 cartes)
        half_deck = len(self.card_deck)//2
        #Crée 2 sous paquets en coupant le paquet au milieu
        sub_decks = [self.card_deck[:half_deck], self.card_deck[half_deck:]]
        shuffled_deck = []

        #Inter-coupe les sous paquets
        #zip(list1, list2) = (list1[0], list2[0]), (list1[1], list2[1]), ...
        #zip s'arrête au dernier élément de la plus petite liste
        for c1, c2 in zip(sub_decks[0], sub_decks[1]):
            shuffled_deck.append(c1)
            shuffled_deck.append(c2)
        
        #Met à jours le paquet
        self.card_deck = shuffled_deck

    #Permet de faire un brassage par paquet de 4
    def overhand_shuffle(self):
        
        sub_decks = []
        shuffled_deck = []
        #Crée les nombres de 0 jusqu'au quart du paquet
        order = range(len(self.card_deck)//4)
        #Les placent dans un ordre aléatoire
        shuffled_order = sample(order, len(order))

        #Subdivise le paquet en sous-paquets de 4
        for i in range(0, len(self.card_deck), 4):
            sub_decks.append(self.card_deck[i:i+4])

        #Les placent dans l'ordre aléatoire généré plus haut
        for o in shuffled_order:
            shuffled_deck = shuffled_deck + sub_decks[o]
        
        #Mets à jour le paquet
        self.card_deck = shuffled_deck
    
    #Écrit un nouveau fichier deck.txt avec l'état du paquet de carte
    def save(self):
        f = open("deck.txt", "w", encoding="utf-8")
        #Utilise la fonction __str__(self) pour avoir le paquet en string
        f.write(str(self))
        f.close()
        
    #Formate le paquet sous un string
    def __str__(self):

        str_deck = ""
        #On utilise énumerate car on a besoin de l'index
        #pour faire un retour de ligne à chaque 13 cartes
        for i, card in enumerate(self.card_deck):
            #Utilise la méthode __str__(self) de la classe Card
            str_deck += str(card)
            if i%13 == 12:
                str_deck += " \n"
        return str_deck     
      

def menu():
    #Initialisation du paquet
    new_deck = Deck()
    exit = False
    while not exit:
        
        print("1. Afficher l'état du jeu de cartes")
        print("2. Faire un brassage inter-coupé")
        print("3. Faire un brassage par paquet aléatoire")
        print("4. Sauvegarder l'état du jeu")
        
        option = int(input("Choisir une option: "))
        
        if option == 1:
            print(new_deck)
        elif option == 2:
            new_deck.riffle_shuffle()
        elif option == 3:
            new_deck.overhand_shuffle()
        elif option == 4:
            new_deck.save()
            exit = True

menu()




        

