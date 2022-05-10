from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import create_list_of_matches, filter_by_location, filter_by_skill


def setup():
    ainara = Coder("ainara", "Bilbao", ["python", "vue"])
    ainhoa = Coder("ainhoa", "Bilbao", ["python", "vue"])
    jeff = Coder("jeff", "Bilbao", ["python", "vue"])

    perla = Recruiter("perla", "Bilbao", ["python", "angular"])
    laura = Recruiter("laura", "Barcelona", ["python", "vue"])
    joseph = Recruiter("joseph", "Bilbao", ["php", "angular"])

    coder_list = [ainara, ainhoa, jeff]
    recruiter_list = [perla, laura, joseph]

    number_of_meetings = 5
    return create_list_of_matches(coder_list, recruiter_list, number_of_meetings)


def test_main_should_create_a_list_of_matches():

    list_of_matches = setup()

    assert len(list_of_matches) == 45


def test_main_should_return_list_of_matches_with_same_locations():

    list_of_matches = setup()

    list_filtered_by_location = filter_by_location(list_of_matches)

    assert len(list_filtered_by_location) == 30


def test_main_should_return_list_of_matches_with_a_matching_skill():

    list_of_matches = setup()

    list_filtered_by_location = filter_by_location(list_of_matches)

    list_filtered_by_skill = filter_by_skill(list_filtered_by_location)

    assert len(list_filtered_by_skill) == 15
