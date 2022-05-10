from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import create_list_of_matches


def test_main_should_create_a_list_of_matches():
    ainara = Coder("ainara", "Bilbao")
    ainhoa = Coder("ainhoa", "Bilbao")
    jeff = Coder("jeff", "Bilbao")

    perla = Recruiter("perla", "Bilbao")
    laura = Recruiter("laura", "Bilbao")

    coder_list = [ainara, ainhoa, jeff]
    recruiter_list = [perla, laura]

    number_of_meetings = 5

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )

    len(list_of_matches) == 30
