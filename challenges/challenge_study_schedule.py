def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None
    result = 0
    for x in permanence_period:
        if type(x[0]) is not int or type(x[1]) is not int:
            return None
        if target_time >= x[0] and target_time <= x[1]:
            result += 1
    return result
