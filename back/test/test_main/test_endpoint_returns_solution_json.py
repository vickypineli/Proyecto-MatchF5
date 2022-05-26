from src.webserver import create_app


def setup():

    app = create_app({})
    client = app.test_client()

    return client


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
            "L-BARCELONA": "x",
            "L-ASTURIAS": "x",
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
            "L-BARCELONA": "x",
            "L-ASTURIAS": "x",
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
            "L-BARCELONA": "x",
            "L-ASTURIAS": "x",
            "S-JAVA": "x",
            "S-PHP": "x",
            "S-PYTHON": "x",
            "10:10": "x",
            "10:20": "x",
            "10:30": "x",
        },
    ],
}


def test_prematch_endpoint_should_return_a_correct_json_of_a_selected_solution():

    client = setup()

    response = client.post("/api/prematch", json=participants_json)

    print(response.json)

    assert response.json == [
        {
            "EMPRESA": "Devoteam Drago",
            "NOMBRE Y APELLIDOS": "IGNACIO MERINO ALVAREZ",
            "EMAIL": "-",
            "CARGO": "DIRECTOR ZONA NORTE",
            "LINKEDIN": "https://www.linkedin.com/in/ignacio-merino/",
            "BCN": "x",
            "AST": "",
            "BIO": "x",
            "PHP": "x",
            "JAVA": "x",
            "PYTHON": "x",
            "10:10": "BIO Perla",
            "10:20": "BIO David Ordiales",
            "10:30": "BIO Ainara",
        }
    ]
