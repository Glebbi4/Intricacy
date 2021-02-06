from pip._vendor.msgpack.fallback import xrange


def intricacy_controller(mru):
    def find(mru, labirint, pos, direction):
        left_rotation = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
        }
        way = False
        temp_direction = direction
        count = 0
        stub = 0
        next_step = {'angle': 0, 'value': 10000}
        while count < 4:
            way_free = mru.go()
            x = pos['x'] + temp_direction[0]
            y = pos['y'] + temp_direction[1]
            if (way_free != True):
                labirint[x][y] = 255
                stub += 1
            elif labirint[x][y] == 255:
                stub += 1
                straight_back(mru)
            else:
                way = True
                if next_step['value'] > labirint[x][y]:
                    next_step['angle'] = count
                    next_step['value'] = labirint[x][y]
                straight_back(mru)
            count += 1
            temp_direction = left_rotation[temp_direction]
            mru.turn_left()
        if way != True and stub == 4:
            return False
        if stub == 3:
            next_step['value'] = 255
        return next_step

    def straight_back(mru):
        mru.turn_left()
        mru.turn_left()
        way = mru.go()
        mru.turn_left()
        mru.turn_left()
        return way

    def rotate_and_go(mru, angle, pos, direction):
        left_rotation = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
        }
        for i in range(angle):
            mru.turn_left()
            direction = left_rotation[direction]
        pos['x'] += direction[0]
        pos['y'] += direction[1]
        mru.go()
        return direction

    labirint = []
    SIZE = 1000
    for i in xrange(0, SIZE):
        labirint.append([])
        for j in xrange(0, SIZE):
            labirint[-1].append(0)
    pos = {'x': int(SIZE / 2), 'y': int(SIZE / 2)}
    direction = (1, 0)
    while True:
        labirint[pos['x']][pos['y']] += 1
        if mru.found():
            return True
        next_step = find(mru, labirint, pos, direction)
        if next_step == False or (next_step['value'] > 10 and next_step['value'] != 255):
            return False
        if next_step['value'] == 255:
            labirint[pos['x']][pos['y']] = 255
        direction = rotate_and_go(mru, next_step['angle'], pos, direction)
