from src.main import *


def test_select_solution_should_return_first_solution_from_the_list_of_solutions():
    first_solution = [
        {
            "EMPRESA": "Merkatu",
            "NOMBRE Y APELLIDOS": "Andres",
            "EMAIL": "andres@merkatu.com",
            "CARGO": "Director",
            "LINKEDIN": "https://www.linkedin.com/in/Andres",
            "BILBAO": "x",
            "JAVA": "x",
            "PHP": "x",
            "PYTHON": "x",
            "10:10": "BIO Ainara Perez",
            "10:20": "BIO Perla Garcia",
            "10:30": "BIO David Ordiales",
        },
        {
            "EMPRESA": "Ibermatica",
            "NOMBRE Y APELLIDOS": "Laura",
            "EMAIL": "laura.ibermatica.es",
            "CARGO": "RH",
            "LINKEDIN": "https://www.linkedin.com/in/Laura",
            "BILBAO": "x",
            "JAVA": "x",
            "PHP": "x",
            "PYTHON": "x",
            "10:10": "BIO Perla Garcia",
            "10:20": "BIO Ainara Perez",
            "10:30": "-",
        },
        {
            "EMPRESA": "Efilm",
            "NOMBRE Y APELLIDOS": "Maria",
            "EMAIL": "maria.eflim.es",
            "CARGO": "Recruiter",
            "LINKEDIN": "https://www.linkedin.com/in/Maria",
            "BILBAO": "x",
            "JAVA": "x",
            "PHP": "x",
            "PYTHON": "x",
            "10:10": "BIO David Ordiales",
            "10:20": "-",
            "10:30": "BIO Ainara Perez",
        },
    ]
    second_solution = [
        {
            "EMPRESA": "Hodeia",
            "NOMBRE Y APELLIDOS": "Lander Goikoetxea",
            "EMAIL": "lander@hodeia.com",
            "CARGO": "Director",
            "LINKEDIN": "https://www.linkedin.com/in/Lander",
            "BILBAO": "x",
            "JAVA": "x",
            "PHP": "x",
            "PYTHON": "x",
            "10:10": "BIO Ainara Perez",
            "10:20": "BIO Perla Garcia",
            "10:30": "BIO David Ordiales",
        },
        {
            "EMPRESA": "Ibermatica",
            "NOMBRE Y APELLIDOS": "Laura",
            "EMAIL": "laura.ibermatica.es",
            "CARGO": "RH",
            "LINKEDIN": "https://www.linkedin.com/in/Laura",
            "BILBAO": "x",
            "JAVA": "x",
            "PHP": "x",
            "PYTHON": "x",
            "10:10": "BIO Ainara Perez",
            "10:20": "BIO Perla Garcia",
            "10:30": "BIO David Ordiales",
        },
        {
            "EMPRESA": "Efilm",
            "NOMBRE Y APELLIDOS": "Maria",
            "EMAIL": "maria.eflim.es",
            "CARGO": "Recruiter",
            "LINKEDIN": "https://www.linkedin.com/in/Maria",
            "BILBAO": "x",
            "JAVA": "x",
            "PHP": "x",
            "PYTHON": "x",
            "10:10": "BIO David Ordiales",
            "10:20": "-",
            "10:30": "BIO Ainara Perez",
        },
    ]

    list_of_solutions = [first_solution, second_solution]

    selected_solution = select_solution(list_of_solutions)

    assert selected_solution == first_solution
