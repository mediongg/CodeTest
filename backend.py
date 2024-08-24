
from flask import Flask, request, render_template
from log_reader import LogReader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log')
def get_log():

    fname = request.args.get('filename', '')
    entries = request.args.get('entries', 5)
    fter = request.args.get('filter', '')

    try:
        entries = int(entries)

        if entries <= 0 or fname == '' or fname.find('..') >= 0:
            return 'Bad request. Query param filename: {}, entries: {}'.format(fname, entries), 400
    except ValueError:
        return 'Bad request. Query param entries cannot be converted to integer: {}'.format(entries), 400
    except:
        return 'Unknown error', 400

    reader = LogReader(fname)

    try:
        content = reader.read_log(entries, fter)
    except Exception as e:
        return 'read file failed', 400

    return content
