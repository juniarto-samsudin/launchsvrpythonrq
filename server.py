import argparse
from flask import Flask

# Create Flask app
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, required=True, help="Host IP address")
    parser.add_argument("--port", type=int, required=True, help="Port number")
    args = parser.parse_args()
    
    # Run the Flask app with specified host and port
    app.run(host=args.host, port=args.port)
