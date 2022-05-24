from lib2to3.pytree import convert
from flask import Flask, request
from flask_cors import CORS
from main import final_result

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
    
    @app.route("/api/prematch", methods=["POST"] )
    def post_coders():
        body = request.json
        coders_list = body["coders"]
        recruiters_list = body["recruiters"]
        coders = convert_to_coder(coders_list)
        recruiters = convert_to_recruiters(recruiters_list)
        number_of_meetings = calculate_number_of_meetings(recruiters[0])
        matches = create_list_of_matches(coders, recruiters, number_of_meetings)
        slots = number_of_meetings * len(recruiters)
        list_result = final_result(matches, slots )
        
        
        return list_result
    

    return app
