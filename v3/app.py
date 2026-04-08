from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <body style="font-family: Arial; text-align: center; background-color: #e9f7ef;">
        <h1>Payment System - Version 3</h1>
        <div style="background: white; padding: 20px; display: inline-block; border-radius: 10px; border: 2px solid green;">
            <h2 style="color: green;">✔ Payment Success</h2>
            <p><b>Transaction ID:</b> #PAY-2026-XYZ</p>
            <p><b>Status:</b> Receipt Generated</p>
            <button style="background: green; color: white;">Download Receipt</button>
        </div>
    </body>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)