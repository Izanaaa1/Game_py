# КРЕСТИКИ НОЛИКИ
ALL_SPACES = list("123456789")
X, O, BLANK = 'X', 'O', ' '

def main():
    """проводит игру в крестики нолики """
    print("Добро пожаловать в tic-tac-toe!")
    gameBoard = TTTBoard() # создает объект игрового поля 
    currentPlayer, nextPlayer = X, O

    while True:
        print(gameBoard.getBoardStr()) # вывести игровое поле

        move = None

        while not gameBoard.isValidSpace(move):
            print(f"Куда хотите походить {currentPlayer}? (1-9)")
            move = input()

        gameBoard.updateBoard(move, currentPlayer)

        # Проверить окончание игры
        if gameBoard.isWinner(currentPlayer):
            print(gameBoard.getBoardStr())
            print(currentPlayer + ' вы выиграли игру!')
            break
        elif gameBoard.isBoardFull():
            print(gameBoard.getBoardStr())
            print("Ничья в игре!")
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer # передать ход сопернику
    print("Спасибо за игру!")



class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """Создает пустое игровое поле для игрока"""
        self._spaces = {}
        for space in ALL_SPACES:
            self._spaces[space] = BLANK # все поля в исходном состоянии пусты.
        
    def getBoardStr(self):
        """Возвращает текстовое представление игрового поля"""
        return f'''
{self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
-+-+-
{self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
-+-+-
{self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9
'''
    def isValidSpace(self, space):
        """Возвращает True если задан допустимы номер клетки и эта клетка пуста"""
        return space in ALL_SPACES and self._spaces[space] == BLANK
    def isWinner(self, player):
        """Возвращает True, если игрок победил на заданном поле."""
        s, p = self._spaces, player # короткие имена для удобства 
        return ((s['1'] == s['2'] == s['3'] == p) or
                (s['4'] == s['5'] == s['6'] == p) or
                (s['7'] == s['8'] == s['9'] == p) or
                (s['1'] == s['4'] == s['7'] == p) or
                (s['2'] == s['5'] == s['8'] == p) or
                (s['3'] == s['6'] == s['9'] == p) or
                (s['3'] == s['5'] == s['7'] == p) or
                (s['1'] == s['5'] == s['9'] == p))
    def isBoardFull(self):
        """Возвращает True, если заняты все клетки игрового поля"""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False # Если есть хотябы одна пустая клетка, вернутт False 
        return True # пустых клеток не осталось 
    
    def updateBoard(self, space, player):
        """Заполняет клетку игрового поля знаком игрока"""
        self._spaces[space] = player


if __name__ == '__main__':
    main()
