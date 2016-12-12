from collections import deque

def test_floor(floor_state):
    if floor_state[0] == 0:
        return True
    for i in xrange(7):
        if (floor_state[1] & (1 << i)) and not(floor_state[0] & (1 << i)):
            return False
    return True

def mod_state(floor_state, gens, mics):
    ret0, ret1 = floor_state
    for g in gens:
        ret0 ^= g
    for m in mics:
        ret1 ^= m
    return (ret0, ret1)

def try_move(state, fr, to, gens, mics):
    flfr = mod_state(state[fr], gens, mics)
    if not test_floor(flfr):
        return None
    flto = mod_state(state[to], gens, mics)
    if not test_floor(flto):
        return None
    next_st = list(state)
    next_st[fr] = flfr
    next_st[to] = flto
    return tuple(next_st)

def full_move(mov, q, vis, state, fr, to, gens, mics):
    nxt = try_move(state, fr, to, gens, mics)
    if nxt:
        h = (to, nxt)
        if h not in vis:
            vis.add(h)
            q.appendleft([mov+1, to, nxt])

def full_moves(mov, q, vis, state, floor, gens, mics):
    if floor > 0:
        full_move(mov, q, vis, state, floor, floor-1, gens, mics)
    if floor < 3:
        full_move(mov, q, vis, state, floor, floor+1, gens, mics)

def get_nums(val):
    return [1 << i for i in xrange(7) if val & (1 << i)]

def solve(lines):
    state = ((7, 7), (120, 0), (0, 120), (0, 0))
    q = deque([(0, 0, state)])
    vis = set([(0, state)])
    maxmov = 0
    while q:
        mov, floor, state = q.pop()
        if mov > maxmov:
            maxmov = mov
            print mov
        if state[3] == (127, 127):
            return mov
        gens = get_nums(state[floor][0])
        mics = get_nums(state[floor][1])
        for g in gens:
            full_moves(mov, q, vis, state, floor, [g], [])
        for m in mics:
            full_moves(mov, q, vis, state, floor, [], [m])
        for i in xrange(len(gens)):
            for j in xrange(i+1, len(gens)):
                full_moves(mov, q, vis, state, floor, [gens[i], gens[j]], [])
        for i in xrange(len(mics)):
            for j in xrange(i+1, len(mics)):
                full_moves(mov, q, vis, state, floor, [], [mics[i], mics[j]])
        for g in gens:
            if g in mics:
                full_moves(mov, q, vis, state, floor, [g], [g])
    return -1

lines = [line.strip() for line in open('data.txt').readlines()]
print solve(lines)
