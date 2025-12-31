from collections import deque
from fractions import Fraction
from itertools import product


ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

tt = 0

for ll in ls:
    ll = ll.split('] (')
    indicators, ll = ll[0][1:], ll[1]
    ll = ll.split(') {')
    buttonsstr, jolts = ll[0], ll[1][:-1]
    buttons = buttonsstr.split(') (')
    cindicators = len(indicators)
    indb = 0
    for i, ind in enumerate(indicators):
        if ind == '#':
            indb |= (1 << i)
    binbuttons = []
    for buttonp in buttons:
        buttonb = 0
        for v in buttonp.split(','):
            buttonb |= (1 << int(v))
        binbuttons.append(buttonb)

    dist = [-1] * (1 << cindicators)
    q = deque()
    start = 0
    dist[start] = 0
    q.append(start)
    while q:
        state = q.popleft()
        d = dist[state]

        for mask in binbuttons:
            nxt = state ^ mask
            if dist[nxt] == -1:
                dist[nxt] = d + 1
                if nxt == indb:
                    tt += dist[nxt]
                    break
                q.append(nxt)
        else:
            continue
        break

print(tt)

""" Part 2 """


def to_fraction_matrix(buttons, targets):
    num_counters = len(targets)
    matrix = []
    for r in range(num_counters):
        row = []
        for btn_indices in buttons:
            row.append(Fraction(1, 1) if r in btn_indices else Fraction(0, 1))
        row.append(Fraction(targets[r], 1))
        matrix.append(row)
    return matrix


def compute_rref(matrix):
    if not matrix:
        return matrix, []
    m = [row[:] for row in matrix]
    rows = len(m)
    cols = len(m[0])
    pivots = []
    r = 0
    for c in range(cols - 1):
        if r >= rows:
            break
        pivot_row = r
        while pivot_row < rows and m[pivot_row][c] == 0:
            pivot_row += 1
        if pivot_row == rows:
            continue
        m[r], m[pivot_row] = m[pivot_row], m[r]
        pivots.append(c)
        pivot_val = m[r][c]
        m[r] = [x / pivot_val for x in m[r]]
        for i in range(rows):
            if i != r:
                factor = m[i][c]
                m[i] = [val - factor * m[r][j] for j, val in enumerate(m[i])]
        r += 1
    return m, pivots


def solve_machine(buttons, targets):
    num_buttons = len(buttons)
    matrix = to_fraction_matrix(buttons, targets)
    rref_mat, pivots = compute_rref(matrix)
    for row in rref_mat:
        all_zeros = all(x == 0 for x in row[:-1])
        if all_zeros and row[-1] != 0:
            return float('inf')
    free_vars = [i for i in range(num_buttons) if i not in pivots]
    bounds = []
    for f_idx in free_vars:
        affected_counters = buttons[f_idx]
        if not affected_counters:
            bounds.append(range(1))
        else:
            limit = min(targets[c] for c in affected_counters)
            bounds.append(range(limit + 1))
    best_total = float('inf')
    for free_vals in product(*bounds):
        x = [Fraction(0, 1)] * num_buttons
        for i, val in enumerate(free_vals):
            x[free_vars[i]] = Fraction(val, 1)
        valid = True
        current_sum = sum(free_vals)
        if current_sum >= best_total:
            continue
        for r, p_idx in enumerate(pivots):
            row = rref_mat[r]
            constant = row[-1]
            sum_free = sum(row[f] * x[f] for f in free_vars)
            val = constant - sum_free
            if val < 0 or val.denominator != 1:
                valid = False
                break
            x[p_idx] = val
            current_sum += int(val)
        if valid:
            if current_sum < best_total:
                best_total = current_sum
    return best_total if best_total != float('inf') else 0

grand_total = 0

for ll in ls:
    parts = ll.split('] (')
    rest = parts[1]
    parts2 = rest.split(') {')
    buttons_str = parts2[0]
    targets_str = parts2[1][:-1]
    targets = list(map(int, targets_str.split(',')))
    raw_buttons = buttons_str.split(') (')
    buttons = []
    for rb in raw_buttons:
        if not rb.strip():
            inds = []
        else:
            inds = [int(v) for v in rb.split(',') if v.strip()]
        buttons.append(set(inds))
    result = solve_machine(buttons, targets)
    grand_total += result

print(grand_total)

