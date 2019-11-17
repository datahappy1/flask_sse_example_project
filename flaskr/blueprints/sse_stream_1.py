"""
SSE Stream 1 blueprint module
"""
from flask import Blueprint, Response
from flaskr.workers import job_runner

SSE_STREAM_1 = Blueprint('sse_stream_1', __name__)


@SSE_STREAM_1.route('/streams/sse_stream_1', methods=['GET'])
def stream():
    """
    function stream
    :return:
    """
    def eventStream():
        """
        function eventStream
        :return:
        """
        while True:
            stream = 'data: {}\n\n'.format(job_runner.fetch_job_states())
            yield stream

    return Response(eventStream(), mimetype="text/event-stream")
