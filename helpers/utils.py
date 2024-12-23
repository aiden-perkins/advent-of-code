

def traverse(x, y, card = True, diag = True, igs = None, d = 1):
    if not igs:
        igs = []

    card_deltas = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1),
    }

    diag_deltas = {
        'NE': (-1, 1),
        'NW': (-1, -1),
        'SE': (1, 1),
        'SW': (1, -1),
    }
    if card:
        for side, (dx, dy) in card_deltas.items():
            if side not in igs:
                yield x + (dx * d), y + (dy * d)
    if diag:
        for side, (dx, dy) in diag_deltas.items():
            if side not in igs:
                yield x + (dx * d), y + (dy * d)


def value_traverse(x, y, arr, card = True, diag = True, igs = None, d = 1):
    arr_len = len(arr)
    for nx, ny in traverse(x, y, card, diag, igs, d):
        if in_bounds(nx, ny, arr_len):
            yield arr[nx][ny], (nx, ny)


def find_val(arr, function):
    for i, row in enumerate(arr):
        for j, val in enumerate(row):
            if function(val):
                yield i, j


def find_one(arr, t_val):
    for i, row in enumerate(arr):
        for j, val in enumerate(row):
            if val == t_val:
                return i, j


def in_bounds(x, y, arr_len):
    return 0 <= x < arr_len and 0 <= y < arr_len
