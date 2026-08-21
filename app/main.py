cat << 'EOF' > app/main.py
from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNT = Counter('app_requests_total', 'Total app requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return "Hello, DevOps Pipeline is Working!"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
EOF
