from flask import Flask
from jinja2.environment import TemplateStream

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p><b>Hello, darlings!</b></p>"

if  __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)