import re

def findOneShinyGold(rule, rule_dict):
    bags_held = rule_dict[rule]
    for bags in bags_held:
        if bags != 'no other bags':
            amount, type = re.match(r'([0-9]+|no) ([a-z ]+)', bags).groups()
            if amount == '1':
                type += 's'
            if type == 'shiny gold bags':
                return True
            result = findOneShinyGold(type, rule_dict)
            if result:
                return result
        else:
            return False
    return False

def getTotalBagsInRule(rule, rule_dict):
    bags_held = rule_dict[rule]
    total = 1
    for bags in bags_held:
        if bags != 'no other bags':
            amount, type = re.match(r'([0-9]+|no) ([a-z ]+)', bags).groups()
            if amount == '1':
                type += 's'
            total += int(amount) * getTotalBagsInRule(type, rule_dict)
    return total


if __name__ == '__main__':
    with open('day7/input.txt') as rules:
        rule_dict = {}
        for rule in rules:
            subject, objects = rule.split(' contain ')
            objects = objects[:-2].split(', ')
            rule_dict[subject] = objects
        bags_that_can_contain_shiny_gold = 0
        for rule in rule_dict:
            result = findOneShinyGold(rule, rule_dict)
            if result:
                bags_that_can_contain_shiny_gold += 1
        print(bags_that_can_contain_shiny_gold)
        print(getTotalBagsInRule("shiny gold bags", rule_dict) - 1)