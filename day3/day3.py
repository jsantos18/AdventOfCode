def getTree(index, line):
    field = list(line)[:len(line) -1]
    square = field[index % len(field)]
    if square == '#':
        return 1
    return 0

if __name__ == "__main__":
    with open("day3/input.txt") as landscape:
        index = 0
        trees_hit = 0
        r1d1, r5d1, r7d1, r1d2 = 0, 0, 0, 0
        r1d1i, r5d1i, r7d1i, r1d2i = 0, 0, 0, 0
        for field in landscape:
            trees_hit += getTree(index, field)
            index += 3

            r1d1 += getTree(r1d1i, field)
            r5d1 += getTree(r5d1i, field)
            r7d1 += getTree(r7d1i, field)
            if r1d2i % 2 == 0:
                print(r1d2i, r1d2i/2)
                r1d2 += getTree(r1d2i/2, field)
            
            r1d1i += 1
            r5d1i += 5
            r7d1i += 7
            r1d2i += 1
            
        print("Trees Collided With: ", trees_hit)
        print("Trees Collided With Multiplied: ", r1d1 * r5d1 * r7d1 * r1d2 * trees_hit)