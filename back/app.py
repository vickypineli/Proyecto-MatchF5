from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import (
    create_list_of_matches,
    create_list_of_combinations,
    filter_invalid_combinations,
    filter_repeated_meetings,
)
import time

ainara = Coder("ainara")
jeff = Coder("jeff")
joseph = Coder("joseph")
ainhoa = Coder("ainhoa")
iker = Coder("iker")

perla = Recruiter("perla")
laura = Recruiter("laura")
ana = Recruiter("ana")


coder_list = [ainara, jeff]
recruiter_list = [perla, laura]

number_of_meetings = 2

match_list = create_list_of_matches(coder_list, recruiter_list, number_of_meetings)

match_list_printable = []
for match in match_list:

    match_list_printable.append(match.to_str())

print(match_list_printable)


time_slots = len(recruiter_list * number_of_meetings)

start_time = time.time()

solutions_list = create_list_of_combinations(match_list, time_slots)

pre_filtered_solutions = filter_invalid_combinations(solutions_list)

filtered_solutions = filter_repeated_meetings(pre_filtered_solutions)

print("--- %s seconds ---" % (time.time() - start_time))

# print(sum(1 for i in filtered_solutions))

solution_number = 0
for solution in filtered_solutions:
    solution_str = ""
    solution_number += 1
    for match in solution:
        solution_str += f"{match.to_str()} "

    print(solution_number, solution_str)
