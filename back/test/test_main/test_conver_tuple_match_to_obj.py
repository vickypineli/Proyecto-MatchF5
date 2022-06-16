from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.domain.match import Match
from src.main import transform_tuples_to_matches


def test_transform_tuples_to_matches_should_return_a_match_object_from_a_tuple():
    ainara = Coder(id=0, name="ainara")
    perla = Recruiter(0, "perla", "Ibermatica", "perla@gmail.com", "Directora")

    match = Match(ainara, perla, 0)

    match_tuple = match.to_tuple()

    solution = transform_tuples_to_matches([match_tuple], [match])

    assert solution[0] == match


def test_transform_tuples_to_matches_should_return_a_list_of_match_objects_from_a_list_of_tuples():
    ainara = Coder(id=0, name="ainara")
    perla = Recruiter(0, "perla", "Ibermatica", "perla@gmail.com", "Directora")
    laura = Recruiter(1, "laura", "Kerkaru", "laura@gmail.com", "Directora")

    match1 = Match(ainara, perla, 0)
    match2 = Match(ainara, laura, 1)

    list_of_matches = [match1, match2]

    first_match_tuple = match1.to_tuple()
    second_match_tuple = match1.to_tuple()

    tuple_list = [first_match_tuple, second_match_tuple]

    solution = transform_tuples_to_matches(tuple_list, list_of_matches)

    assert solution[0] in list_of_matches
    assert solution[1] in list_of_matches
