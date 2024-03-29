import math

WHITE_ROOK = 1
WHITE_KNIGHT = 2
BLACK_ROOK = -1
BLACK_KNIGHT = -2
NOTHING = 0

printable = {ROOK: '| _ |', KNIGHT: 'i|_|-', NOTHING: '     '}

class Board:
    def __init__(self):
        self.board = [[BLACK_KNIGHT] * 8] + [[BLACK_ROOK] * 8] + [[NOTHING] * 8 for _ in range(4)] \
            + [[WHITE_ROOK] * 8] + [[WHITE_KNIGHT] * 8]
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
        if converted_turn[0] == converted_turn[2] or converted_turn[1] == converted_turn[3]:
            if (type_cell != self.board[converted_turn[2]][converted_turn[3]]){
                if ()
            }
            return True
        return False
        
    def knights_move(self, converted_turn):
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
