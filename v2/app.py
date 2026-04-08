from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #eef2f3; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 2rem; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); width: 350px; border-top: 5px solid #ff9800; }
        h1 { color: #333; text-align: center; }
        .secure-badge { background: #fff3e0; color: #e65100; padding: 5px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 10px; }
        button { background: #ff9800; color: white; border: none; padding: 15px; border-radius: 10px; cursor: pointer; width: 100%; font-size: 16px; font-weight: 600; box-shadow: 0 4px 14px 0 rgba(255,152,0,0.39); }
    </style>
    <div class="card">
        <div style="text-align:center"><span class="secure-badge">🛡️ ENCRYPTED SESSION</span></div>
        <h1>Review Payment</h1>
        <p style="text-align:center; color: #555;">Verify your details before submitting.</p>
        <button onclick="alert('System: Validating security protocols...')">Confirm & Authenticate</button>
    </div>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)