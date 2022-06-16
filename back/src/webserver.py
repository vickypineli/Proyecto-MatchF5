from lib2to3.pytree import convert
from flask import Flask, request, jsonify
from flask_cors import CORS
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

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/prematch", methods=["POST"])
    def post_coders():
        body = request.json
        coders_list = body["CODERS"]
        recruiters_list = body["RECRUITERS"]
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
        matches_solution = transform_tuples_to_matches(selected_solution, matches)
        dict_of_solution = solution_to_dict(matches_solution, locations, skills)

        return jsonify(dict_of_solution), 200

    return app
