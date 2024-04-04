import math

WHITE_ROOK = 1
WHITE_KNIGHT = 2
BLACK_ROOK = -1
BLACK_KNIGHT = -2
NOTHING = 0

printable = {WHITE_ROOK: '| _ i', WHITE_KNIGHT: '-|_|i', BLACK_KNIGHT: 'i|_|-', BLACK_ROOK: 'i _ |', NOTHING: '     '}

class Board:
    def __init__(self):
        self.board = [[BLACK_KNIGHT] * 8] + [[BLACK_ROOK] * 8] + [[NOTHING] * 8 for _ in range(4)] \
            + [[WHITE_ROOK] * 8] + [[WHITE_KNIGHT] * 8]
        self.current_side = 1
        #self.board = [[printable[1]] * 8] + [[printable[0]] * 8] + [[printable[2]] * 8 for _ in range(4)] + [[printable[0]] * 8] + [[printable[1]] * 8]
    
    def convert_turn(self, turn):
        self.from_letter = turn[0]
        self.from_number = turn[1]
        self.to_letter = turn[5]
        self.to_number = turn[6]
        if self.from_letter not in 'ABCDEFGH' or self.to_letter not in 'ABCDEFGH':
            raise RuntimeError('Could not convert')
        if self.from_number not in '12345678' or self.to_number not in '12345678':
            raise RuntimeError('Could not convert')
        self.from_number = int(self.from_number)
        self.to_number = int(self.to_number)
        self.from_letter = ord(self.from_letter) - 65
        self.to_letter = ord(self.to_letter) - 65
        return (self.from_number, self.from_letter, self.to_number, self.to_letter)

    def try_make_turn(self, turn):
        # является ли turn ходом клетка-клетка, есть ли на первой клетке фигура 
        # и есть ли у нее по правилам такой ход
        converted_turn = self.convert_turn(turn)
        type_cell = self.board[converted_turn[0]][converted_turn[1]]
        if type_cell == NOTHING:
            raise RuntimeError('Empty cell')
        if converted_turn[0] == converted_turn[2] and converted_turn[1] == converted_turn[3]:
            raise RuntimeError('Same cell')
        if (self.current_side and type_cell < 0) or (-current_side and type_cell > 0):
            raise RuntimeError('Wrong color')
        if self.current_side:
            self.current_side *= -1
            if type_cell == WHITE_KNIGHT:
                return self.knights_move(converted_turn)
            else:
                return self.rooks_move(converted_turn)
        else:
            self.current_side *= -1
            if type_cell == BLACK_KNIGHT:
                return self.knights_move(converted_turn)
            else:
                return self.rooks_move(converted_turn)
    

    def after_turn(self, turn):
        converted_turn = self.convert_turn(turn)
        result = self.try_make_turn(turn)
        if result:
            self.board[converted_turn[2]][converted_turn[3]] = self.board[converted_turn[0]][converted_turn[1]]
            self.board[converted_turn[0]][converted_turn[1]] = NOTHING
        else:
            print('Incorrect turn')
            #self.after_turn(new_turn)


        
        
    # проверка хода:
    # 1. это вообще клетки?
    # 2. они различные?
    # 3. на from стоит фигура?
    # 4. она твоего цвета?
    # ! 5. по дороге к to пусто?
    # 6. на to не стоит фигура либо стоит фигура другого цвета?
    # ! 7. наша фигура умеет ходить из from в to?

    def rooks_move(self, converted_turn):
        type_cell = self.board[converted_turn[0]][converted_turn[1]]
        else_type_cell = self.board[converted_turn[2]][converted_turn[3]]
        if type_cell == else_type_cell:
            return False
        if converted_turn[0] == converted_turn[2] or converted_turn[1] == converted_turn[3]:
            if converted_turn[0] == converted_turn[2]:
                i = converted_turn[1] + 1
                while i <= converted_turn[3]:
                    if (self.board[converted_turn[0]][i] != NOTHING):
                        return False
            else:
                i = converted_turn[0] + 1
                while i <= converted_turn[2]:
                    if (self.board[i][converted_turn[1]] != NOTHING):
                        return False
            return True
        return False
        
    def knights_move(self, converted_turn):
        type_cell = self.board[converted_turn[0]][converted_turn[1]]
        else_type_cell = self.board[converted_turn[2]][converted_turn[3]]
        if type_cell == else_type_cell:
            return False
        step = [abs(converted_turn[0] - converted_turn[2]), abs(converted_turn[1] - converted_turn[3])]
        step.sort()
        if step == [1, 2]:
            return True
        return False





    def __str__(self):
        result = ''
        for i in range(8):
            result += str(8 - i) + ' ' + ' '.join(
                map(
                    lambda item: printable[item], # что применить
                    self.board[i] # к какой последовательности применить
                )
            ) + '\n' + '\n'
        result += '  ' + ' '.join('  {0}  '.format(i) for i in 'ABCDEFGH')
        return result

try:
    b = Board()
    b.convert_turn('9T - T9')
except RuntimeError as e:
    print("Caught:", e)

print(b)
