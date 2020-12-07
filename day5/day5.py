def getRow(seat):
    current_distance = 127
    min_range = 0
    max_range = 127
    for i in range(7):
        current_distance /= 2
        if seat[i] == 'F':
            max_range = min_range + current_distance
        else:
            min_range = max_range - current_distance
    return min_range

def getColumn(seat):
    current_distance = 7
    min_range = 0
    max_range = 7
    for i in range(7, 10):
        current_distance /= 2
        if seat[i] == 'L':            
            max_range = min_range + current_distance
        else:
            min_range = max_range - current_distance
    return min_range

def getID(seat):
    row = getRow(seat)
    column = getColumn(seat)
    return row * 8 + column

if __name__ == "__main__":
    with open('day5/input.txt') as boarding:
        id_list = []
        for seat in boarding:
            id_list.append(getID(seat))
        id_list.sort()
        print(max(id_list))
        for i in range(len(id_list) - 1):
            if id_list[i] + 1 != id_list[i + 1]:
                print(id_list[i], id_list[i+1])