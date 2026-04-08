from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 350px; text-align: center; }
        h1 { color: #1a73e8; margin-bottom: 1rem; font-size: 24px; }
        input { width: 100%; padding: 12px; margin: 15px 0; border: 1px solid #ddd; border-radius: 8px; box-sizing: border-box; }
        button { background: #1a73e8; color: white; border: none; padding: 12px 25px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; transition: 0.3s; }
        button:hover { background: #1557b0; }
    </style>
    <div class="card">
        <h1>Secure Pay v1</h1>
        <p style="color: #666;">Enter the amount to begin</p>
        <input type="number" placeholder="Amount ($)">
        <button>Proceed to Pay</button>
    </div>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)