from ratemyprofessor import *
from faculty_names import *

facultyFixed = []
profsNotFound = []
facultyDict = {}

for h in LIST_OF_FACULTY_NAMES_GOES_HERE:
    splitNames = h.split()
    if len(splitNames) == 3:
        facultyFixed.append(splitNames[0] + " " + splitNames[2])
    elif len(splitNames) == 4:
        facultyFixed.append(splitNames[0] + " " +  splitNames[3])
    else:
        facultyFixed.append(h)

print(facultyFixed)

for i in facultyFixed:
    #search for prof
    professor = get_professor_by_school_and_name(
        get_school_by_name("Texas A&M University at College Station"), f"{i}")
    #add to dictionary
    try:
        courses = [course.name for course in professor.courses]
        facultyDict[i]=[courses, professor.rating, professor.difficulty, professor.would_take_again]
    except:
        profsNotFound.append(i)
        
        
print(f"facultyDict = {facultyDict}")
print(f"Not found on rate my professor : {profsNotFound}")