import subprocess
from datetime import datetime

from flask import Flask, render_template, jsonify
from reddit import get_active_bosses

app = Flask(__name__)


@app.template_filter('datetimeformat')
def datetimeformat(value):
    dt = datetime.utcfromtimestamp(value)
    return dt.strftime('%Y-%m-%d %H:%M UTC')

def get_git_version():
    try:
        version = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
        return version.decode("utf-8").strip()
    except:
        return "dev"

@app.route('/')
def index():
    data = get_active_bosses()
    version = get_git_version()
    return render_template('index.html',bosses=data, version=version)

@app.route('/api/bosses')
def bosses():
    data = get_active_bosses()
    return render_template('index.html',bosses=data)

if __name__ == '__main__':
    app.run(debug=True)