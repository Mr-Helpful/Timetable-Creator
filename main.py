import random

subjectsList = [["Maths - Pure",4],
                ["Maths - Stats",4],
                ["Maths - Mechanics",4],
                ["Compsci",12],
                ["Tech",12],
                ["Physics",12],
                ]

def add_new(subjects,subjectsChosen):
    while True:
        random.shuffle(subjects)
        subjectChoice = subjects[0]
        if(subjectChoice[0] not in subjectsChosen):
            break
    subjectChoice[1] -= 1
    if(subjectChoice[1] == 0):
        subjects.remove(subjectChoice)
    return(subjectChoice[0])

def make_day(subjects,dayspan,dayNo):
    print(f"\nday{dayNo}:")
    subjectsChosen = []
    for i in range(dayspan):
        newSubject = add_new(subjects,subjectsChosen)
        subjectsChosen.append(newSubject)
        print(f"subject{i+1}:".ljust(15," ") + str(newSubject))

for i in range(16):
    make_day(subjectsList,3,i+1)
