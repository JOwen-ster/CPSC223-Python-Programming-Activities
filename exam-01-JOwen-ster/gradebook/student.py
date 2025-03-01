def homework_average(grades, student_id):
    if student_id not in grades:
        return 0
    getHw = grades[student_id]['homework']
    avg = 0
    for score in getHw:
        avg += score
    return avg / len(getHw)

def laboratory_average(grades, student_id):
    if student_id not in grades:
        return 0
    getLab = grades[student_id]['laboratory']
    avg = 0
    for score in getLab:
        avg += score
    return avg / len(getLab)

def total_weighted_average(grades, student_id):
    if student_id not in grades:
        return 0
    return ((homework_average(grades, student_id) * 0.25) + (laboratory_average(grades, student_id) * 0.75))

