from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
def generate_log():
    app.logger.debug("Test debug log")
    app.logger.warning("Test warning log")
    app.logger.error("Test error log")
    return "<p>Hello World</p>"

if __name__ == "__main__":
    app.run(port=environ.get('PORT', '8181'), debug=False, host='0.0.0.0')
