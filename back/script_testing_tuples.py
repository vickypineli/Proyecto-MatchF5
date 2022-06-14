from src.main import *

participants_json = {
    "CODERS": [
        {
            "NOMBRE": "Ainara",
            "APELLIDOS": "Perez",
            "TELEFONO": 666666661,
            "MAIL": "ainara@gmail.com",
            "PROMOCION": "BIO",
            "L-REMOTO": "",
            "L-BILBAO": "x",
            "L-ASTRUIAS": "",
            "L-BARCELONA": "",
            "L-SEVILLA": "",
            "S-JAVASCRIPT": "",
            "S-VUE": "",
            "S-JAVA": "",
            "S-PHP": "",
            "S-PYTHON": "x",
        },
        {
            "NOMBRE": "Perla",
            "APELLIDOS": "Martinez",
            "TELEFONO": 666666662,
            "MAIL": "Perla@gmail.com",
            "PROMOCION": "BCN",
            "L-REMOTO": "",
            "L-BILBAO": "x",
            "L-ASTRUIAS": "",
            "L-BARCELONA": "x",
            "L-SEVILLA": "",
            "S-JAVASCRIPT": "",
            "S-VUE": "x",
            "S-JAVA": "",
            "S-PHP": "",
            "S-PYTHON": "x",
        },
        {
            "NOMBRE": "Vicky",
            "APELLIDOS": "Pinero",
            "TELEFONO": 666666663,
            "MAIL": "vicky@gmail.com",
            "PROMOCION": "BIO",
            "L-REMOTO": "",
            "L-BILBAO": "x",
            "L-ASTRUIAS": "",
            "L-BARCELONA": "",
            "L-SEVILLA": "",
            "S-JAVASCRIPT": "",
            "S-VUE": "x",
            "S-JAVA": "",
            "S-PHP": "",
            "S-PYTHON": "x",
        },
    ],
    "RECRUITERS": [
        {
            "EMPRESA": "Merkatu",
            "NOMBRE DEL RECRUITER": "Andres Merkatu",
            "EMAIL": "andres@merkatu.com",
            "LINKEDIN": "https://www.linkedin.com/in/Andres",
            "CARGO": "Director",
            "L-REMOTO": "",
            "L-BILBAO": "x",
            "L-ASTRUIAS": "",
            "L-BARCELONA": "",
            "L-SEVILLA": "",
            "S-JAVASCRIPT": "",
            "S-VUE": "",
            "S-JAVA": "",
            "S-PHP": "",
            "S-PYTHON": "x",
            "S-REACT": "",
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
            "L-REMOTO": "",
            "L-BILBAO": "x",
            "L-ASTRUIAS": "x",
            "L-BARCELONA": "x",
            "L-SEVILLA": "",
            "S-JAVASCRIPT": "",
            "S-VUE": "",
            "S-JAVA": "",
            "S-PHP": "",
            "S-PYTHON": "x",
            "S-REACT": "",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
        },
        {
            "EMPRESA": "Inetum",
            "NOMBRE DEL RECRUITER": "Samantha",
            "EMAIL": "samantha.inetum.es",
            "LINKEDIN": "https://www.linkedin.com/in/inetum",
            "CARGO": "RH",
            "L-REMOTO": "",
            "L-BILBAO": "x",
            "L-ASTRUIAS": "",
            "L-BARCELONA": "",
            "L-SEVILLA": "",
            "S-JAVASCRIPT": "x",
            "S-VUE": "x",
            "S-JAVA": "",
            "S-PHP": "",
            "S-PYTHON": "x",
            "S-REACT": "",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
        },
        # {
        #     "EMPRESA": "Efilm",
        #     "NOMBRE DEL RECRUITER": "Maria",
        #     "EMAIL": "maria.eflim.es",
        #     "LINKEDIN": "https://www.linkedin.com/in/Maria",
        #     "CARGO": "Recruiter",
        #     "L-REMOTO": "",
        #     "L-BILBAO": "x",
        #     "L-ASTRUIAS": "",
        #     "L-BARCELONA": "x",
        #     "L-SEVILLA": "",
        #     "S-JAVASCRIPT": "",
        #     "S-VUE": "x",
        #     "S-JAVA": "",
        #     "S-PHP": "",
        #     "S-PYTHON": "x",
        #     "S-REACT": "",
        #     "10:10": "x",
        #     "10:20": "x",
        #     "10:30": "x",
        # },
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

tuples = transform_matches_to_tuples(filtered_matches)

slots = number_of_meetings * len(recruiters)

combs = create_list_of_combinations(tuples, slots)

filtered_combs = filter_tuples(combs)

# counter = sum(1 for i in final_filter)
solution = select_solution(filtered_combs)

solution_with_objs = transform_tuples_to_matches(solution, filtered_matches)

dict_of_solution = solution_to_dict(solution_with_objs, locations, skills)

print(dict_of_solution)
# print(counter)
