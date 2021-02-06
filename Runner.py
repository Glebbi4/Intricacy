def print_intricacy(intricacy, x, y):
    for i in range(len(intricacy)):
        s = ''
        for j in range(len(intricacy)):
            if i == x and j == y:
                s += 'X'
            elif intricacy[i][j] == 1:
                s += '1'
            else:
                s += '.'
        print(s)
    print(' ')


class IntricacyRunner(object):
    def __init__(self, intricacy, start, finish):
        self.__intricacy = intricacy
        self.__rotation = (1, 0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__intricacy) - 1 \
                or y > len(self.__intricacy) - 1 \
                or x < 0 or y < 0 \
                or self.__intricacy[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        print_intricacy(self.__intricacy, self.__x, self.__y)
        return True

    def turn_left(self):
        left_rotation = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self

    def turn_right(self):
        right_rotation = {
            (1, 0): (0, 1),
            (0, -1): (1, 0),
            (-1, 0): (0, -1),
            (0, 1): (-1, 0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self

    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]
