if __name__ == '__main__':
    expense_array = []
    with open('./input.txt') as file:
        for line in file:
            expense_array.append(int(line))
    for i in range(len(expense_array)):
        for j in range(len(expense_array)):
            if j != i:
                expense_sum = expense_array[i] + expense_array[j]
                if expense_sum == 2020:
                    expense_mult = expense_array[i] * expense_array[j]
                    print("Part 1: ", expense_array[i], expense_array[j], expense_mult)
    for i in range(len(expense_array)):
        for j in range(len(expense_array)):
            for k in range(len(expense_array)):
                if i != j and i != k and j != k:
                    expense_sum = expense_array[i] + expense_array[j] + expense_array[k]
                    if expense_sum == 2020:
                        expense_mult = expense_array[i] * expense_array[j] * expense_array[k]
                        print("Part 2: ", expense_array[i], expense_array[j], expense_array[k], expense_mult)
