# Complete the function below.
from collections import defaultdict

def checkIllumination(n, lamps, queries):
    its_lit = []

    x_hash = defaultdict(list)
    y_hash = defaultdict(list)
    d1_hash = defaultdict(list)
    d2_hash = defaultdict(list)

    for lamp in lamps:
        x, y = lamp[0], lamp[1]

        x_hash[x].append(lamp)
        y_hash[y].append(lamp)
        d1_hash[x-y].append(lamp)
        d2_hash[x+y].append(lamp)

    for q in queries:
        x, y = q[0], q[1]

        if check_x(x, y, x_hash) or check_y(x, y, y_hash) or check_d1(x, y, d1_hash) or check_d2(x, y, d2_hash):
            its_lit.append("LIGHT")
        else:
            its_lit.append("DARK")

    return its_lit

def check_x(x, y, hash):
    for lamp in hash[x]:
        if left_on(x, y, lamp):
            return True
    return False

def check_y(x, y, hash):
    for lamp in hash[y]:
        if left_on(x, y, lamp):
            return True
    return False

# diagonal 1: each runs bottom left to top right
def check_d1(x, y, hash):
    for lamp in hash[x-y]:
        if left_on(x, y, lamp):
            return True
    return False

# diagonal 2: each runs top left to bottom right
def check_d2(x, y, hash):
    for lamp in hash[x+y]:
        if left_on(x, y, lamp):
            return True
    return False

def left_on(x, y, lamp):
    l_x, l_y = lamp[0], lamp[1]
    if l_x < x - 1 or l_x > x + 1 or l_y < y - 1 or l_y > y + 1:
        return True
    else:
        return False