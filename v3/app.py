from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #ebfbee; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 2.5rem; border-radius: 25px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); width: 380px; text-align: center; }
        .check { background: #4caf50; color: white; width: 60px; height: 60px; line-height: 60px; border-radius: 50%; display: inline-block; font-size: 30px; margin-bottom: 20px; }
        h1 { color: #2e7d32; margin: 0; }
        .details { background: #f9f9f9; padding: 15px; border-radius: 12px; margin: 20px 0; text-align: left; font-size: 14px; color: #444; }
        .btn-receipt { background: #2e7d32; color: white; border: none; padding: 12px; border-radius: 10px; cursor: pointer; width: 100%; font-weight: bold; }
    </style>
    <div class="card">
        <div class="check">✓</div>
        <h1>Payment Success</h1>
        <div class="details">
            <p><strong>Order ID:</strong> #TXN-2026-9901</p>
            <p><strong>Date:</strong> April 08, 2026</p>
            <p><strong>Status:</strong> Completed</p>
        </div>
        <button class="btn-receipt">Download E-Receipt</button>
    </div>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)