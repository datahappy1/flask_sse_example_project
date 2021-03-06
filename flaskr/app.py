"""
app.py
"""
import os
from flask import Flask, render_template, send_from_directory
from waitress import serve
from flaskr.blueprints.sse_stream_1 import SSE_STREAM_1
from flaskr.blueprints.sse_stream_2 import SSE_STREAM_2

APP = Flask(__name__)

APP.register_blueprint(SSE_STREAM_1)
APP.register_blueprint(SSE_STREAM_2)

BLUEPRINTS_REGISTERED = APP.blueprints.keys()
THREADS_COUNT = len(BLUEPRINTS_REGISTERED)

@APP.context_processor
def menu_items():
    """
    context processor for sending menu items
    to the web app menu based on the imported
    blueprints with the SSE streams
    :return:
    """
    blueprints_enum = enumerate(BLUEPRINTS_REGISTERED)
    return dict(menu_items=blueprints_enum)


@APP.route('/favicon.ico')
def favicon():
    """
    function to properly handle favicon
    :return:
    """
    return send_from_directory(os.path.join(APP.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@APP.route('/', methods=['GET'])
def main():
    """
    the main rout rendering index.html
    :return:
    """
    return render_template('index.html')


@APP.route('/<string:stream_name>', methods=['GET'])
def stream(stream_name):
    """
    the stream route rendering stream.html
    :param stream_name:
    :return:
    """
    if stream_name not in BLUEPRINTS_REGISTERED:
        return render_template('error_page.html',
                               template_error_message='stream not found in imported Flask Blueprints')
    else:
        return render_template('stream.html',
                               template_stream_name=stream_name)


if __name__ == "__main__":
    serve(APP, host='0.0.0.0', port=80, threads=THREADS_COUNT)
