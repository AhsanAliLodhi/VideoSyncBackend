from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
import os
from flask_cors import CORS
from .api.messages import messages_bp

audi_app = Flask(__name__)

# add CORS
CORS(audi_app, origins=['http://localhost:3000'])

# swagger config
audi_app.config['SWAGGER'] = {
    'title': 'VideoSync API',
    'uiversion': 3
}
template = {
  "swagger": "2.0",
  "info": {
    "title": "VideoSync API",
    "description": "This is the VideoSync API. You need an api key \
    to call the API. To generate an api key, run `python3 api_key.py` \
    in the root directory of the app",
    "contact": {
      "responsibleOrganization": "AhsanAliLodhi",
    },
    "version": "0.1"
  },
}

Swagger(audi_app, template=template)

# blueprints
#audi_app.register_blueprint(messages_bp, url_prefix='/api')


@audi_app.route("/")
@swag_from('swagger_yml/hello.yml')
def hello():
    """
      Easy way to check if API is online
    """
    return jsonify({'message': 'VideoSync API!'})
