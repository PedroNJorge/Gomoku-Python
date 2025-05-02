class Board:
    def __init__(self):
        # bitboards
        self.white = 0
        self.black = 0
        self.size = 15

    def __str__(self):
        result = []
        for row in range(self.size):
            row_str = []
            for col in range(self.size):
                pos = col + row * self.size
                if (self.white >> pos) & 1:
                    row_str.append("W")
                elif (self.black >> pos) & 1:
                    row_str.append("B")
                else:
                    row_str.append(".")
            result.append(" ".join(row_str))
        return "\n".join(result)

    def place_stone(self, pos, player):
        bit_pos = pos[0] * self.size + pos[1]
        if player == "WHITE":
            self.white |= 1 << bit_pos
            return self.check_win(self.white, bit_pos)
        else:
            self.black |= 1 << bit_pos
            return self.check_win(self.black, bit_pos)

    def check_win(self, bitboard, bit_pos):
        directions = [1, self.size, self.size + 1, self.size - 1]
        for step in directions:
            count = 1
            for i in range(1, 5):
                try:
                    if (bitboard >> (bit_pos + i * step)) & 1:
                        count += 1
                    else:
                        break
                except ValueError:
                    break

            for i in range(1, 5):
                try:
                    if (bitboard >> (bit_pos - i * step)) & 1:
                        count += 1
                    else:
                        break
                except ValueError:
                    break
            if count >= 5:
                return True
        return False
