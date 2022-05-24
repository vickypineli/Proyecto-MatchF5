from src.main import convert_to_recruiter

def test_convert_to_recruiter_should_transform_a_dict_into_a_recruiter():
    recruiter_dict = {
        "EMPRESA": "Merkatu",
        "NOMBRE DEL RECRUITER": "Andres",
        "EMAIL": "andres@merkatu.com",
        "CARGO": "Director",
        "L-BILBAO": "x",
        "S-PYTHON": "x",
        "10:10": "x",
        "10:20": "x",
        "13:00": "x",
        "13:30": "x"
    }
        
    recruiter = convert_to_recruiter(recruiter_dict)
    
    assert recruiter.name == "Andres"
    assert recruiter.company == "Merkatu"
    assert recruiter.locations == ["BILBAO"]
    assert recruiter.skills == ["PYTHON"]
    
