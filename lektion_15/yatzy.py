def counter(dice):
    """
    Counts how many of each numbers is in dice roll
    """
    count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for die in dice:
        if die == 1:
            count[1] += 1
        elif die == 2:
            count[2] += 1
        elif die == 3:
            count[3] += 1
        elif die == 4:
            count[4] += 1
        elif die == 5:
            count[5] += 1
        else:
            count[6] += 1

    return(count)

