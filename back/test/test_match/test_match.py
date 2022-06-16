from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.domain.match import Match


def test_should_return_coder_and_recruiter():
    ainara = Coder(id=1, name="ainara", locations=["Bilbao"], skills=["python", "vue"])
    perla = Recruiter(
        id=1,
        name="perla",
        company="Companyinc",
        charge="Recruiter",
        locations=["Bilbao"],
        skills=["python", "vue"],
    )

    assert ainara.name == "ainara"
    assert ainara.locations == ["Bilbao"]

    assert perla.name == "perla"
    assert perla.locations == ["Bilbao"]


# def test_should_relate_coder_and_retruiter():
#     ainara = Coder(name="ainara", locations=["Bilbao"], skills=["python", "vue"])
#     perla = Recruiter(
#         name="perla",
#         company="Companyinc",
#         charge="Recruiter",
#         locations=["Bilbao"],
#         skills=["python", "vue"],
#     )
#     match = Match(ainara, perla)

#     assert match.coincidence == 1


# def test_should_not_relate_coder_and_retruiter():
#     ainara = Coder(name="ainara", locations=["Bilbao"], skills=["python", "vue"])
#     perla = Recruiter(
#         name="perla",
#         company="Companyinc",
#         charge="Recruiter",
#         locations=["Bilbao"],
#         skills=["python", "vue"],
#     )
#     match = Match(ainara, perla)

#     assert match.coincidence == 0


# def test_relate_by_number_of_skills():
#     ainara = Coder(name="ainara", locations=["Bilbao"], skills=["python", "vue"])
#     perla = Recruiter(
#         name="perla",
#         company="Companyinc",
#         charge="Recruiter",
#         locations=["Bilbao"],
#         skills=["python", "vue"],
#     )
#     match = Match(ainara, perla, 0)

#     assert match.coincidence == 1


# def test_relate_by_number_of_languages():
#     ainara = Coder(name="ainara", locations=["Bilbao"], skills=["python", "vue"])
#     perla = Recruiter(
#         name="perla",
#         company="Companyinc",
#         charge="Recruiter",
#         locations=["Bilbao"],
#         skills=["python", "vue"],
#     )
#     match = Match(ainara, perla, 0)

#     assert match.coincidence == 1


# def test_relate_by_number_of_languages():
#     ainara = Coder(name="ainara", locations=["Bilbao"], skills=["python", "vue"])
#     perla = Recruiter(
#         name="perla",
#         company="Companyinc",
#         charge="Recruiter",
#         locations=["Bilbao"],
#         skills=["python", "vue"],
#     )
#     match = Match(ainara, perla, 0)

#     assert match.coincidence < 1
