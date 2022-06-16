from src.main import (
    create_list_of_recruiters,
    create_list_of_coders,
    count_number_of_slots,
    create_list_of_matches,
    final_result,
    select_solution,
    get_all_locations,
    get_all_skills,
    solution_to_dict,
    principal_filter,
    transform_tuples_to_matches,
)

participants_json = {
    "CODERS": [
        {
            "NOMBRE": "Ainara",
            "APELLIDOS": "Perez",
            "TELEFONO": 666666661,
            "MAIL": "ainara@gmail.com",
            "PROMOCION": "BIO",
            "L-BILBAO": "x",
            "L-BARCELONA": "x",
            "S-JAVASCRIPT": "x",
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
    ],
    "RECRUITERS": [
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
            "S-JAVA": "",
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
            "S-JAVA": "x",
            "S-PHP": "",
            "S-PYTHON": "x",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
        },
    ],
}

coders_list = participants_json["CODERS"]
recruiters_list = participants_json["RECRUITERS"]

coders = create_list_of_coders(coders_list)
recruiters = create_list_of_recruiters(recruiters_list)

number_of_meetings = count_number_of_slots(recruiters)
locations = get_all_locations(recruiters_list[0])
skills = get_all_skills(recruiters_list[0])
matches = create_list_of_matches(coders, recruiters, number_of_meetings)

filtered_matches = principal_filter(matches)

slots = number_of_meetings * len(recruiters)
solutions = final_result(filtered_matches, slots)

selected_solution = select_solution(solutions)
solution_matches = transform_tuples_to_matches(selected_solution, matches)
dict_of_solution = solution_to_dict(solution_matches, locations, skills)

print(dict_of_solution)
