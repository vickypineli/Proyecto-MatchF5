from src.main import select_locations, select_skills, select_schedule_from_recruiter

def test_select_skills_should_return_a_list_of_skills():
    example_dict ={
        "NOMBRE": "Ainara ",
        "TELEFONO": 666666661,
        "MAIL": "ainara@gmail.com",
        "PROMOCION": "BIO",
        "BILBAO": "x",
        "S-PYTHON": "x",
        "S-JAVA": "x"
    }
    skills = select_skills(example_dict)
    assert skills == ["PYTHON", "JAVA"]
    
def test_select_skills_should_not_return_unselected_skills():
    example_dict ={
        "NOMBRE": "Ainara ",
        "TELEFONO": 666666661,
        "MAIL": "ainara@gmail.com",
        "PROMOCION": "BIO",
        "BILBAO": "x",
        "S-PYTHON": "",
        "S-JAVA": ""
    }
    skills = select_skills(example_dict)
    assert skills == []

def test_select_location_should_return_a_list_of_selected_locations():
    example_dict ={
        "NOMBRE": "Ainara ",
        "TELEFONO": 666666661,
        "MAIL": "ainara@gmail.com",
        "PROMOCION": "BIO",
        "L-BILBAO": "x",
        "L-BARCELONA": "",
        "S-PYTHON": "x",
        "S-JAVA": "x"
    }
    locations = select_locations(example_dict)
    assert locations == ["BILBAO"]

def test_select_schedule_from_recruiter_should_return_a_dict_of_selected_schedule():
    example_dict = {
        "EMPRESA": "Merkatu",
        "NOMBRE DEL RECRUITER": "Andres",
        "EMAIL": "andres@merkatu.com",
        "CARGO": "Director",
        "U-BILBAO": "x",
        "S-PYTHON": "x",
        "10:10": "x",
        "10:20": "x",
        "13:00": "",
        "13:30": "x"
    }
    
    dict_of_schedule = select_schedule_from_recruiter(example_dict)
    
    assert dict_of_schedule == {"10:10": "x",
                                "10:20": "x",
                                "13:00": "",
                                "13:30": "x"}