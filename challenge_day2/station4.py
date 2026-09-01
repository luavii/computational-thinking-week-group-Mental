def solution_station_4(x):
    if x <= 1:
        tf = True
    else:
        tf = False

        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                tf = True
                break

    return tf