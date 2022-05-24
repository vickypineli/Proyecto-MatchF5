from src.main import select_locations, select_skills

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