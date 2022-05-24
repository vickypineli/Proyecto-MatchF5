from src.main import convert_to_coder, create_list_of_coders

def test_convert_to_coder_should_transform_a_dict_into_a_coder():
    coder_dict = {
        "NOMBRE": "Ainara",
        "TELEFONO": 666666661,
        "MAIL": "ainara@gmail.com",
        "PROMOCION": "BIO",
        "L-BILBAO": "x",
        "S-PYTHON": "x"
    }    
    coder = convert_to_coder(coder_dict)
    
    assert coder.name == "Ainara"
    assert coder.prom == "BIO"
    assert coder.locations == ["BILBAO"]
    assert coder.skills == ["PYTHON"]
    
def test_create_list_of_coders_should_return_list_of_coder_objects():
    list_of_coders_dict = [
        {
            "NOMBRE": "Ainara",
            "TELEFONO": 666666661,
            "MAIL": "ainara@gmail.com",
            "PROMOCION": "BIO",
            "L-BILBAO": "x",
            "S-PYTHON": "x"
        },
        {
            "NOMBRE": "Perla",
            "TELEFONO": 666666662,
            "MAIL": "Perla@gmail.com",
            "PROMOCION": "BIO",
            "L-BILBAO": "x",
            "L-BARCELONA": "x",
            "S-JAVASCRIPT": "x",
            "S-PYTHON": "x"
        }
    ]
    
    list_of_coder_objs = create_list_of_coders(list_of_coders_dict)
    
    assert list_of_coder_objs[0].name == "Ainara"
    assert list_of_coder_objs[1].name == "Perla"
    assert list_of_coder_objs[0].skills == ["PYTHON"]
    assert list_of_coder_objs[1].skills == ["JAVASCRIPT" , "PYTHON"]
    

# def test_convert_to_coder_should_transform_json_coders_into_a_list_of_coders():
    
#     assert list_of_coders == [ainara, perla]