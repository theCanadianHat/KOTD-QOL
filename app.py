from datetime import datetime, timezone

from flask import Flask, render_template

from reddit import get_active_bosses

app = Flask(__name__)


@app.template_filter('datetimeformat')
def datetimeformat(value):
    dt = datetime.fromtimestamp(value, tz=timezone.utc)
    return dt.strftime('%Y-%m-%d %H:%M UTC')

def get_version():
    try:
        with open("version.txt") as f:
            lines = [line.strip() for line in f if line.strip()]
            if len(lines) >= 2:
                commit_hash, build_time = lines[0], lines[1]
                return f"{commit_hash[:7]}-{build_time}"
            else:
                raise RuntimeError('Version not found')
    except:
        return "dev"

@app.route('/')
def index():
    data = get_active_bosses()
    version = get_version()
    return render_template('index.html',bosses=data, version=version)

if __name__ == '__main__':
    app.run(debug=True)