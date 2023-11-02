import os

from flask import Flask, request, jsonify, make_response
from app.ai import get_corrected_text
from langdetect import detect


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/correct_your_text', methods=["GET"])
    def index():
        text = request.args.get('text')
        print(text)
        if text == "":
            return make_response(jsonify({'corrected_text': "INPUT TEXT"}), 404)
        if text == "\"\"":
            return make_response(jsonify({'corrected_text': "INPUT TEXT"}), 404)
        if text is None:
            return make_response(jsonify({'corrected_text': "INPUT TEXT"}), 404)
        else:
            if detect(text) == 'en':
                corrected_text = get_corrected_text("Fix grammatical errors in this sentence: " + text)
                return make_response(jsonify({'corrected_text': corrected_text}), 200)
            else:
                return make_response(jsonify({'corrected_text': 'INPUT_ENGLISH_TEXT'}), 404)
    return app