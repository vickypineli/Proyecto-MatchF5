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
    transform_matches_to_tuples,
)


def setup():

    ainara = Coder(
        id=1, name="ainara", locations=["Bilbao", "Barcelona"], skills=["python", "vue"]
    )
    ainhoa = Coder(id=2, name="ainhoa", locations=["Bilbao"], skills=["python", "vue"])
    jeff = Coder(id=3, name="jeff", locations=["Bilbao"], skills=["python", "vue"])

    perla = Recruiter(
        id=1,
        name="perla",
        company="company1",
        charge="recruiter",
        locations=["Bilbao"],
        skills=["python", "angular"],
        schedule={"10:10": "x", "10:20": "x", "10:30": "x"},
    )
    laura = Recruiter(
        id=2,
        name="laura",
        company="company2",
        charge="recruiter",
        locations=["Barcelona"],
        skills=["python", "vue"],
        schedule={"10:10": "x", "10:20": "x", "10:30": "x"},
    )
    joseph = Recruiter(
        id=3,
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
    ainara = Coder(1, "ainara")
    perla = Recruiter(1, "perla", "Ibermatica", "perla@gmail.com", "Directora")
    laura = Recruiter(2, "laura", "Kerkaru", "laura@gmail.com", "Directora")
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
    ainara = Coder(1, "ainara")
    perla = Recruiter(1, "perla", "Ibermatica", "perla@gmail.com", "Directora")
    laura = Recruiter(2, "laura", "Kerkaru", "laura@gmail.com", "Directora")
    coder_list = [ainara]
    recruiter_list = [perla, laura]
    number_of_meetings = 2

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )
    slots = len(recruiter_list) * number_of_meetings

    matches_tuples = transform_matches_to_tuples(list_of_matches)
    list_of_combinations = create_list_of_combinations(matches_tuples, slots)
    number_of_combinations = 0
    for combination in list_of_combinations:
        number_of_combinations += 1

    assert len(list_of_matches) == 8
    assert number_of_combinations == 70


def test_should_create_combinations_from_a_filtered_list_of_matches():
    list_of_matches = setup()

    filtered_matches = principal_filter(list_of_matches)

    slots = 9

    matches_tuples = transform_matches_to_tuples(filtered_matches)
    list_of_combinations = create_list_of_combinations(matches_tuples, slots)
    number_of_combinations = sum(1 for i in list_of_combinations)

    assert len(filtered_matches) == 21
    assert number_of_combinations == 293930
