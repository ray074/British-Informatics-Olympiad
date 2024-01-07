from itertools import combinations


def calc_points(cards):
    points = 0
    for i in range(2,6):
        combs = combinations(cards, i)
        if i == 2:
            for comb in combs:
                if comb[0] == comb[1]:
                    points += 1
                elif sum(comb) == 15:
                    points += 1
        else:
            for comb in combs:
                if sum(comb) == 15:
                    points += 1
    return points


def main():
    cards = input().split()
    print(calc_points([int(x) for x in cards]))


main()
