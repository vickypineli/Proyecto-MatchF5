from src.main import *


def test_select_solution_should_return_one_solution_from_the_list_of_solutions():
    json_coders = [
        {
            "NOMBRE": "Ainara",
            "APELLIDOS": "Perez",
            "TELEFONO": 666666661,
            "MAIL": "ainara@gmail.com",
            "PROMOCION": "BIO",
            "L-BILBAO": "",
            "L-BARCELONA": "x",
            "S-JAVASCRIPT": "",
            "S-PYTHON": "x",
        },
        {
            "NOMBRE": "Perla",
            "APELLIDOS": "Garcia",
            "TELEFONO": 666666662,
            "MAIL": "Perla@gmail.com",
            "PROMOCION": "BIO",
            "L-BILBAO": "x",
            "L-BARCELONA": "x",
            "S-JAVASCRIPT": "x",
            "S-PYTHON": "x",
            "S-PHP": "x",
        },
        {
            "NOMBRE": "David",
            "APELLIDOS": "Ordiales",
            "TELEFONO": 666666663,
            "MAIL": "David@gmail.com",
            "PROMOCION": "BIO",
            "L-BILBAO": "x",
            "L-BARCELONA": "x",
            "S-JAVASCRIPT": "x",
            "S-PYTHON": "x",
        },
    ]

    json_recruiters = [
        {
            "EMPRESA": "Merkatu",
            "NOMBRE DEL RECRUITER": "Andres",
            "EMAIL": "andres@merkatu.com",
            "LINKEDIN": "https://www.linkedin.com/in/Andres",
            "CARGO": "Director",
            "L-BILBAO": "x",
            "L-BARCELONA": "",
            "L-ASTURIAS": "",
            "S-JAVA": "x",
            "S-PHP": "x",
            "S-PYTHON": "x",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
        },
        {
            "EMPRESA": "Ibermatica",
            "NOMBRE DEL RECRUITER": "Laura",
            "EMAIL": "laura.ibermatica.es",
            "LINKEDIN": "https://www.linkedin.com/in/Laura",
            "CARGO": "RH",
            "L-BILBAO": "x",
            "L-BARCELONA": "",
            "L-ASTURIAS": "",
            "S-JAVA": "x",
            "S-PHP": "x",
            "S-PYTHON": "x",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
        },
        {
            "EMPRESA": "Efilm",
            "NOMBRE DEL RECRUITER": "Maria",
            "EMAIL": "maria.eflim.es",
            "LINKEDIN": "https://www.linkedin.com/in/Maria",
            "CARGO": "Recruiter",
            "L-BILBAO": "x",
            "L-BARCELONA": "",
            "L-ASTURIAS": "",
            "S-JAVA": "",
            "S-PHP": "x",
            "S-PYTHON": "",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
        },
    ]

    coder_list = create_list_of_coders(json_coders)
    recruiter_list = create_list_of_recruiters(json_recruiters)
    number_of_meetings = count_number_of_slots(recruiter_list)

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )

    filtered_matches = principal_filter(list_of_matches)

    slots = len(recruiter_list) * number_of_meetings

    list_of_combinations = create_list_of_combinations(filtered_matches, slots)

    pre_filtered_list = filter_invalid_combinations(list_of_combinations)

    filtered_list = filter_repeated_meetings(pre_filtered_list)

    selected_solution = select_solution(filtered_list)

    assert selected_solution is not None
