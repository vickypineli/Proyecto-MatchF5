from src.domain.recruiter import Recruiter
from src.domain.match import Match
from src.domain.coder import Coder
from itertools import combinations
import re


def create_list_of_matches(coders, recruiters, number_of_meetings):
    matchs_list = []
    coders.append(Coder(0, "joker"))
    for coder in coders:
        for recruiter in recruiters:
            for meeting in range(number_of_meetings):
                match = Match(coder, recruiter, meeting)
                matchs_list.append(match)
    return matchs_list


def transform_matches_to_tuples(list_of_matches):
    return [match.to_tuple() for match in list_of_matches]


def transform_tuples_to_matches(list_of_tuples, list_of_matches):
    return [
        match
        for match in list_of_matches
        for tuple in list_of_tuples
        if tuple[0] == match.match_code
    ]


def create_list_of_combinations(list_of_matches, slots):
    list_of_combinations = combinations(list_of_matches, slots)
    return list_of_combinations


def filter_invalid_combinations(list_of_combinations):
    return filter(is_valid_combination, list_of_combinations)


def is_valid_combination(comb):
    return len(comb) == len({match[1] for match in comb})


def filter_repeated_meetings(list_of_combinations):
    pre_filter = filter(is_meeting_repeated, list_of_combinations)
    return filter(is_coder_repeated, pre_filter)


def is_meeting_repeated(comb):
    return (
        len(comb)
        == len({match[2] for match in comb})
        + (sum(1 for match in comb if match[2] == "0") - 1)
        if sum(1 for match in comb if match[2] == "0") >= 1
        else 0
    )


def is_coder_repeated(comb):

    return (
        len(comb)
        == len({match[3] for match in comb})
        + (sum(1 for match in comb if match[3] == "0") - 1)
        if sum(1 for match in comb if match[3] == "0") >= 1
        else 0
    )


# def has_coders_properly_distributed(combination):
#     meeting_list = []
#     coder_times = []
#     for match in combination:
#         if match.coder.name == "joker":
#             continue
#         meeting = f"{match.recruiter.name}{match.coder.name}"
#         if meeting in meeting_list:
#             return False
#         coder_time_slot = f"{match.coder.name}{match.meeting_time}"
#         meeting_list.append(meeting)
#         if coder_time_slot in coder_times:
#             return False
#         coder_times.append(coder_time_slot)
#     return True


def final_result(list_of_matches, slots):
    matches_tuples = transform_matches_to_tuples(list_of_matches)
    list_of_combinations = create_list_of_combinations(matches_tuples, slots)
    valid_combinations = filter_invalid_combinations(list_of_combinations)
    final_meetings = filter_repeated_meetings(valid_combinations)
    return final_meetings


def filter_by_location(list_of_matches):

    return [match for match in list_of_matches if match.is_same_location()]


def filter_by_skill(list_of_matches):

    return [match for match in list_of_matches if match.has_skill()]


def filter_by_schedules(list_of_matches):
    return [match for match in list_of_matches if match.has_schedule()]


# def filter_by_languages(list_of_matches):

#     return [match for match in list_of_matches if match.has_same_languages()]


def principal_filter(list_of_matches):
    location_filter = filter_by_location(list_of_matches)
    skill_filter = filter_by_skill(location_filter)
    final_filter = filter_by_schedules(skill_filter)
    return final_filter


def select_skills(item_dict):
    skills = []
    for key, value in item_dict.items():
        if key.startswith("S-") and value == "x":
            skills.append(key[2:])
    return skills


def select_locations(item_dict):
    locations = []
    for key, value in item_dict.items():
        if key.startswith("L-") and value == "x":
            locations.append(key[2:])
    return locations


def convert_to_coder(coder_dict, index):

    skills = select_skills(coder_dict)
    locations = select_locations(coder_dict)
    coder = Coder(
        id=index + 1,
        name=coder_dict["NOMBRE"] + " " + coder_dict["APELLIDOS"],
        locations=locations,
        skills=skills,
        prom=coder_dict["PROMOCION"],
    )

    return coder


def create_list_of_coders(coder_list):
    return [convert_to_coder(coder, index) for index, coder in enumerate(coder_list)]


def select_schedule_from_recruiter(recruiter_dict):
    schedule_dict = {}
    for key, value in recruiter_dict.items():
        if re.search("^[0-2][0-3]:[0-5][0-9]", key) is not None:
            schedule_dict[key] = value
    return schedule_dict


def convert_to_recruiter(recruiter_dict, index):
    skills = select_skills(recruiter_dict)
    locations = select_locations(recruiter_dict)
    schedules = select_schedule_from_recruiter(recruiter_dict)
    recruiter = Recruiter(
        id=index + 1,
        name=recruiter_dict["NOMBRE DEL RECRUITER"],
        company=recruiter_dict["EMPRESA"],
        email=recruiter_dict["EMAIL"],
        linkedin=recruiter_dict["LINKEDIN"],
        charge=recruiter_dict["CARGO"],
        locations=locations,
        skills=skills,
        languages=[],
        schedule=schedules,
    )

    return recruiter


def create_list_of_recruiters(recruiters_list):
    return [
        convert_to_recruiter(recruiter, index)
        for index, recruiter in enumerate(recruiters_list)
    ]


def count_number_of_slots(recruiter_obj_list):
    recruiter = recruiter_obj_list[0]
    slots = len(recruiter.schedule)
    return slots


def select_solution(list_of_solutions):
    for solution in list_of_solutions:

        return solution


def solution_to_dict(solution, locations, skills):
    recruiters = []
    list_of_dicts = []
    for match in solution:
        recruiter = match.recruiter
        coder = match.coder
        schedule = recruiter.schedule
        schedule_hours = list(schedule.keys())
        hour = schedule_hours[match.meeting_time]
        if recruiter.name in recruiters:
            list_position = next(
                (
                    i
                    for i, item in enumerate(list_of_dicts)
                    if item["NOMBRE Y APELLIDOS"] == recruiter.name
                )
            )
            list_of_dicts[list_position][hour] = coder.prom_and_name()
        else:
            this_dict = {
                "EMPRESA": recruiter.company,
                "NOMBRE Y APELLIDOS": recruiter.name,
                "EMAIL": recruiter.email,
                "CARGO": recruiter.charge,
                "LINKEDIN": recruiter.linkedin,
            }
            possible_locations = {key: "" for key in locations}
            solution_locations = recruiter.location_dict(possible_locations)
            this_dict.update(solution_locations)
            possible_skills = {key: "" for key in skills}
            solution_skills = recruiter.skills_dict(possible_skills)
            this_dict.update(solution_skills)
            this_dict.update(recruiter.schedule)
            this_dict[hour] = coder.prom_and_name()
            list_of_dicts.append(this_dict)
            recruiters.append(recruiter.name)
    return list_of_dicts


def get_all_locations(recruiter_dict):
    location_dict = {}
    for key, value in location_dict.items():
        if key.startswith("L-"):
            dict = {key[2:]: ""}
            location_dict.update(dict)
    return location_dict


def get_all_skills(recruiter_dict):
    skills_dict = {}
    for key, value in skills_dict.items():
        if key.startswith("S-"):
            dict = {key[2:]: ""}
            skills_dict.update(dict)
    return skills_dict
