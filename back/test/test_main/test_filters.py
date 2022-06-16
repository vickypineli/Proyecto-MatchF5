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
        schedule={"10:10": "", "10:20": "x", "10:30": "x", "10:40": "x", "10:50": "x"},
    )
    laura = Recruiter(
        id=2,
        name="laura",
        company="company2",
        charge="recruiter",
        locations=["Barcelona"],
        skills=["python", "vue"],
        schedule={"10:10": "x", "10:20": "x", "10:30": "x", "10:40": "", "10:50": "x"},
    )
    joseph = Recruiter(
        id=3,
        name="joseph",
        company="company3",
        charge="recruiter",
        locations=["Bilbao"],
        skills=["php", "angular"],
        schedule={"10:10": "x", "10:20": "x", "10:30": "", "10:40": "x", "10:50": ""},
    )

    coder_list = [ainara, ainhoa, jeff]
    recruiter_list = [perla, laura, joseph]

    number_of_meetings = 5
    return create_list_of_matches(coder_list, recruiter_list, number_of_meetings)


def test_main_should_filter_invalid_combiantions():
    ainara = Coder(1, "ainara")
    perla = Recruiter(1, "perla", "Ibermatica", "perla@gmail.com", "Directora")
    laura = Recruiter(2, "laura", "Kerkaru", "laura@gmail.com", "Directora")
    coder_list = [ainara]
    # coder adicional joker
    recruiter_list = [perla, laura]
    number_of_meetings = 2

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )
    slots = len(recruiter_list) * number_of_meetings

    matches_tuples = transform_matches_to_tuples(list_of_matches)
    list_of_combinations = create_list_of_combinations(matches_tuples, slots)

    filtered_list = filter_invalid_combinations(list_of_combinations)

    number_of_combinations = sum(1 for i in filtered_list)

    assert number_of_combinations == 16


def test_main_should_filter_repeat_meetings():
    ainara = Coder(id=0, name="ainara")
    perla = Recruiter(0, "perla", "Ibermatica", "perla@gmail.com", "Directora")
    laura = Recruiter(1, "laura", "Kerkaru", "laura@gmail.com", "Directora")
    coder_list = [ainara]
    recruiter_list = [perla, laura]
    number_of_meetings = 2

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )
    list_of_matches_tuples = transform_matches_to_tuples(list_of_matches)

    slots = len(recruiter_list) * number_of_meetings

    list_of_combinations = create_list_of_combinations(list_of_matches_tuples, slots)

    pre_filtered_list = filter_invalid_combinations(list_of_combinations)

    filtered_list = filter_repeated_meetings(pre_filtered_list)

    number_of_combinations = sum(1 for i in filtered_list)

    assert number_of_combinations == 7


def test_main_should_return_list_of_matches_with_same_locations():

    list_of_matches = setup()

    list_filtered_by_location = filter_by_location(list_of_matches)

    assert len(list_filtered_by_location) == 50


def test_main_should_return_list_of_matches_with_a_matching_skill():

    list_of_matches = setup()

    list_filtered_by_skill = filter_by_skill(list_of_matches)

    assert len(list_filtered_by_skill) == 45


def test_main_should_return_list_of_matches_with_correct_schedules():
    list_of_matches = setup()

    list_filtered_by_assistance = filter_by_schedules(list_of_matches)

    assert len(list_filtered_by_assistance) == 48


# def test_main_should_return_list_of_matches_with_same_languages():

#     list_of_matches = setup()

#     list_filtered_by_languages = filter_by_languages(list_of_matches)

#     assert len(list_filtered_by_languages) == 5
