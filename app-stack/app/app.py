from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)

redis = Redis(host='redis-db', port=6379)

@app.route('/')
def hello():
    try:
        count = redis.incr('hits')
    except Exception as e:
        count = "Error connecting to Redis"
        
    return f"""
    <h1>Automated Container Stack</h1>
    <p><b>Status:</b> Backend is running via Multi-stage Docker!</p>
    <p><b>Visits:</b> {count}</p>
    <p><b>Container ID:</b> {socket.gethostname()}</p>
    <p><b>Target VM IP:</b> 172.30.30.230</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
