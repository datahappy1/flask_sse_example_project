from flaskr.workers import job_runner
from flask import Blueprint, Response

SSE_STREAM_2 = Blueprint('sse_stream_2', __name__)


@SSE_STREAM_2.route('/streams/sse_stream_2', methods = ['GET'])
def stream():
    def eventStream():
        while True:
            stream = 'data: {}\n\n'.format(job_runner.fetch_job_states())
            yield stream

    return Response(eventStream(), mimetype="text/event-stream")