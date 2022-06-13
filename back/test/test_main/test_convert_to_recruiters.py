from src.main import convert_to_recruiter, create_list_of_recruiters


def test_convert_to_recruiter_should_transform_a_dict_into_a_recruiter():
    recruiter_dict = {
        "EMPRESA": "Merkatu",
        "NOMBRE DEL RECRUITER": "Andres",
        "EMAIL": "andres@merkatu.com",
        "LINKEDIN": "https://www.linkedin.com/in/Andres",
        "CARGO": "Director",
        "L-BILBAO": "x",
        "S-PYTHON": "x",
        "10:10": "x",
        "10:20": "x",
        "13:00": "x",
        "13:30": "x",
    }
    index = 0
    recruiter = convert_to_recruiter(recruiter_dict, index)

    assert recruiter.name == "Andres"
    assert recruiter.company == "Merkatu"
    assert recruiter.locations == ["BILBAO"]
    assert recruiter.skills == ["PYTHON"]


def test_create_list_of_recruiters_should_return_a_list_of_recruiters_obj():
    recruiter_list = [
        {
            "EMPRESA": "Merkatu",
            "NOMBRE DEL RECRUITER": "Andres",
            "EMAIL": "andres@merkatu.com",
            "LINKEDIN": "https://www.linkedin.com/in/Andres",
            "CARGO": "Director",
            "L-BILBAO": "x",
            "S-PYTHON": "x",
            "10:10": "x",
            "10:20": "x",
            "13:00": "x",
            "13:30": "x",
        },
        {
            "EMPRESA": "Ibermatica",
            "NOMBRE DEL RECRUITER": "Laura",
            "EMAIL": "laura.ibermatica.es",
            "LINKEDIN": "https://www.linkedin.com/in/Andres",
            "CARGO": "RH",
            "L-BILBAO": "x",
            "L-BARCELONA": "x",
            "S-JAVA": "x",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
            "13:00": "x",
            "13:30": "x",
        },
    ]

    recruiter_obj_list = create_list_of_recruiters(recruiter_list)

    assert recruiter_obj_list[0].name == "Andres"
    assert recruiter_obj_list[1].name == "Laura"
    assert recruiter_obj_list[0].skills == ["PYTHON"]
    assert recruiter_obj_list[1].skills == ["JAVA"]


def test_create_list_of_recruiters_should_add_id():
    recruiter_list = [
        {
            "EMPRESA": "Merkatu",
            "NOMBRE DEL RECRUITER": "Andres",
            "EMAIL": "andres@merkatu.com",
            "LINKEDIN": "https://www.linkedin.com/in/Andres",
            "CARGO": "Director",
            "L-BILBAO": "x",
            "S-PYTHON": "x",
            "10:10": "x",
            "10:20": "x",
            "13:00": "x",
            "13:30": "x",
        },
        {
            "EMPRESA": "Ibermatica",
            "NOMBRE DEL RECRUITER": "Laura",
            "EMAIL": "laura.ibermatica.es",
            "LINKEDIN": "https://www.linkedin.com/in/Andres",
            "CARGO": "RH",
            "L-BILBAO": "x",
            "L-BARCELONA": "x",
            "S-JAVA": "x",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
            "13:00": "x",
            "13:30": "x",
        },
    ]

    recruiter_obj_list = create_list_of_recruiters(recruiter_list)

    assert recruiter_obj_list[0].id == 1
    assert recruiter_obj_list[1].id == 2
