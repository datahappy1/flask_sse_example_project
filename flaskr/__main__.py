from flask import Flask, render_template, Response, session, url_for, redirect, request
from waitress import serve
from flaskr.lib import job_runner

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/streams/', methods = ['GET'])
def stream():
    def eventStream():
        while True:
            stream = 'data: {}\n\n'.format(job_runner.fetch_step_states())
            yield stream

    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80)
