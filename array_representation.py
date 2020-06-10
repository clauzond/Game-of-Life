import numpy as np
from random import random

class GameOfLife():

    def __init__(self,height=None,width=None,initial_array=None):
        """
        Implémentation par un np.array
            -> "height" lignes et "width" colonnes
            -> array[i][j] = i-ème ligne / j-ème colonne
        Une case vivante correspond à 1, une case morte à 0
        """

        if initial_array is None:
            if (height is None) or (width is None):
                raise Exception("Spécifier la forme (height,width)")
            self.gameArray = np.full((height,width),0)
            self.shape = (height,width)
        else:
            self.gameArray = initial_array
            self.shape = initial_array.shape

        self.totalSteps = 0

        return

    def __repr__(self):
        _string = f"Game Array:\n{self.gameArray}\n"
        _string += f"Number of steps : {self.totalSteps}\n"
        return(_string)


    def nextStep(self):
        """
        Applique la règle du jeu à toutes les cases de self.gameArray

        return: liste des cases qui ont changés
        """
        # _changedList permet de ne modifier que les cases qui ont changés
        _changedList = []
        for x in range(0,self.shape[0]):
            for y in range(0,self.shape[1]):
                _bool = self._applyRules(x,y)

                if _bool:
                    _changedList.append((x,y))

        # On change l'état de chaque case
        # n.b : pour un état qui a changé, le nouvel état est "1 - ancien_etat"
        for (x,y) in _changedList:
            self.gameArray[x][y] = 1 - self.gameArray[x][y]

        self.totalSteps += 1

        return(_changedList)


    def randomize(self,chance=0.05,reset=False):
        """
        Randomize le self.gameArray actuel
        Chaque case a "chance" de venir au monde, "1-chance" d'être morte

        return: liste des cases qui ont changés
        """
        _changedList = []
        for x in range(0,self.shape[0]):
            for y in range(0,self.shape[1]):
                old = self.gameArray[x][y]
                r = random()
                if r <= chance:
                    self.gameArray[x][y] = 1
                    if old == 0:
                        _changedList.append((x,y))
                else:
                    self.gameArray[x][y] = 0
                    if old == 1:
                        _changedList.append((x,y))

        if reset:
            self.totalSteps = 0

        return(_changedList)


    def _ruleOne(self,x,y):
        """
        Règle n°1 :
        pour une case vivante, si  2 <= voisins <= 3 elle vit, sinon elle meurt

        return: True s'il y a eu du changement ; False sinon
        """
        # Vérification case vivante
        if self.gameArray[x][y] == 0:
            return(False)

        numberOfNeighbours = len(self._getAliveNeighbours(x,y))
        if not (2<=numberOfNeighbours<=3):
            return(True)
        else:
            return(False)

    def _ruleTwo(self,x,y):
        """
        Règle n°2 :
        pour une case morte, si voisins == 3 elle vient à la vie; sinon non.

        return: True s'il y a eu du changement ; False sinon
        """
        # Vérification case morte
        if self.gameArray[x][y] == 1:
            return(False)

        numberOfNeighbours = len(self._getAliveNeighbours(x,y))
        if numberOfNeighbours == 3:
            return(True)
        else:
            return(False)

    def _applyRules(self,x,y):
        """
        Applique la règle n°1 ou n°2 selon l'état actuel de la case
        """
        if self.gameArray[x][y] == 1:
            return(self._ruleOne(x,y))
        else:
            return(self._ruleTwo(x,y))


    def _getNeighbours(self,x,y):
        """
        Renvoie toutes les cases voisines d'une case donnée (sauf elle-même)
        (x,y) doit désigner une case existante de self.gameArray

        return: liste des cases (doublon x,y) voisines possibles
        """
        _list = []

        # pour (x-1)
        if (x-1) >= 0:
            if (y-1) >= 0:
                _list.append((x-1,y-1))
            _list.append((x-1,y))
            if (y+1) <= (self.shape[1] - 1):
                _list.append((x-1,y+1))
        # pour x
        if True:
            if (y-1) >= 0:
                _list.append((x,y-1))
            if (y+1) <= (self.shape[1] - 1):
                _list.append((x,y+1))
        # pour (x+1)
        if (x+1) <= (self.shape[0] - 1):
            if (y-1) >= 0:
                _list.append((x+1,y-1))
            _list.append((x+1,y))
            if (y+1) <= (self.shape[1] - 1):
                _list.append((x+1,y+1))

        return(_list)

    def _getAliveNeighbours(self,x,y):
        _list = self._getNeighbours(x,y)
        _temp = []
        for (x,y) in _list:
            if self.gameArray[x][y] == 1:
                _temp.append((x,y))
        return(_temp)

    def _getAlive(self):
        _list = []
        for x in range(0,self.shape[0]):
            for y in range(0,self.shape[1]):
                if self.gameArray[x][y] == 1:
                    _list.append((x,y))
        return(_list)


if __name__ == "__main__":
    global game

    game = GameOfLife(height=10,width=10)
    game.randomize(chance=0.1, reset=True)
