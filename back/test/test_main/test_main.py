from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import (
    create_list_of_matches,
    create_list_of_combinations,
    principal_filter,
)

coders = [
    {
        "name": "Ainara Perez",
        "locations": ["BILBAO", "BARCELONA"],
        "skills": ["JAVASCRIPT", "PYTHON"],
        "prom": "BIO",
    }
]

recruiters = [
    {
        "name": "Andres",
        "company": "Merkatu",
        "email": "andres@merkatu.com",
        "linkedin": "https://www.linkedin.com/in/Andres",
        "charge": "Director",
        "locations": ["BILBAO"],
        "skills": ["JAVA", "PHP", "PYTHON"],
        "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
    },
    {
        "name": "Laura",
        "company": "Ibermatica",
        "email": "laura.ibermatica.es",
        "linkedin": "https://www.linkedin.com/in/Laura",
        "charge": "RH",
        "locations": ["BILBAO"],
        "skills": ["PHP", "PYTHON"],
        "schedule": {"10:10": "x", "10:20": "x", "10:30": "x"},
    },
]

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


def test_main_should_create_a_list_of_matches():

    number_of_meetings = 2

    list_of_matches = create_list_of_matches(coders, recruiters, number_of_meetings)
    assert len(list_of_matches) == 8


def test_main_should_create_a_list_of_posible_combinations():
    ainara = Coder("ainara")
    perla = Recruiter("perla", "Ibermatica", "perla@gmail.com", "Directora")
    laura = Recruiter("laura", "Kerkaru", "laura@gmail.com", "Directora")
    coder_list = [ainara]
    recruiter_list = [perla, laura]
    number_of_meetings = 2

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )
    slots = len(recruiter_list) * number_of_meetings

    list_of_combinations = create_list_of_combinations(list_of_matches, slots)
    number_of_combinations = 0
    for combination in list_of_combinations:
        number_of_combinations += 1

    assert len(list_of_matches) == 8
    assert number_of_combinations == 70


def test_should_create_combinations_from_a_filtered_list_of_matches():

    filtered_matches = principal_filter(list_of_matches)

    slots = 6

    list_of_combinations = create_list_of_combinations(filtered_matches, slots)
    number_of_combinations = 0
    for combination in list_of_combinations:
        number_of_combinations += 1

    assert len(filtered_matches) == 7
    assert number_of_combinations == 7
