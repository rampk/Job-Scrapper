from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/test', methods=['POST', 'GET'])
def test():
    subprocess.Popen(['unix_crawler.sh'], cwd="../", shell=True)
    return "Function started"


if __name__ == "__main__":
    app.run(debug=True)
