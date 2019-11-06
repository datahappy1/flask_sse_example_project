from flask import Flask, render_template, Response, session, url_for, redirect, request
from waitress import serve
from flaskr.config import settings
from flaskr.lib import aws, global_variables

app = Flask(__name__)

app.secret_key = 'loginner'

users = {
    'admin' : 'secret',
    'foo'   : 'myfoo',
}


@app.route('/login')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password and username in users and users[username] == password:
        session['logged_in'] = True
        return redirect(url_for('account'))

    return render_template('login.html')

@app.route("/account")
def account():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('account.html')

@app.route('/logout')
def logout():
    if not session.get('logged_in'):
        return "Not logged in"
    else:
        session['logged_in'] = False
    return render_template('logout.html')

@app.route('/')
def main():
    return render_template('index.html', emr_job_id = settings.EMR_JOB_ID)


@app.route('/streams/', methods = ['GET'])
#def stream(id):
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            #yield 'data: {}-{}\n\n'.format(id,aws.get_message(id))
            stream = 'data: {}\n\n'.format(aws.fetch_step_states(job_id=1))
            yield stream

    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == "__main__":
    global_variables.EMR_INIT_OBJ = aws.EMR(job_id=settings.EMR_JOB_ID)
    serve(app, host='0.0.0.0', port=80)
