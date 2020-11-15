def solution():
    from collections import Counter

    N = int(input())
    Dice_num = [list(input().split()) for i in range(N)]

    prizes = []
    for num in Dice_num:
        try:
            common_num = Counter(num).most_common(2)
            first_num = common_num[0]
            second_num = common_num[1]
        except:
            pass
        if first_num[1] == 4:
            prizes.append(50000 + int(first_num[0]) * 5000)
        elif first_num[1] == 3:
            prizes.append(10000 + int(first_num[0]) * 1000)
        elif first_num[1] == 2:
            if second_num[1] == 2:
                prizes.append(2000 + int(first_num[0]) * 500 + int(second_num[0]) * 500)
            else:
                prizes.append(1000 + int(first_num[0]) * 100)
        else:
            prizes.append(max([int(i) for i in num]) * 100)
    return max(prizes)