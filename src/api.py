import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Speech Analysis API</h1>
    <ol>
    <li><b>Do you suffer from any health diseaes?</b></li>
    Answer: (Audio file)
    <br><br>
    <li><b>What is your annual income?</b></li>
    Answer: (Audio file)
    <br><br>
    <li><b>What is your DOB?</b></li>
    Answer: (Audio file)
    <br><br>
    </ol>'''

app.run()