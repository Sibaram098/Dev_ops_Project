from flask import Flask
from prometheus_client import generate_latest, Counter, Histogram
import time

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total app requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency', ['endpoint'])

@app.route('/')
def hello():
    start_time = time.time()
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    response = "Microservice Pipeline Operational!"
    REQUEST_LATENCY.labels(endpoint='/').observe(time.time() - start_time)
    return response

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
