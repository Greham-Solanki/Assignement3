from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Solanki ECS Container."

@app.route('/health')  # Add a specific health check endpoint
def health():
    return "Healthy", 200
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
