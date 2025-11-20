import subprocess
from datetime import datetime

from flask import Flask, render_template, jsonify
from reddit import get_active_bosses

app = Flask(__name__)


@app.template_filter('datetimeformat')
def datetimeformat(value):
    dt = datetime.utcfromtimestamp(value)
    return dt.strftime('%Y-%m-%d %H:%M UTC')

def get_version():
    try:
        with open("version.txt") as f:
            lines = [line.strip() for line in f if line.strip()]
            if len(lines) >= 3:
                tag, hash, buildTime = lines[0], lines[1], lines[2]
                return f"{tag}.{hash[:7]}-{buildTime}"
            else:
                raise RuntimeError('Version not found')
    except:
        return "dev"

    with open("version.txt") as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) >= 2:
        tag, commit = lines[0], lines[1]
        return f"{tag} ({commit[:7]})"
    return "unknown"


@app.route('/')
def index():
    data = get_active_bosses()
    version = get_version()
    return render_template('index.html',bosses=data, version=version)

# @app.route('/api/bosses')
# def bosses():
#     data = get_active_bosses()
#     return render_template('index.html',bosses=data)

if __name__ == '__main__':
    app.run(debug=True)