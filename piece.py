
class Piece:
    x = 0
    y = 0
    alive = True
    selected = True
    alignment = 0
    def __init__(self, x, y, alignment):
        self.x = x
        self.y = y
        self.alignment = alignment

class Pawn(Piece):
    firstMove = True
    def __init__(self, x, y, alignment):
        super().__init__(x, y, alignment)

    ''' Pawn Movement 
     3 | 2 | 4
       | 1 |   
       |PAW|   
       |   |   

    '''

    def move(self, option):
        if self.firstMove:
            if option == 1:
                self.y += 1 * increment(self.alignment)
            elif option == 2:
                self.y += 2 * increment(self.alignment)
            self.firstMove = False
        else:
            self.y += 1 * increment(self.alignment)

class King(Piece):
    def __init__(self, x, y, alignment):
        super().__init__(x, y, alignment)

    ''' King Movement 
     8 | 1 | 2 
     7 |KIN| 3 
     6 | 5 | 4 

    '''

    def move(self, option):
        if option == 1:
            self.y += 1 * increment(self.alignment)
        elif option == 2:
            self.y += 1 * increment(self.alignment)
            self.x += 1 * increment(self.alignment)
        elif option == 3:
            self.x += 1 * increment(self.alignment)
        elif option == 4:
            self.y -= 1 * increment(self.alignment)
            self.x += 1 * increment(self.alignment)
        elif option == 5:
            self.y -= 1 * increment(self.alignment)
        elif option == 6:
            self.y -= 1 * increment(self.alignment)
            self.x -= 1 * increment(self.alignment)
        elif option == 7:
            self.x -= 1 * increment(self.alignment)
        elif option == 2:
            self.y += 1 * increment(self.alignment)
            self.x -= 1 * increment(self.alignment)

class Knight(Piece):
    def __init__(self, x, y, alignment):
        super().__init__(x, y, alignment)

    '''Knight Movement
       | 8 |   | 1 |   |
     7 |   |   |   | 2 |
       |   |KNI|   |   |
     6 |   |   |   | 3 |
       | 5 |   | 4 |   |
   
    '''

    def move(self, option):
        if option == 1:
            self.y += 2 * increment(self.alignment)
            self.x += 1 * increment(self.alignment)
        elif option == 2:
            self.y += 1 * increment(self.alignment)
            self.x += 2 * increment(self.alignment)
        elif option == 3:
            self.y -= 1 * increment(self.alignment)
            self.x += 4 * increment(self.alignment)
        elif option == 4:
            self.y -= 2 * increment(self.alignment)
            self.x += 1 * increment(self.alignment)
    
def increment(alignment):
    if alignment == 0:
        return -1
    else:
        return 1