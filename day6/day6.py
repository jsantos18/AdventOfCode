def getUniques(group):
    answers = []
    for answer in group:
        if answer != '\n' and answer not in answers:
            answers.append(answer)
    return len(answers)

def getIntersection(group):
    people = group.split('\n')[:-1]
    answers = list(set([x for x in people[0]]))
    for i in range(1, len(people)):
        new_answers = list(set([x for x in people[i]]))
        answers = [x for x in answers if x in new_answers]
    return len(answers)

if __name__ == '__main__':
    with open('day6/input.txt') as declarations:
        split_declarations = []
        current_declaration = ""
        for line in declarations:
            if line != '\n':
                current_declaration += line
            else:
                split_declarations.append(current_declaration)
                current_declaration = ""
        sum1 = 0
        sum2 = 0
        for group in split_declarations:
            sum1 += getUniques(group)
            sum2 += getIntersection(group)

        print(sum1)
        print(sum2)