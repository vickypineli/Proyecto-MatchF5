from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import (
    create_list_of_matches,
    create_list_of_combinations,
    filter_invalid_combinations,
    filter_repeated_meetings,
    filter_by_location,
    filter_by_skill,
    filter_by_schedules,
    principal_filter,
)


list_of_matches = [
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["JAVA", "PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 0,
    },
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BILBAO", "BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["PHP"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 1,
    },
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BILBAO", "BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["PHP"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 2,
    },
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BILBAO", "BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 0,
    },
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BILBAO", "BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "", "10:20": "", "10:30": "x"},
        },
        "meeting_time": 1,
    },
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BILBAO", "BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "", "10:20": "", "10:30": "x"},
        },
        "meeting_time": 2,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["JAVA", "PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 0,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["JAVA", "PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 1,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["JAVA", "PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 2,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 0,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 1,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
        },
        "meeting_time": 2,
    },
]
list_of_matches_2 = [
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["JAVA", "PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x"},
        },
        "meeting_time": 0,
    },
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BILBAO", "BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["PHP"],
            "schedule": {"10:10": "x", "10:20": "x"},
        },
        "meeting_time": 1,
    },
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BILBAO", "BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x"},
        },
        "meeting_time": 0,
    },
    {
        "coder": {
            "name": "Ainara Perez",
            "locations": ["BILBAO", "BARCELONA"],
            "skills": ["JAVASCRIPT", "PYTHON"],
            "prom": "BIO",
        },
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "", "10:20": ""},
        },
        "meeting_time": 1,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["JAVA", "PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x"},
        },
        "meeting_time": 0,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Andres",
            "company": "Merkatu",
            "email": "andres@merkatu.com",
            "linkedin": "https://www.linkedin.com/in/Andres",
            "charge": "Director",
            "locations": ["BILBAO"],
            "skills": ["JAVA", "PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x"},
        },
        "meeting_time": 1,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x"},
        },
        "meeting_time": 0,
    },
    {
        "coder": {"name": "joker", "locations": [], "skills": [], "prom": ""},
        "recruiter": {
            "name": "Laura",
            "company": "Ibermatica",
            "email": "laura.ibermatica.es",
            "linkedin": "https://www.linkedin.com/in/Laura",
            "charge": "RH",
            "locations": ["BILBAO"],
            "skills": ["PHP", "PYTHON"],
            "schedule": {"10:10": "x", "10:20": "x"},
        },
        "meeting_time": 1,
    },
]


def test_main_should_filter_invalid_combiantions():

    slots = 4
    list_of_combinations = create_list_of_combinations(list_of_matches_2, slots)

    filtered_list = filter_invalid_combinations(list_of_combinations)

    number_of_combinations = sum(1 for i in filtered_list)

    assert number_of_combinations == 16


def test_main_should_filter_repeat_meetings():

    slots = 4

    list_of_combinations = create_list_of_combinations(list_of_matches_2, slots)

    pre_filtered_list = filter_invalid_combinations(list_of_combinations)

    filtered_list = filter_repeated_meetings(pre_filtered_list)

    number_of_combinations = sum(1 for i in filtered_list)

    assert number_of_combinations == 7


def test_main_should_return_list_of_matches_with_same_locations():

    starting_matches = len(list_of_matches)

    list_filtered_by_location = filter_by_location(list_of_matches)

    expected_coders_without_matching_location = 1

    assert (
        len(list_filtered_by_location)
        == starting_matches - expected_coders_without_matching_location
    )


def test_main_should_return_list_of_matches_with_a_matching_skill():

    starting_matches = len(list_of_matches)

    list_filtered_by_skill = filter_by_skill(list_of_matches)

    expected_recruiter_without_matching_skills = 2

    assert (
        len(list_filtered_by_skill)
        == starting_matches - expected_recruiter_without_matching_skills
    )


def test_main_should_return_list_of_matches_with_correct_schedules():

    starting_matches = len(list_of_matches)

    list_filtered_by_assistance = filter_by_schedules(list_of_matches)

    expected_recruiter_without_matching_schedule = 1

    assert (
        len(list_filtered_by_assistance)
        == starting_matches - expected_recruiter_without_matching_schedule
    )


def test_main_should_filter_inapropiate_matches():

    starting_matches = len(list_of_matches)

    filtered_matches = principal_filter(list_of_matches)

    expected_filtered_matches = 4

    assert len(filtered_matches) == starting_matches - expected_filtered_matches


# def test_main_should_return_list_of_matches_with_same_languages():

#     list_of_matches = setup()

#     list_filtered_by_languages = filter_by_languages(list_of_matches)

#     assert len(list_filtered_by_languages) == 5
