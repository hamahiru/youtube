from callwiki import getwiki
from youtube import download_url
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def wiki():
    soup = getwiki()
    return soup


@app.route("/youtube")
def youtube():

    return render_template('youtube.html')

@app.route("/download", methods=["POST"])
def download():
    if request.method == "POST":
        url = request.json['helbidea']
        download_url(url)
        return "Jetsi da"
    else:
        return "Ez dabil"

if __name__ == "__main__":
    app.debug = True
    app.run()
