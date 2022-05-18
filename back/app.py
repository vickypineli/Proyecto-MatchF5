from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import (
    create_list_of_matches,
    create_list_of_combinations,
    filter_invalid_combinations,
    filter_repeated_meetings,
)

ainara = Coder("ainara")
jeff = Coder("jeff")

perla = Recruiter("perla")
laura = Recruiter("laura")


coder_list = [ainara, jeff]
recruiter_list = [perla, laura]

number_of_meetings = 2

match_list = create_list_of_matches(coder_list, recruiter_list, number_of_meetings)

time_slots = len(recruiter_list * number_of_meetings)

solutions_list = create_list_of_combinations(match_list, time_slots)

pre_filtered_solutions = filter_invalid_combinations(solutions_list)

filtered_solutions = filter_repeated_meetings(pre_filtered_solutions)

solution_number = 0

for solution in filtered_solutions:
    hours = []
    for match in solution:
        if match.meeting_time in hours:
            continue
        hours.append(match.meeting_time)
    header = "| Rec/H |"
    hours = [int(hour) for hour in hours]
    hours.sort()
    for hour in hours:
        header += f" 10:{str(hour)}0 |"

    recruiters = []
    for match in solution:
        if match.recruiter.name in recruiters:
            continue
        recruiters.append(match.recruiter.name)
    solution_number += 1
    print(f"-------Solución {solution_number}---------")
    print(header)
    for recruiter in recruiters:
        row_str = f"| {recruiter} | "
        coders = []
        for match in solution:
            if match.recruiter.name == recruiter:
                coder_with_time = {
                    "time": match.meeting_time,
                    "coder": match.coder.name,
                }
                coders.append(coder_with_time)
        coders.sort(key=lambda dict: dict["time"])
        for coder in coders:
            if coder["coder"] == "joker":
                row_str += f" ----- |"
                continue
            row_str += f" {coder['coder']} |"

        print(row_str)

    print("\n")
