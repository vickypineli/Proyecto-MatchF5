from time import time
from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import create_list_of_matches, create_list_of_combinations

ainara = Coder("ainara", ["Bilbao", "Barcelona"], ["python", "vue"])

perla = Recruiter("perla", ["Bilbao"], ["python", "angular"], ["ingles"])
laura = Recruiter("laura", ["Bilbao"], ["python", "angular"], ["ingles"])

coder_list = [ainara]
recruiter_list = [perla, laura]

number_of_meetings = 2
match_list = create_list_of_matches(coder_list, recruiter_list, number_of_meetings)

match_list_printable = []
for match in match_list:

    match_list_printable.append(match.to_str())

print(match_list_printable)

time_slots = len(recruiter_list * number_of_meetings)
solutions_list = create_list_of_combinations(match_list, time_slots)

solution_number = 0
for solution in solutions_list:
    solution_str = ""
    solution_number += 1
    for match in solution:
        solution_str += f"{match.to_str()} "

    print(solution_number, solution_str)
