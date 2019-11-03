import time
from flask import Flask, render_template, Response
from waitress import serve

app = Flask(__name__)

def get_message(id):
    '''this could be any function that blocks until data is ready'''

    time.sleep(float(id))

    s = time.ctime(time.time())
    return s


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/stream/<int:id>', methods = ['GET'])
def stream(id):
    def eventStream():
        print(id)
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}-{}\n\n'.format(id,get_message(id))
    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=80)
    serve(app, host='0.0.0.0', port=80)
