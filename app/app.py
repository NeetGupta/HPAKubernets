from flask import Flask
import time
import math

app = Flask(__name__)

@app.route('/')
def home():
    return "E-commerce Product API is running!"

@app.route('/load')
def cpu_load():
    start = time.time()
    while time.time() - start < 10:
        math.sqrt(12345) ** 5
    return "CPU load generated!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
