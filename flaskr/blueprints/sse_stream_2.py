"""
SSE Stream 2 blueprint module
"""
from flask import Blueprint, Response
from flaskr.workers import job_runner

SSE_STREAM_2 = Blueprint('sse_stream_2', __name__)


@SSE_STREAM_2.route('/streams/sse_stream_2', methods=['GET'])
def sse_stream():
    """
    function stream
    :return:
    """
    def event_stream():
        """
        function eventStream
        :return:
        """
        while True:
            stream = 'data: {}\n\n'.format(job_runner.fetch_job_states())
            yield stream

    return Response(event_stream(), mimetype="text/event-stream")
