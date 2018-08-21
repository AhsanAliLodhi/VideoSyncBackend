from flask import Blueprint, jsonify, request
from flasgger import swag_from
import copy
from app.db import messages
from app.api_key import api_key_exists

messages_bp = Blueprint('messages_bp', __name__)


@messages_bp.route('/messages', methods=['POST'])
@swag_from('swagger_yml/post_messages.yml')
def post_messages():
    """
        Post message here..
        returns the message passed if authorized!
    """
    # check api_key header
    current_api_key = request.headers.get('api_key')

    if current_api_key is None \
            or not api_key_exists(current_api_key):
        return jsonify({'message': 'Unauthorized access'}), 401

    # check if user_input is of the correct format
    # TODO

    # all good, put message into db
    try:
        payload = request.json
        message = payload.get('message')
        context = payload.get('context')

        # reply is container in res
        res = {"message":"helloWorld"}

        messages.insert({'message': res})

        return jsonify({'message': res}), 200

    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong'}), 500
