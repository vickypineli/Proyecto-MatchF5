from src.domain.recruiter import Recruiter
from src.domain.match import Match
from src.domain.coder import Coder
from itertools import combinations
import re


def create_list_of_matches(coders, recruiters, number_of_meetings):
    matchs_list = []
    coders.append(Coder("joker"))
    for coder in coders:
        for recruiter in recruiters:
            for meeting in range(number_of_meetings):
                match = Match(coder, recruiter, meeting)
                matchs_list.append(match)
    return matchs_list


def create_list_of_combinations(list_of_matches, slots):
    list_of_combinations = combinations(list_of_matches, slots)
    return list_of_combinations


def filter_invalid_combinations(list_of_combinations):
    return filter(is_valid_combination, list_of_combinations)

def is_valid_combination(combination):

    time_slot_list = []
    for match in combination:
        time_slot = f"{match.recruiter.name}{match.meeting_time}"
        if time_slot in time_slot_list:
            return False
        time_slot_list.append(time_slot)
    return True

def filter_repeated_meetings(list_of_combinations):
    return filter(has_coders_properly_distributed, list_of_combinations)

def has_coders_properly_distributed(combination):
    meeting_list = []
    coder_times = []
    for match in combination:
        if match.coder.name == "joker":
            continue
        meeting = f"{match.recruiter.name}{match.coder.name}"
        if meeting in meeting_list:
            return False
        coder_time_slot = f"{match.coder.name}{match.meeting_time}"
        meeting_list.append(meeting)
        if coder_time_slot in coder_times:
            return False
        coder_times.append(coder_time_slot)
    return True

def final_result(list_of_matches, slots):
    list_of_combinations = create_list_of_combinations(list_of_matches, slots)
    valid_combinations = filter_invalid_combinations(list_of_combinations)
    final_meetings = filter_repeated_meetings(valid_combinations)
    return final_meetings

def filter_by_location(list_of_matches):
    return [match for match in list_of_matches if match.is_same_location()]

def filter_by_skill(list_of_matches):

    return [match for match in list_of_matches if match.has_skill()]

def filter_by_languages(list_of_matches):

    return [match for match in list_of_matches if match.has_same_languages()]

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

def convert_to_coder(coder_dict):

    skills = select_skills(coder_dict)
    locations = select_locations(coder_dict)
    coder = Coder(name = coder_dict["NOMBRE"]+ " " + coder_dict["APELLIDOS"], locations= locations, skills = skills, prom = coder_dict["PROMOCION"] )

    return coder

def create_list_of_coders(coder_list):
    return [convert_to_coder(coder) for coder in coder_list]

def select_schedule_from_recruiter(recruiter_dict):
    schedule_dict = {}
    for key, value in recruiter_dict.items():
        if re.search("^[0-2][0-3]:[0-5][0-9]", key) is not None:
            schedule_dict[key]=value
    return schedule_dict            

def convert_to_recruiter(recruiter_dict):
    skills = select_skills(recruiter_dict)
    locations = select_locations(recruiter_dict)
    schedules = select_schedule_from_recruiter(recruiter_dict)
    recruiter = Recruiter(name = recruiter_dict["NOMBRE DEL RECRUITER"], company  = recruiter_dict["EMPRESA"], email = ["EMAIL"], charge = recruiter_dict["CARGO"], locations = locations, skills = skills, languages = [], schedule = schedules )

    return recruiter

def create_list_of_recruiters(recruiters_list):
    return [convert_to_recruiter(recruiter) for recruiter in recruiters_list]
