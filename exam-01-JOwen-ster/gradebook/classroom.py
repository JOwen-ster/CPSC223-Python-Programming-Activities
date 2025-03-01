# I thought this we had only till 7:50
#so I committed without finishing the docstring for external methods I made
#and didnt optimze what I wanted

def assignments(grades: dict) -> int:
    '''
    Made to find how many assignments there are.
    '''
    length = 0
    for student in grades.keys():
        if len(grades[student]['homework']) > length:
            length = len(grades[student]['homework'])
    return length


def labs(grades: dict) -> int:
    '''
    Made to find how many labs there are.
    '''
    length = 0
    for student in grades.keys():
        if len(grades[student]['laboratory']) > length:
            length = len(grades[student]['laboratory'])
    return length



def homework_average(grades: dict, assignment_no: int) -> float:
    if assignment_no not in range(assignments(grades)):
        return 0
    avg = 0;
    counter = 0;
    for student in grades.keys():
        avg += grades[student]['homework'][assignment_no]
        counter += 1
    return avg / counter

def homework_average_average(grades: dict) -> float:
    avg = 0;
    counter = 0;
    for i in range(assignments(grades)):
        avg += homework_average(grades, i)
        counter += 1
    return avg / counter

def laboratory_average(grades: dict, assignment_no: int) -> float:
    if assignment_no not in range(labs(grades)):
        return 0
    avg = 0;
    counter = 0;
    for student in grades.keys():
        avg += grades[student]['laboratory'][assignment_no]
        counter += 1
    return avg / counter

def laboratory_average_average(grades: dict) -> float: 
    avg = 0;
    counter = 0;
    for i in range(labs(grades)):
        avg += laboratory_average(grades, i)
        counter += 1
    return avg / counter

def total_weighted_average_average(grades: dict) -> float:
    avgHw = homework_average_average(grades)
    avgLab = laboratory_average_average(grades)
    return (avgHw * 0.25) + (avgLab * 0.75)

