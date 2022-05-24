from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import (
    create_list_of_matches,
    create_list_of_combinations,
    filter_invalid_combinations,
    filter_repeated_meetings,
    filter_by_location,
    filter_by_skill,
    filter_by_languages,
)


def test_main_should_filter_invalid_combiantions():
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

    filtered_list = filter_invalid_combinations(list_of_combinations)

    number_of_combinations = sum(1 for i in filtered_list)

    assert number_of_combinations == 16


def test_main_should_filter_repeat_meetings():
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

    pre_filtered_list = filter_invalid_combinations(list_of_combinations)

    filtered_list = filter_repeated_meetings(pre_filtered_list)

    number_of_combinations = sum(1 for i in filtered_list)

    assert number_of_combinations == 7
    

    
    


# def test_main_should_return_list_of_matches_with_same_locations():

#     list_of_matches = setup()

#     list_filtered_by_location = filter_by_location(list_of_matches)

#     assert len(list_filtered_by_location) == 35


# def test_main_should_return_list_of_matches_with_a_matching_skill():

#     list_of_matches = setup()

#     list_filtered_by_skill = filter_by_skill(list_of_matches)

#     assert len(list_filtered_by_skill) == 30


# def test_main_should_return_list_of_matches_with_same_languages():

#     list_of_matches = setup()

#     list_filtered_by_languages = filter_by_languages(list_of_matches)

#     assert len(list_filtered_by_languages) == 5
