from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import (
    create_list_of_matches,
    transform_matches_to_tuples,
    create_list_of_combinations,
    filter_recruiter_tuples,
    filter_tuples,
)


def test_main_should_filter_invalid_combiantions():
    ainara = Coder(id=0, name="ainara")
    perla = Recruiter(0, "perla", "Ibermatica", "perla@gmail.com", "Directora")
    laura = Recruiter(1, "laura", "Kerkaru", "laura@gmail.com", "Directora")
    coder_list = [ainara]
    # coder adicional joker
    recruiter_list = [perla, laura]
    number_of_meetings = 2

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )
    list_of_matches_tuples = transform_matches_to_tuples(list_of_matches)

    slots = len(recruiter_list) * number_of_meetings

    list_of_combinations = create_list_of_combinations(list_of_matches_tuples, slots)

    filtered_list = filter_recruiter_tuples(list_of_combinations)

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

    filtered_list = filter_tuples(list_of_combinations)

    number_of_combinations = sum(1 for i in filtered_list)

    for i in filtered_list:
        print(i)

    assert number_of_combinations == 7
