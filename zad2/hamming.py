def distance(a, b):
    if len(a) != len(b):
        raise ValueError("Must be an equal length")
    else:
        calculated_distance = 0
        for x, (i, j) in enumerate(zip(a, b)):
            if i != j:
                calculated_distance += 1
    return calculated_distance