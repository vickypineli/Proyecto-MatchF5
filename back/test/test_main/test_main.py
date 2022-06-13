from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import (
    create_list_of_matches,
    create_list_of_combinations,
    filter_invalid_combinations,
    filter_repeated_meetings,
    filter_by_location,
    filter_by_skill,
    principal_filter,
)


def setup():

    ainara = Coder(
        id=0, name="ainara", locations=["Bilbao", "Barcelona"], skills=["python", "vue"]
    )
    ainhoa = Coder(id=1, name="ainhoa", locations=["Bilbao"], skills=["python", "vue"])
    jeff = Coder(id=2, name="jeff", locations=["Bilbao"], skills=["python", "vue"])

    perla = Recruiter(
        id=0,
        name="perla",
        company="company1",
        charge="recruiter",
        locations=["Bilbao"],
        skills=["python", "angular"],
        schedule={"10:10": "x", "10:20": "x", "10:30": "x"},
    )
    laura = Recruiter(
        id=1,
        name="laura",
        company="company2",
        charge="recruiter",
        locations=["Barcelona"],
        skills=["python", "vue"],
        schedule={"10:10": "x", "10:20": "x", "10:30": "x"},
    )
    joseph = Recruiter(
        id=2,
        name="joseph",
        company="company3",
        charge="recruiter",
        locations=["Bilbao"],
        skills=["php", "angular"],
        schedule={"10:10": "x", "10:20": "x", "10:30": "x"},
    )

    coder_list = [ainara, ainhoa, jeff]
    recruiter_list = [perla, laura, joseph]

    number_of_meetings = 3
    return create_list_of_matches(coder_list, recruiter_list, number_of_meetings)


def test_main_should_create_a_list_of_matches():
    ainara = Coder(id=0, name="ainara")
    perla = Recruiter(0, "perla", "Ibermatica", "perla@gmail.com", "Directora")
    laura = Recruiter(1, "laura", "Kerkaru", "laura@gmail.com", "Directora")
    coder_list = [ainara]
    recruiter_list = [perla, laura]
    number_of_meetings = 2

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )
    assert len(list_of_matches) == 8


def test_main_should_filter_inapropiate_matches():
    list_of_matches = setup()

    filtered_matches = principal_filter(list_of_matches)

    assert len(filtered_matches) == 21


def test_main_should_create_a_list_of_posible_combinations():
    ainara = Coder(id=0, name="ainara")
    perla = Recruiter(0, "perla", "Ibermatica", "perla@gmail.com", "Directora")
    laura = Recruiter(1, "laura", "Kerkaru", "laura@gmail.com", "Directora")
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
    list_of_matches = setup()

    filtered_matches = principal_filter(list_of_matches)

    slots = 9

    list_of_combinations = create_list_of_combinations(filtered_matches, slots)
    number_of_combinations = 0
    for combination in list_of_combinations:
        number_of_combinations += 1

    assert len(filtered_matches) == 21
    assert number_of_combinations == 293930
