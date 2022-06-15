def score(dice: list):
    total = 0
    one = dice.count(1)
    two = dice.count(2)
    three = dice.count(3)
    four = dice.count(4)
    five = dice.count(5)
    six = dice.count(6)

    total += (one // 3) * 1000 + (two // 3) * 200 + (three // 3) * 300 + (four // 3) * 400 + (five // 3) * 500 + \
             (six // 3) * 600
    total += (one % 3) * 100 + (five % 3) * 50
    return total
