from src.main import count_number_of_slots, create_list_of_recruiters

def test_count_number_of_slots_should_return_the_number_of_slots():
    recruiter_list = [
        {
            "EMPRESA": "Merkatu",
            "NOMBRE DEL RECRUITER": "Andres",
            "EMAIL": "andres@merkatu.com",
            "CARGO": "Director",
            "L-BILBAO": "x",
            "S-PYTHON": "x",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
            "13:00": "x",
            "13:30": "x"
        },
        {
            "EMPRESA": "Ibermatica",
            "NOMBRE DEL RECRUITER": "Laura",
            "EMAIL": "laura.ibermatica.es",
            "CARGO": "RH",
            "L-BILBAO": "x",
            "L-BARCELONA": "x",
            "S-JAVA": "x",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
            "13:00": "x",
            "13:30": "x"
        }
    ]
    
    recruiter_obj_list = create_list_of_recruiters(recruiter_list)
    slots = count_number_of_slots(recruiter_obj_list)
    
    assert slots == 5
    