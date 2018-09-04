from flask import Flask, request
# set the project root directory as the static folder, you can set others.
vs_app = Flask(__name__, static_url_path='')

@vs_app.route('/')
def root():
    return vs_app.send_static_file('index.html')