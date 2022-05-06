from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.domain.match import Match


def test_should_return_coder_and_recruiter():
    ainara = Coder("ainara", "Bilbao")
    perla = Recruiter("perla","Bilbao")

    assert ainara.name == "ainara"
    assert ainara.location == "Bilbao"

    assert perla.name == "perla"
    assert perla.location == "Bilbao"


def test_should_relate_coder_and_retruiter():
    ainara = Coder("ainara", "Bilbao")
    perla = Recruiter("perla","Bilbao")
    match = Match (ainara, perla)


    assert match.coincidence == 1

def test_should_not_relate_coder_and_retruiter():
    ainara = Coder("ainara", "Bilbao")
    perla = Recruiter("perla","Barcelona")
    match = Match (ainara, perla)


    assert match.coincidence == 0

def test_relate_by_number_of_skills():
    ainara = Coder("ainara", ["Bilbao"],["python","vue"])
    perla = Recruiter("perla", ["Bilbao"],["python","vue"])
    match = Match (ainara, perla)


    assert match.coincidence == 1

def test_relate_by_number_of_languages():
    ainara = Coder("ainara",  ["Bilbao"],["python","vue"], ["ingles"])
    perla = Recruiter("perla", ["Bilbao"],["python","vue"], ["ingles"])
    match = Match (ainara, perla)


    assert match.coincidence == 1

  
def test_relate_by_number_of_languages():
    ainara = Coder("ainara", ["Bilbao"], ["python"], ["ingles"])
    perla = Recruiter("perla", ["Bilbao"], ["python","vue"], ["ingles"])
    match = Match (ainara, perla)


    assert match.coincidence < 1
