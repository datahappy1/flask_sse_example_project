# Flask, SSE, JS example project
Flask, Waitress and Javascript used for 1-N Server-sent event streams to enable long running jobs state auto-refresh visualized in a HTML table in the browser

*Currently designed to run on Windows, but if you replace Waitress WSGI with Gunicorn for instance, can
run also on *nix based OS

## 10000 ft. overview Diagram
![alt text][diagram]

[diagram]: https://github.com/datahappy1/flask_sse_example_project/blob/master/flaskr/docs/diagram.png "diagram"

## Screenshots from the web app
![alt text][screens]

[screens]: https://github.com/datahappy1/flask_sse_example_project/blob/master/flaskr/docs/screens.gif "screens"


## How it works
1) Flask backend before each app startup imports blueprints with the SSE streaming routes from the folder `/blueprints/`
2) These routes publish the events into `http://127.0.0.1:80/streams/<stream_name>`
3) Flask generates the HTML templates, template `stream.html` has JavaScript code attached, which uses
JSON2HTML JS library to change the event stream from JSON to HTML table rows and injects these rows in the 
table used for jobs statuses visualization
4) You can create a new stream by importing into `__main__.py` a new blueprint


## How to get started
1) Git clone this repository
2) Create and activate yourself a Python virtual environment
3) run `pip3 install -r requirements.txt`
4) set your Windows Python working directory to `C:\<<<folder where you cloned this repo to>>>\flaskr`
5) run `python3 C:\<<<folder where you cloned this repo to>>>\flaskr\__main__.py`

### Useful links:
- https://stackoverflow.com/questions/30645664/how-to-stop-server-sent-events 
- https://medium.com/brillio-data-science/exposing-your-data-science-project-to-the-world-flask-with-a-waitress-8592f0356b27
- https://stackoverflow.com/questions/12232304/how-to-implement-server-push-in-flask-framework
- https://medium.com/code-zen/python-generator-and-html-server-sent-events-3cdf14140e56
- https://json2html.com/examples/
